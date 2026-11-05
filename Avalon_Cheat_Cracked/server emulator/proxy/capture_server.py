import ssl
import json
import datetime
import os
import socket
import http.server
import requests
import urllib3
from pathlib import Path

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SCRIPT_DIR = Path(__file__).parent.resolve()
LOG_DIR = SCRIPT_DIR / "captures"
LOG_DIR.mkdir(parents=True, exist_ok=True)

REAL_SERVER_IP = "104.21.83.246"
REAL_HOST = "api.eggshell.solutions"
CAPTURE_COUNT = 0


def log(msg):
    ts = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(f"[{ts}] {msg}", flush=True)


def save_capture(request_data, response_data):
    global CAPTURE_COUNT
    CAPTURE_COUNT += 1
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = LOG_DIR / f"capture_{CAPTURE_COUNT:03d}_{ts}.json"
    capture = {
        "timestamp": datetime.datetime.now().isoformat(),
        "request": request_data,
        "response": response_data,
    }
    with open(fname, "w") as f:
        json.dump(capture, f, indent=2, default=str)


class ProxyHandler(http.server.BaseHTTPRequestHandler):
    def _read_body(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length) if content_length > 0 else b""
        return body

    def _forward(self, method):
        body = self._read_body()
        req_headers = dict(self.headers)
        log(f"REQUEST {method} {self.path}")

        url = f"https://{REAL_HOST}" + self.path
        log(f"Forwarding to: {url}")

        orig_getaddrinfo = socket.getaddrinfo
        def patched_getaddrinfo(host, port, *args, **kwargs):
            if host == REAL_HOST:
                return orig_getaddrinfo(REAL_SERVER_IP, port, *args, **kwargs)
            return orig_getaddrinfo(host, port, *args, **kwargs)
        socket.getaddrinfo = patched_getaddrinfo

        fwd_headers = {}
        for key, val in req_headers.items():
            if key.lower() not in ("host", "content-length", "accept-encoding", "transfer-encoding"):
                fwd_headers[key] = val
        fwd_headers["Host"] = REAL_HOST

        try:
            resp = requests.request(
                method=method,
                url=url,
                headers=fwd_headers,
                data=body if body else None,
                verify=False,
                timeout=30,
                allow_redirects=False,
            )
            socket.getaddrinfo = orig_getaddrinfo

            resp_body = resp.content
            log(f"RESPONSE {resp.status_code} - {len(resp_body)} bytes")

            self.send_response(resp.status_code)
            for key, val in resp.headers.items():
                if key.lower() not in ("transfer-encoding", "content-encoding", "content-length"):
                    self.send_header(key, val)
            self.send_header("Content-Length", str(len(resp_body)))
            self.end_headers()
            self.wfile.write(resp_body)

        except Exception as e:
            socket.getaddrinfo = orig_getaddrinfo
            log(f"FORWARD ERROR: {e}")
            error_body = b'{"error":"proxy_error"}'
            self.send_response(502)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(error_body)))
            self.end_headers()
            self.wfile.write(error_body)

        req_data = {
            "method": method,
            "path": self.path,
            "headers": req_headers,
            "body_bytes": body.hex() if body else "",
            "body_length": len(body),
        }
        try:
            req_data["body_text"] = body.decode("utf-8")
        except:
            req_data["body_text"] = None

        save_capture(req_data, {
            "status": resp.status_code if 'resp' in dir() else 502,
            "headers": dict(resp.headers) if 'resp' in dir() else {},
            "body_bytes": resp_body.hex() if 'resp_body' in dir() else "",
            "body_length": len(resp_body) if 'resp_body' in dir() else 0,
        })

    def do_GET(self):
        self._forward("GET")

    def do_POST(self):
        self._forward("POST")

    def do_PUT(self):
        self._forward("PUT")

    def do_DELETE(self):
        self._forward("DELETE")

    def do_OPTIONS(self):
        self._forward("OPTIONS")

    def log_message(self, format, *args):
        pass


def main():
    cert_file = SCRIPT_DIR / "certs" / "proxy.crt"
    key_file = SCRIPT_DIR / "certs" / "proxy.key"

    if not cert_file.exists() or not key_file.exists():
        log("ERROR: Cert files not found in certs/ folder")
        return

    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(str(cert_file), str(key_file))

    server = http.server.HTTPServer(("0.0.0.0", 443), ProxyHandler)
    server.socket = ctx.wrap_socket(server.socket, server_side=True)

    log("=" * 50)
    log("PROXY RUNNING ON PORT 443")
    log(f"Forwarding to: {REAL_HOST} ({REAL_SERVER_IP})")
    log("Waiting for loader to connect...")
    log("=" * 50)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        log("Shutting down...")
        server.shutdown()


if __name__ == "__main__":
    main()
