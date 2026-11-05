# Avalon AI — Cracked

Full dump + analysis of a cracked build of **Avalon AI**, an AI color-aimbot
(CS2, Valorant, Fortnite, Apex, Rust, CoD, Overwatch, and ~20 other titles).

Cracked by Kai. Older crack — mostly working, a couple of bugs here and there.
Everything is in here: packed + unpacked loader, all cheat modules, the AI
model, the local server emulator used to bypass licensing, and the full
decompiled WPF menu source.

## Repo layout

| Path | What it is |
|---|---|
| `Avalon_Cheat_Cracked/RUN/` | Ready-to-run cracked copy — launch `XmlHelper.exe` |
| `Avalon_Cheat_Cracked/loader/` | Loader binaries: original packed, unpacked dump, AvalonML component |
| `Avalon_Cheat_Cracked/cheat modules/` | Core DLLs + the YOLO TensorRT aim model + unidentified modules |
| `Avalon_Cheat_Cracked/server emulator/` | MITM proxy + certs that emulate Avalon's backend (license bypass) |
| `Avalon_Cheat_Cracked/analysis/` | Decompiled GUI source (full WPF project, BAML resources, themes) |

## How the crack works

1. `server emulator/proxy/capture_server.py` + the certs in `server emulator/certs/`
   MITM the loader's traffic and fake the backend responses (license checks,
   payloads).
2. `RUN/XmlHelper.exe` (packed loader) starts against the local emulator instead
   of the real Avalon servers.
3. The loader drops/loads the modules in `cheat modules/`:
   `yolo_tensorrt_model.bin` does on-screen player detection,
   `overlay_skiaSharp.dll` draws the ESP overlay, `gui_wpf.dll` is the menu.
4. `loader/unpacked/XmlHelper_unpacked.exe` is the dumped unpacked loader for
   static analysis — the thing that made the rest of this repo possible.

## File-by-file index

Every file in the repo is documented in [`FILE_INDEX.md`](FILE_INDEX.md).

## Screenshots

![Avalon_Cheat_Cracked root — RUN, cheat modules, loader, analysis, server emulator](screenshots/image.webp)
![cheat modules — ai model, core dlls, unknown](<screenshots/image (1).webp>)
![analysis — decompiled_code, decompiled_code2, decompiled_config, decompiled_gui](<screenshots/image (2).webp>)
![server emulator — certs, proxy](<screenshots/image (3).webp>)
![loader — unpacked, avalon ml, original packed](<screenshots/image (4).webp>)
![decompiled_code — features, fonts, menu, Properties, resources, themes](<screenshots/image (5).webp>)
![features — aimbot, flickbot, input, rcs, triggerbot](<screenshots/image (6).webp>)
