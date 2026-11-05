import datetime
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from pathlib import Path

cert_dir = Path(__file__).parent.resolve() / "certs"
cert_dir.mkdir(parents=True, exist_ok=True)

key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COMMON_NAME, "api.eggshell.solutions"),
])

cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.datetime.now())
    .not_valid_after(datetime.datetime.now() + datetime.timedelta(days=365))
    .add_extension(
        x509.SubjectAlternativeName([
            x509.DNSName("api.eggshell.solutions"),
            x509.DNSName("eggshell.solutions"),
            x509.DNSName("www.eggshell.solutions"),
            x509.DNSName("localhost"),
        ]),
        critical=False,
    )
    .sign(key, hashes.SHA256())
)

cert_path = cert_dir / "proxy.crt"
key_path = cert_dir / "proxy.key"

with open(cert_path, "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

with open(key_path, "wb") as f:
    f.write(key.private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.TraditionalOpenSSL,
        serialization.NoEncryption(),
    ))

print(f"Cert: {cert_path}")
print(f"Key:  {key_path}")
print("Done!")
