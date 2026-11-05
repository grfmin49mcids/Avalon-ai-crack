# File-by-file index

Every file in `Avalon_Cheat_Cracked/`, grouped by directory.
`.baml` = compiled XAML (WPF UI resource extracted from the decompiled assembly).

## `RUN/` — ready-to-run cracked copy

| File | What it is |
|---|---|
| `XmlHelper.exe` | Packed loader executable — this is what you actually launch (32 MB) |
| `XmlHelper_backup.exe` | Untouched backup copy of the packed loader |
| `capture_server.py` | Local backend emulator — captures and answers the loader's server requests |
| `certs/proxy.crt` | TLS certificate the MITM proxy presents to the loader |
| `certs/proxy.key` | Private key for `proxy.crt` |

## `loader/` — loader binaries

| File | What it is |
|---|---|
| `avalon ml/AvalonML.exe` | ML component of the loader — hosts the AI detection pipeline |
| `original packed/XmlHelper.exe` | Original packed/protected loader, untouched |
| `unpacked/XmlHelper_unpacked.exe` | Dumped + unpacked loader (64 MB) used for static analysis |

## `cheat modules/` — payload modules

| File | What it is |
|---|---|
| `ai model/yolo_tensorrt_model.bin` | YOLO object-detection model serialized for TensorRT — detects players on screen for the aimbot (27 MB) |
| `core dlls/config_strings.dll` | Encrypted/plaintext config + feature strings used by the cheat |
| `core dlls/gui_wpf.dll` | The WPF menu/GUI assembly — the thing decompiled under `analysis/` |
| `core dlls/overlay_skiaSharp.dll` | SkiaSharp-based overlay renderer — draws ESP/aim visuals (11 MB) |
| `unknown/unknown_module_356KB.dll` | Unidentified 356 KB module |
| `unknown/unknown_module_1_356KB.dll` | Second copy/variant of the same unidentified module |

## `server emulator/` — license bypass backend

| File | What it is |
|---|---|
| `certs/proxy.crt` | MITM proxy certificate |
| `certs/proxy.key` | Proxy private key |
| `certs/proxy.pem` | PEM bundle of the proxy cert/key |
| `certs/proxy.pfx` | Windows-importable PFX bundle of the proxy cert/key |
| `proxy/capture_server.py` | Captures loader requests and emulates Avalon's backend (license check bypass) |
| `proxy/gen_cert.py` | Generates the proxy certs above |

## `analysis/` — decompiled source

### `decompiled_code/` — `gui_wpf.dll` decompiled into a WPF project

| File | What it is |
|---|---|
| `gui_wpf.csproj` | Reconstructed C# project file |
| `Properties/AssemblyInfo.cs` | Assembly metadata |
| `app.baml` | App.xaml compiled resources |
| `fodyweavers.xml` | Fody/Costura embedded-resource weaver config |
| `fonts/figtree-bold.ttf` | Figtree Bold font |
| `fonts/figtree-italic.ttf` | Figtree Italic font |
| `fonts/figtree-light.ttf` | Figtree Light font |
| `fonts/figtree-medium.ttf` | Figtree Medium font |
| `fonts/figtree-regular.ttf` | Figtree Regular font |
| `fonts/figtree-semibold.ttf` | Figtree Semibold font |
| `menu/controls/avalontabbutton.baml` | Sidebar tab button control |
| `menu/controls/configitem.baml` | Single config-preset row |
| `menu/controls/dialogs/acceptdialog.baml` | Generic accept modal |
| `menu/controls/dialogs/confirmationdialog.baml` | Yes/no confirm modal |
| `menu/controls/dialogs/hrefdialog.baml` | Modal containing a hyperlink |
| `menu/controls/dialogs/informationdialog.baml` | Info modal |
| `menu/controls/dialogs/restartdialog.baml` | Restart-prompt modal |
| `menu/controls/dialogs/textinputdialog.baml` | Text-entry modal |
| `menu/controls/featurealert.baml` | Alert banner inside a feature card |
| `menu/controls/featureboneselection.baml` | Aimbot target-bone selector UI |
| `menu/controls/featurecardstyle.baml` | Card container for one feature |
| `menu/controls/featurecheckbox.baml` | Checkbox bound to a feature toggle |
| `menu/controls/featurecolorbutton.baml` | Color-picker button (ESP colors etc.) |
| `menu/controls/featureslider.baml` | Slider bound to a numeric feature setting |
| `menu/controls/featuretextfield.baml` | Text field bound to a feature setting |
| `menu/controls/hierarchyline.baml` | Tree/indent connector line |
| `menu/controls/infodisplay.baml` | Read-only info display |
| `menu/controls/keybindrecorderbutton.baml` | Button that records a keybind |
| `menu/controls/languageselect.baml` | Language picker |
| `menu/controls/loading/loadingoverlay.baml` | Loading spinner overlay |
| `menu/controls/modelselector.baml` | AI model picker |
| `menu/controls/patterneditor/modifiergroupscontrol.baml` | Recoil pattern editor — modifier groups |
| `menu/controls/patterneditor/patterneditor.baml` | Recoil pattern editor root |
| `menu/controls/patterneditor/patterneditorcanvas.baml` | Recoil pattern editor drawing canvas |
| `menu/controls/patterneditor/patterneditortable.baml` | Recoil pattern editor table |
| `menu/controls/patterneditor/patterneditorwindow.baml` | Recoil pattern editor window |
| `menu/controls/performancegraph.baml` | FPS/performance graph |
| `menu/controls/performancepanel.baml` | Performance stats panel |
| `menu/controls/priorityitem.baml` | Target-priority list item |
| `menu/controls/recentconfigspanel.baml` | Recently used configs panel |
| `menu/converters/converters.baml` | Shared WPF value converters |
| `menu/mainwindow.baml` | Main window chrome |
| `menu/views/loadingview.baml` | Loading screen |
| `menu/views/main/1pc/menuview.baml` | Main menu for one-PC setup |
| `menu/views/main/features/aimbot/aimboteasyprofilecontrol.baml` | Aimbot — simplified profile editor |
| `menu/views/main/features/aimbot/aimbotprofilecontrol.baml` | Aimbot — full profile editor |
| `menu/views/main/features/aimbot/aimbotview.baml` | Aimbot settings page |
| `menu/views/main/features/aiview.baml` | AI detection/model settings page |
| `menu/views/main/features/configsview.baml` | Config management page |
| `menu/views/main/features/flickbot/flickbotprofilecontrol.baml` | Flickbot profile editor |
| `menu/views/main/features/flickbot/flickbotview.baml` | Flickbot settings page |
| `menu/views/main/features/input/bladedrivertab.baml` | Input method — BladeDriver |
| `menu/views/main/features/input/defaulttab.baml` | Input method — default/direct |
| `menu/views/main/features/input/inputdirectortab.baml` | Input method — InputDirector |
| `menu/views/main/features/input/kmbprotab.baml` | Input method — KMB Pro box |
| `menu/views/main/features/input/kmnettab.baml` | Input method — KMNet |
| `menu/views/main/features/input/makcutab.baml` | Input method — Makcu |
| `menu/views/main/features/input/unifiedremotetab.baml` | Input method — Unified Remote |
| `menu/views/main/features/input/xppentab.baml` | Input method — XP-Pen tablet |
| `menu/views/main/features/inputview.baml` | Input method parent page |
| `menu/views/main/features/rcs/rcsprofilecontrol.baml` | Recoil-control profile editor |
| `menu/views/main/features/rcs/rcsview.baml` | Recoil-control settings page |
| `menu/views/main/features/triggerbot/triggerboteasyprofilecontrol.baml` | Triggerbot — simplified profile editor |
| `menu/views/main/features/triggerbot/triggerbotprofilecontrol.baml` | Triggerbot — full profile editor |
| `menu/views/main/features/triggerbot/triggerbotview.baml` | Triggerbot settings page |
| `menu/views/main/features/visualsview.baml` | ESP/visuals settings page |
| `menu/views/main/games/apexgameview.baml` | Per-game settings — Apex Legends |
| `menu/views/main/games/battlefieldgameview.baml` | Per-game settings — Battlefield |
| `menu/views/main/games/bloodstrikegameview.baml` | Per-game settings — Blood Strike |
| `menu/views/main/games/callofdutygameview.baml` | Per-game settings — Call of Duty |
| `menu/views/main/games/cs2gameview.baml` | Per-game settings — CS2 |
| `menu/views/main/games/deadlockgameview.baml` | Per-game settings — Deadlock |
| `menu/views/main/games/empulsegameview.baml` | Per-game settings — Empulse |
| `menu/views/main/games/fortnitegameview.baml` | Per-game settings — Fortnite |
| `menu/views/main/games/fragpunkgameview.baml` | Per-game settings — FragPunk |
| `menu/views/main/games/halogameview.baml` | Per-game settings — Halo |
| `menu/views/main/games/highguardgameview.baml` | Per-game settings — Highguard |
| `menu/views/main/games/marathongameview.baml` | Per-game settings — Marathon |
| `menu/views/main/games/marvelrivalsgameview.baml` | Per-game settings — Marvel Rivals |
| `menu/views/main/games/overwatchgameview.baml` | Per-game settings — Overwatch |
| `menu/views/main/games/pubggameview.baml` | Per-game settings — PUBG |
| `menu/views/main/games/rainbowsixgameview.baml` | Per-game settings — Rainbow Six |
| `menu/views/main/games/robloxgameview.baml` | Per-game settings — Roblox |
| `menu/views/main/games/rustgameview.baml` | Per-game settings — Rust |
| `menu/views/main/games/splitgate2gameview.baml` | Per-game settings — Splitgate 2 |
| `menu/views/main/games/stalcraftxgameview.baml` | Per-game settings — Stalcraft X |
| `menu/views/main/games/strinovagameview.baml` | Per-game settings — Strinova |
| `menu/views/main/games/thefinalsgameview.baml` | Per-game settings — The Finals |
| `menu/views/main/games/universalgameview.baml` | Generic/any-game settings view |
| `menu/views/main/games/valorantgameview.baml` | Per-game settings — Valorant |
| `menu/views/main/mainview.baml` | Main view container |
| `menu/views/main/preview/featurepreview.baml` | Live preview of a feature |
| `menu/views/main/preview/sidepanel.baml` | Side panel next to preview |
| `menu/views/setup/compatibilitycheckview.baml` | Setup wizard — hardware compat check |
| `menu/views/setup/gameselection.baml` | Setup wizard — pick your game |
| `menu/views/setup/onepc/lookingforgame.baml` | One-PC setup — scanning for game process |
| `menu/views/setup/onepc/onepcsetupview.baml` | One-PC setup page |
| `menu/views/setup/onepc/processselectionview.baml` | One-PC setup — pick the game process |
| `menu/views/setup/setupkindselection.baml` | Setup wizard — choose 1-PC vs 2-PC |
| `menu/views/setup/twopc/calibrationdialog.baml` | Two-PC setup — calibration dialog |
| `menu/views/setup/twopc/capturecarddeviceselection.baml` | Two-PC setup — pick capture card |
| `menu/views/setup/twopc/capturecardpreview.baml` | Two-PC setup — capture card preview |
| `menu/views/setup/twopc/ndipreview.baml` | Two-PC setup — NDI stream preview |
| `menu/views/setup/twopc/ndisourceselection.baml` | Two-PC setup — pick NDI source |
| `menu/views/setup/twopc/twopccapturemethodselection.baml` | Two-PC setup — pick capture method |
| `menu/views/setup/twopc/twopcsetupview.baml` | Two-PC setup page |
| `resources/avalon_big.png` | Large Avalon logo |
| `resources/logo.png` | Avalon logo |
| `resources/flags/cn.svg` | Flag icon — Chinese |
| `resources/flags/es.svg` | Flag icon — Spanish |
| `resources/flags/fi.svg` | Flag icon — Finnish |
| `resources/flags/kr.svg` | Flag icon — Korean |
| `resources/flags/ru.svg` | Flag icon — Russian |
| `resources/flags/tr.svg` | Flag icon — Turkish |
| `resources/flags/us.svg` | Flag icon — English/US |
| `themes/base/allicons.baml` | Full icon-geometry set used by the menu |
| `themes/base/brushes.baml` | Brush definitions |
| `themes/base/colors.baml` | Color palette |
| `themes/base/converters.baml` | Theme-level converters |
| `themes/base/fonts.baml` | Font definitions |
| `themes/base/sizes.baml` | Size/spacing tokens |
| `themes/controls/buttonstyles.baml` | Button styles |
| `themes/controls/checkboxstyles.baml` | Checkbox styles |
| `themes/controls/colorpickerstyles.baml` | Color picker styles |
| `themes/controls/colortogglestyles.baml` | Color toggle styles |
| `themes/controls/comboboxstyles.baml` | ComboBox styles |
| `themes/controls/configcardstyles.baml` | Config card styles |
| `themes/controls/contextmenustyles.baml` | Context menu styles |
| `themes/controls/featurecardstyles.baml` | Feature card styles |
| `themes/controls/filepickerstyles.baml` | File picker styles |
| `themes/controls/geartogglestyles.baml` | Gear/settings toggle styles |
| `themes/controls/keybindpickerstyles.baml` | Keybind picker styles |
| `themes/controls/labeledsliderstyles.baml` | Labeled slider styles |
| `themes/controls/lightraystyles.baml` | Decorative light-ray styles |
| `themes/controls/listboxstyles.baml` | ListBox styles |
| `themes/controls/loadingspinnerstyles.baml` | Loading spinner styles |
| `themes/controls/miscstyles.baml` | Misc styles |
| `themes/controls/modalstyles.baml` | Modal styles |
| `themes/controls/rangesliderstyles.baml` | Range slider styles |
| `themes/controls/scrollbarstyles.baml` | Scrollbar styles |
| `themes/controls/searchboxstyles.baml` | Search box styles |
| `themes/controls/sidepanelstyles.baml` | Side panel styles |
| `themes/controls/sliderstyles.baml` | Slider styles |
| `themes/controls/statcardstyles.baml` | Stat card styles |
| `themes/controls/textboxstyles.baml` | TextBox styles |
| `themes/controls/togglegroupstyles.baml` | Toggle group styles |
| `themes/controls/viewtabstyles.baml` | View tab styles |
| `themes/generic.baml` | Theme root resource dictionary |

### `decompiled_code2/` — single-file decompile

| File | What it is |
|---|---|
| `gui_wpf.decompiled.cs` | `gui_wpf.dll` decompiled into one big C# file — the actual code behind all the BAML above |

### `decompiled_config/` — config module decompile

| File | What it is |
|---|---|
| `config_strings.decompiled.cs` | `config_strings.dll` decompiled — all the cheat's config/feature strings |

### `decompiled_gui/decompiled_gui/` — second decompile of `gui_wpf.dll`

Same structure/content as `decompiled_code/` — a parallel decompile pass.

| File | What it is |
|---|---|
| `Properties/AssemblyInfo.cs` | Assembly metadata |
| `app.baml` | App.xaml compiled resources |
| `fodyweavers.xml` | Fody weaver config |
| `fonts/figtree-bold.ttf` | Figtree Bold font |
| `fonts/figtree-italic.ttf` | Figtree Italic font |
| `fonts/figtree-light.ttf` | Figtree Light font |
| `fonts/figtree-medium.ttf` | Figtree Medium font |
| `fonts/figtree-regular.ttf` | Figtree Regular font |
| `fonts/figtree-semibold.ttf` | Figtree Semibold font |
| `menu/controls/avalontabbutton.baml` | Sidebar tab button control |
| `menu/controls/configitem.baml` | Single config-preset row |
| `menu/controls/dialogs/acceptdialog.baml` | Generic accept modal |
| `menu/controls/dialogs/confirmationdialog.baml` | Yes/no confirm modal |
| `menu/controls/dialogs/hrefdialog.baml` | Modal containing a hyperlink |
| `menu/controls/dialogs/informationdialog.baml` | Info modal |
| `menu/controls/dialogs/restartdialog.baml` | Restart-prompt modal |
| `menu/controls/dialogs/textinputdialog.baml` | Text-entry modal |
| `menu/controls/featurealert.baml` | Alert banner inside a feature card |
| `menu/controls/featureboneselection.baml` | Aimbot target-bone selector UI |
| `menu/controls/featurecheckbox.baml` | Checkbox bound to a feature toggle |
| `menu/controls/featurecolorbutton.baml` | Color-picker button |
| `menu/controls/featureslider.baml` | Slider bound to a numeric setting |
| `menu/controls/featuretextfield.baml` | Text field bound to a feature setting |
| `menu/controls/hierarchyline.baml` | Tree/indent connector line |
| `menu/controls/infodisplay.baml` | Read-only info display |
| `menu/controls/keybindrecorderbutton.baml` | Button that records a keybind |
| `menu/controls/languageselect.baml` | Language picker |
| `menu/controls/loading/loadingoverlay.baml` | Loading spinner overlay |
| `menu/controls/modelselector.baml` | AI model picker |
| `menu/controls/patterneditor/modifiergroupscontrol.baml` | Recoil pattern editor — modifier groups |
| `menu/controls/patterneditor/patterneditor.baml` | Recoil pattern editor root |
| `menu/controls/patterneditor/patterneditorcanvas.baml` | Recoil pattern editor canvas |
| `menu/controls/patterneditor/patterneditortable.baml` | Recoil pattern editor table |
| `menu/controls/patterneditor/patterneditorwindow.baml` | Recoil pattern editor window |
| `menu/controls/performancegraph.baml` | FPS/performance graph |
| `menu/controls/performancepanel.baml` | Performance stats panel |
| `menu/controls/priorityitem.baml` | Target-priority list item |
| `menu/controls/recentconfigspanel.baml` | Recently used configs panel |
| `menu/converters/converters.baml` | Shared WPF value converters |
| `menu/mainwindow.baml` | Main window chrome |
| `menu/views/loadingview.baml` | Loading screen |
| `menu/views/main/1pc/menuview.baml` | Main menu for one-PC setup |
| `menu/views/main/features/aimbot/aimboteasyprofilecontrol.baml` | Aimbot — simplified profile editor |
| `menu/views/main/features/aimbot/aimbotprofilecontrol.baml` | Aimbot — full profile editor |
| `menu/views/main/features/aimbot/aimbotview.baml` | Aimbot settings page |
| `menu/views/main/features/aiview.baml` | AI detection/model settings page |
| `menu/views/main/features/configsview.baml` | Config management page |
| `menu/views/main/features/flickbot/flickbotprofilecontrol.baml` | Flickbot profile editor |
| `menu/views/main/features/flickbot/flickbotview.baml` | Flickbot settings page |
| `menu/views/main/features/input/bladedrivertab.baml` | Input method — BladeDriver |
| `menu/views/main/features/input/defaulttab.baml` | Input method — default/direct |
| `menu/views/main/features/input/inputdirectortab.baml` | Input method — InputDirector |
| `menu/views/main/features/input/kmbprotab.baml` | Input method — KMB Pro box |
| `menu/views/main/features/input/kmnettab.baml` | Input method — KMNet |
| `menu/views/main/features/input/makcutab.baml` | Input method — Makcu |
| `menu/views/main/features/input/unifiedremotetab.baml` | Input method — Unified Remote |
| `menu/views/main/features/input/xppentab.baml` | Input method — XP-Pen tablet |
| `menu/views/main/features/inputview.baml` | Input method parent page |
| `menu/views/main/features/rcs/rcsprofilecontrol.baml` | Recoil-control profile editor |
| `menu/views/main/features/rcs/rcsview.baml` | Recoil-control settings page |
| `menu/views/main/features/triggerbot/triggerboteasyprofilecontrol.baml` | Triggerbot — simplified profile editor |
| `menu/views/main/features/triggerbot/triggerbotprofilecontrol.baml` | Triggerbot — full profile editor |
| `menu/views/main/features/triggerbot/triggerbotview.baml` | Triggerbot settings page |
| `menu/views/main/features/visualsview.baml` | ESP/visuals settings page |
| `menu/views/main/games/apexgameview.baml` | Per-game settings — Apex Legends |
| `menu/views/main/games/battlefieldgameview.baml` | Per-game settings — Battlefield |
| `menu/views/main/games/bloodstrikegameview.baml` | Per-game settings — Blood Strike |
| `menu/views/main/games/callofdutygameview.baml` | Per-game settings — Call of Duty |
| `menu/views/main/games/cs2gameview.baml` | Per-game settings — CS2 |
| `menu/views/main/games/deadlockgameview.baml` | Per-game settings — Deadlock |
| `menu/views/main/games/empulsegameview.baml` | Per-game settings — Empulse |
| `menu/views/main/games/fortnitegameview.baml` | Per-game settings — Fortnite |
| `menu/views/main/games/fragpunkgameview.baml` | Per-game settings — FragPunk |
| `menu/views/main/games/halogameview.baml` | Per-game settings — Halo |
| `menu/views/main/games/highguardgameview.baml` | Per-game settings — Highguard |
| `menu/views/main/games/marathongameview.baml` | Per-game settings — Marathon |
| `menu/views/main/games/marvelrivalsgameview.baml` | Per-game settings — Marvel Rivals |
| `menu/views/main/games/overwatchgameview.baml` | Per-game settings — Overwatch |
| `menu/views/main/games/pubggameview.baml` | Per-game settings — PUBG |
| `menu/views/main/games/rainbowsixgameview.baml` | Per-game settings — Rainbow Six |
| `menu/views/main/games/robloxgameview.baml` | Per-game settings — Roblox |
| `menu/views/main/games/rustgameview.baml` | Per-game settings — Rust |
| `menu/views/main/games/splitgate2gameview.baml` | Per-game settings — Splitgate 2 |
| `menu/views/main/games/stalcraftxgameview.baml` | Per-game settings — Stalcraft X |
| `menu/views/main/games/strinovagameview.baml` | Per-game settings — Strinova |
| `menu/views/main/games/thefinalsgameview.baml` | Per-game settings — The Finals |
| `menu/views/main/games/universalgameview.baml` | Generic/any-game settings view |
| `menu/views/main/games/valorantgameview.baml` | Per-game settings — Valorant |
| `menu/views/main/mainview.baml` | Main view container |
| `menu/views/main/preview/featurepreview.baml` | Live preview of a feature |
| `menu/views/main/preview/sidepanel.baml` | Side panel next to preview |
| `menu/views/setup/compatibilitycheckview.baml` | Setup wizard — hardware compat check |
| `menu/views/setup/gameselection.baml` | Setup wizard — pick your game |
| `menu/views/setup/onepc/lookingforgame.baml` | One-PC setup — scanning for game process |
| `menu/views/setup/onepc/onepcsetupview.baml` | One-PC setup page |
| `menu/views/setup/onepc/processselectionview.baml` | One-PC setup — pick the game process |
| `menu/views/setup/setupkindselection.baml` | Setup wizard — choose 1-PC vs 2-PC |
| `menu/views/setup/twopc/calibrationdialog.baml` | Two-PC setup — calibration dialog |
| `menu/views/setup/twopc/capturecarddeviceselection.baml` | Two-PC setup — pick capture card |
| `menu/views/setup/twopc/capturecardpreview.baml` | Two-PC setup — capture card preview |
| `menu/views/setup/twopc/ndipreview.baml` | Two-PC setup — NDI stream preview |
| `menu/views/setup/twopc/ndisourceselection.baml` | Two-PC setup — pick NDI source |
| `menu/views/setup/twopc/twopccapturemethodselection.baml` | Two-PC setup — pick capture method |
| `menu/views/setup/twopc/twopcsetupview.baml` | Two-PC setup page |
| `resources/avalon_big.png` | Large Avalon logo |
| `resources/logo.png` | Avalon logo |
| `resources/flags/cn.svg` | Flag icon — Chinese |
| `resources/flags/es.svg` | Flag icon — Spanish |
| `resources/flags/fi.svg` | Flag icon — Finnish |
| `resources/flags/kr.svg` | Flag icon — Korean |
| `resources/flags/ru.svg` | Flag icon — Russian |
| `resources/flags/tr.svg` | Flag icon — Turkish |
| `resources/flags/us.svg` | Flag icon — English/US |
| `themes/base/allicons.baml` | Full icon-geometry set |
| `themes/base/brushes.baml` | Brush definitions |
| `themes/base/colors.baml` | Color palette |
| `themes/base/converters.baml` | Theme-level converters |
| `themes/base/fonts.baml` | Font definitions |
| `themes/base/sizes.baml` | Size/spacing tokens |
| `themes/controls/buttonstyles.baml` | Button styles |
| `themes/controls/checkboxstyles.baml` | Checkbox styles |
| `themes/controls/colorpickerstyles.baml` | Color picker styles |
| `themes/controls/colortogglestyles.baml` | Color toggle styles |
| `themes/controls/comboboxstyles.baml` | ComboBox styles |
| `themes/controls/configcardstyles.baml` | Config card styles |
| `themes/controls/contextmenustyles.baml` | Context menu styles |
| `themes/controls/featurecardstyles.baml` | Feature card styles |
| `themes/controls/filepickerstyles.baml` | File picker styles |
| `themes/controls/geartogglestyles.baml` | Gear/settings toggle styles |
| `themes/controls/keybindpickerstyles.baml` | Keybind picker styles |
| `themes/controls/labeledsliderstyles.baml` | Labeled slider styles |
| `themes/controls/lightraystyles.baml` | Decorative light-ray styles |
| `themes/controls/listboxstyles.baml` | ListBox styles |
| `themes/controls/loadingspinnerstyles.baml` | Loading spinner styles |
| `themes/controls/miscstyles.baml` | Misc styles |
| `themes/controls/modalstyles.baml` | Modal styles |
| `themes/controls/rangesliderstyles.baml` | Range slider styles |
| `themes/controls/scrollbarstyles.baml` | Scrollbar styles |
| `themes/controls/searchboxstyles.baml` | Search box styles |
| `themes/controls/sidepanelstyles.baml` | Side panel styles |
| `themes/controls/sliderstyles.baml` | Slider styles |
| `themes/controls/statcardstyles.baml` | Stat card styles |
| `themes/controls/textboxstyles.baml` | TextBox styles |
| `themes/controls/togglegroupstyles.baml` | Toggle group styles |
| `themes/controls/viewtabstyles.baml` | View tab styles |
| `themes/generic.baml` | Theme root resource dictionary |
| `zx_4e23ae116b914ed3038933b7f1ed5f0e.csproj` | Auto-generated temp project file from the decompiler |
