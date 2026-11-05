# every file explained

every file in the repo and what it is. baml is just compiled xaml, its the menu ui pulled out of the dll

## RUN

**XmlHelper.exe** : the loader, launch this one (32mb)

**XmlHelper_backup.exe** : backup of the packed loader

**capture_server.py** : fakes avalons backend, captures the loaders requests and answers them

**certs/proxy.crt** : cert the proxy shows the loader

**certs/proxy.key** : private key for that cert

## loader

**avalon ml/AvalonML.exe** : the ml part of the loader, runs the detection model

**original packed/XmlHelper.exe** : the original packed loader, untouched

**unpacked/XmlHelper_unpacked.exe** : the loader after i unpacked it (64mb), used for analysis

## cheat modules

**ai model/yolo_tensorrt_model.bin** : the yolo model serialized for tensorrt, detects players on screen for the aimbot (27mb)

**core dlls/config_strings.dll** : all the config and feature strings

**core dlls/gui_wpf.dll** : the menu, this is the dll everything in analysis came from

**core dlls/overlay_skiaSharp.dll** : draws the esp overlay with skia (11mb)

**unknown/unknown_module_356KB.dll** : never figured out what this one does

**unknown/unknown_module_1_356KB.dll** : same unknown module, second copy

## server emulator

**certs/proxy.crt** : the proxy cert

**certs/proxy.key** : its private key

**certs/proxy.pem** : same thing in pem form

**certs/proxy.pfx** : same thing in pfx form so windows can import it

**proxy/capture_server.py** : the actual emulator, answers the loaders requests so the license check passes

**proxy/gen_cert.py** : makes the certs above

## analysis decompiled_code

this is gui_wpf.dll decompiled back into a wpf project

**gui_wpf.csproj** : the project file

**Properties/AssemblyInfo.cs** : assembly info

**app.baml** : app resources

**fodyweavers.xml** : fody config for embedded resources

**fonts/figtree-bold.ttf** : figtree bold

**fonts/figtree-italic.ttf** : figtree italic

**fonts/figtree-light.ttf** : figtree light

**fonts/figtree-medium.ttf** : figtree medium

**fonts/figtree-regular.ttf** : figtree regular

**fonts/figtree-semibold.ttf** : figtree semibold

### controls

**avalontabbutton.baml** : the sidebar tab buttons

**configitem.baml** : one config entry in the list

**dialogs/acceptdialog.baml** : accept popup

**dialogs/confirmationdialog.baml** : yes or no popup

**dialogs/hrefdialog.baml** : popup with a link in it

**dialogs/informationdialog.baml** : info popup

**dialogs/restartdialog.baml** : restart prompt

**dialogs/textinputdialog.baml** : popup where u type something

**featurealert.baml** : warning banner on a feature

**featureboneselection.baml** : pick which bone the aimbot aims at

**featurecardstyle.baml** : the card each feature sits in

**featurecheckbox.baml** : checkbox for toggling a feature

**featurecolorbutton.baml** : color picker button, for esp colors and stuff

**featureslider.baml** : slider for numbers like fov and smoothness

**featuretextfield.baml** : text field for a setting

**hierarchyline.baml** : the little line showing whats nested under what

**infodisplay.baml** : just shows info

**keybindrecorderbutton.baml** : button that records what key u press

**languageselect.baml** : language picker

**loading/loadingoverlay.baml** : spinner overlay while it loads

**modelselector.baml** : pick which ai model to use

**patterneditor/modifiergroupscontrol.baml** : recoil pattern editor, modifier groups

**patterneditor/patterneditor.baml** : the recoil pattern editor itself

**patterneditor/patterneditorcanvas.baml** : the canvas u draw the pattern on

**patterneditor/patterneditortable.baml** : pattern editor table view

**patterneditor/patterneditorwindow.baml** : the window the pattern editor opens in

**performancegraph.baml** : fps graph

**performancepanel.baml** : perf stats panel

**priorityitem.baml** : target priority list entry

**recentconfigspanel.baml** : panel showing recently used configs

**converters/converters.baml** : shared value converters

**mainwindow.baml** : the main window

### views

**loadingview.baml** : loading screen

**main/1pc/menuview.baml** : main menu for one pc setups

**main/features/aimbot/aimboteasyprofilecontrol.baml** : aimbot profile editor, simple version

**main/features/aimbot/aimbotprofilecontrol.baml** : aimbot profile editor, full version

**main/features/aimbot/aimbotview.baml** : the aimbot page

**main/features/aiview.baml** : ai detection settings page

**main/features/configsview.baml** : config manager page

**main/features/flickbot/flickbotprofilecontrol.baml** : flickbot profile editor

**main/features/flickbot/flickbotview.baml** : the flickbot page

**main/features/input/bladedrivertab.baml** : input method, bladedriver

**main/features/input/defaulttab.baml** : input method, default

**main/features/input/inputdirectortab.baml** : input method, inputdirector

**main/features/input/kmbprotab.baml** : input method, kmb pro box

**main/features/input/kmnettab.baml** : input method, kmnet

**main/features/input/makcutab.baml** : input method, makcu

**main/features/input/unifiedremotetab.baml** : input method, unified remote

**main/features/input/xppentab.baml** : input method, xppen tablet

**main/features/inputview.baml** : the page all the input tabs sit in

**main/features/rcs/rcsprofilecontrol.baml** : recoil control profile editor

**main/features/rcs/rcsview.baml** : recoil control page

**main/features/triggerbot/triggerboteasyprofilecontrol.baml** : triggerbot profile editor, simple version

**main/features/triggerbot/triggerbotprofilecontrol.baml** : triggerbot profile editor, full version

**main/features/triggerbot/triggerbotview.baml** : the triggerbot page

**main/features/visualsview.baml** : esp and visuals page

**main/games/apexgameview.baml** : apex settings

**main/games/battlefieldgameview.baml** : battlefield settings

**main/games/bloodstrikegameview.baml** : blood strike settings

**main/games/callofdutygameview.baml** : cod settings

**main/games/cs2gameview.baml** : cs2 settings

**main/games/deadlockgameview.baml** : deadlock settings

**main/games/empulsegameview.baml** : empulse settings

**main/games/fortnitegameview.baml** : fortnite settings

**main/games/fragpunkgameview.baml** : fragpunk settings

**main/games/halogameview.baml** : halo settings

**main/games/highguardgameview.baml** : highguard settings

**main/games/marathongameview.baml** : marathon settings

**main/games/marvelrivalsgameview.baml** : marvel rivals settings

**main/games/overwatchgameview.baml** : overwatch settings

**main/games/pubggameview.baml** : pubg settings

**main/games/rainbowsixgameview.baml** : r6 settings

**main/games/robloxgameview.baml** : roblox settings

**main/games/rustgameview.baml** : rust settings

**main/games/splitgate2gameview.baml** : splitgate 2 settings

**main/games/stalcraftxgameview.baml** : stalcraft x settings

**main/games/strinovagameview.baml** : strinova settings

**main/games/thefinalsgameview.baml** : the finals settings

**main/games/universalgameview.baml** : generic settings for any game

**main/games/valorantgameview.baml** : valorant settings

**main/mainview.baml** : main view everything sits in

**main/preview/featurepreview.baml** : live preview of a feature

**main/preview/sidepanel.baml** : side panel next to the preview

**setup/compatibilitycheckview.baml** : setup wizard, checks if ur pc works

**setup/gameselection.baml** : setup wizard, pick ur game

**setup/onepc/lookingforgame.baml** : one pc setup, scanning for the game

**setup/onepc/onepcsetupview.baml** : one pc setup page

**setup/onepc/processselectionview.baml** : one pc setup, pick the game process

**setup/setupkindselection.baml** : setup wizard, one pc or two pc

**setup/twopc/calibrationdialog.baml** : two pc setup, calibration popup

**setup/twopc/capturecarddeviceselection.baml** : two pc setup, pick ur capture card

**setup/twopc/capturecardpreview.baml** : two pc setup, capture card preview

**setup/twopc/ndipreview.baml** : two pc setup, ndi preview

**setup/twopc/ndisourceselection.baml** : two pc setup, pick the ndi source

**setup/twopc/twopccapturemethodselection.baml** : two pc setup, pick how u capture

**setup/twopc/twopcsetupview.baml** : two pc setup page

### resources and themes

**resources/avalon_big.png** : big avalon logo

**resources/logo.png** : avalon logo

**resources/flags/cn.svg** : chinese flag for the language picker

**resources/flags/es.svg** : spanish flag

**resources/flags/fi.svg** : finnish flag

**resources/flags/kr.svg** : korean flag

**resources/flags/ru.svg** : russian flag

**resources/flags/tr.svg** : turkish flag

**resources/flags/us.svg** : us flag

**themes/base/allicons.baml** : every icon in the menu

**themes/base/brushes.baml** : brush defs

**themes/base/colors.baml** : the color palette

**themes/base/converters.baml** : theme converters

**themes/base/fonts.baml** : font defs

**themes/base/sizes.baml** : size and spacing values

**themes/controls/buttonstyles.baml** : button styles

**themes/controls/checkboxstyles.baml** : checkbox styles

**themes/controls/colorpickerstyles.baml** : color picker styles

**themes/controls/colortogglestyles.baml** : color toggle styles

**themes/controls/comboboxstyles.baml** : combobox styles

**themes/controls/configcardstyles.baml** : config card styles

**themes/controls/contextmenustyles.baml** : right click menu styles

**themes/controls/featurecardstyles.baml** : feature card styles

**themes/controls/filepickerstyles.baml** : file picker styles

**themes/controls/geartogglestyles.baml** : gear toggle styles

**themes/controls/keybindpickerstyles.baml** : keybind picker styles

**themes/controls/labeledsliderstyles.baml** : labeled slider styles

**themes/controls/lightraystyles.baml** : the light ray effect in the menu

**themes/controls/listboxstyles.baml** : listbox styles

**themes/controls/loadingspinnerstyles.baml** : loading spinner styles

**themes/controls/miscstyles.baml** : misc styles

**themes/controls/modalstyles.baml** : modal styles

**themes/controls/rangesliderstyles.baml** : range slider styles

**themes/controls/scrollbarstyles.baml** : scrollbar styles

**themes/controls/searchboxstyles.baml** : search box styles

**themes/controls/sidepanelstyles.baml** : side panel styles

**themes/controls/sliderstyles.baml** : slider styles

**themes/controls/statcardstyles.baml** : stat card styles

**themes/controls/textboxstyles.baml** : textbox styles

**themes/controls/togglegroupstyles.baml** : toggle group styles

**themes/controls/viewtabstyles.baml** : view tab styles

**themes/generic.baml** : the root theme file that pulls it all together

## decompiled_code2

**gui_wpf.decompiled.cs** : the whole gui dll decompiled into one big cs file, this is the actual code behind all the baml

## decompiled_config

**config_strings.decompiled.cs** : config_strings.dll decompiled, all the config and feature strings in the cheat

## decompiled_gui

second decompile of gui_wpf.dll, same files as decompiled_code

**Properties/AssemblyInfo.cs** : assembly info

**app.baml** : app resources

**fodyweavers.xml** : fody config

**fonts/figtree-bold.ttf** : figtree bold

**fonts/figtree-italic.ttf** : figtree italic

**fonts/figtree-light.ttf** : figtree light

**fonts/figtree-medium.ttf** : figtree medium

**fonts/figtree-regular.ttf** : figtree regular

**fonts/figtree-semibold.ttf** : figtree semibold

**menu/controls/avalontabbutton.baml** : sidebar tab buttons

**menu/controls/configitem.baml** : one config entry

**menu/controls/dialogs/acceptdialog.baml** : accept popup

**menu/controls/dialogs/confirmationdialog.baml** : yes or no popup

**menu/controls/dialogs/hrefdialog.baml** : popup with a link

**menu/controls/dialogs/informationdialog.baml** : info popup

**menu/controls/dialogs/restartdialog.baml** : restart prompt

**menu/controls/dialogs/textinputdialog.baml** : popup where u type

**menu/controls/featurealert.baml** : warning banner on a feature

**menu/controls/featureboneselection.baml** : pick the aimbot bone

**menu/controls/featurecheckbox.baml** : feature toggle checkbox

**menu/controls/featurecolorbutton.baml** : color picker button

**menu/controls/featureslider.baml** : slider for numeric settings

**menu/controls/featuretextfield.baml** : text field for a setting

**menu/controls/hierarchyline.baml** : nesting line

**menu/controls/infodisplay.baml** : shows info

**menu/controls/keybindrecorderbutton.baml** : records keybinds

**menu/controls/languageselect.baml** : language picker

**menu/controls/loading/loadingoverlay.baml** : loading overlay

**menu/controls/modelselector.baml** : ai model picker

**menu/controls/patterneditor/modifiergroupscontrol.baml** : recoil pattern modifier groups

**menu/controls/patterneditor/patterneditor.baml** : recoil pattern editor

**menu/controls/patterneditor/patterneditorcanvas.baml** : pattern drawing canvas

**menu/controls/patterneditor/patterneditortable.baml** : pattern table

**menu/controls/patterneditor/patterneditorwindow.baml** : pattern editor window

**menu/controls/performancegraph.baml** : fps graph

**menu/controls/performancepanel.baml** : perf stats panel

**menu/controls/priorityitem.baml** : target priority entry

**menu/controls/recentconfigspanel.baml** : recent configs panel

**menu/converters/converters.baml** : value converters

**menu/mainwindow.baml** : main window

**menu/views/loadingview.baml** : loading screen

**menu/views/main/1pc/menuview.baml** : main menu for one pc

**menu/views/main/features/aimbot/aimboteasyprofilecontrol.baml** : simple aimbot profile editor

**menu/views/main/features/aimbot/aimbotprofilecontrol.baml** : full aimbot profile editor

**menu/views/main/features/aimbot/aimbotview.baml** : aimbot page

**menu/views/main/features/aiview.baml** : ai settings page

**menu/views/main/features/configsview.baml** : config manager page

**menu/views/main/features/flickbot/flickbotprofilecontrol.baml** : flickbot profile editor

**menu/views/main/features/flickbot/flickbotview.baml** : flickbot page

**menu/views/main/features/input/bladedrivertab.baml** : bladedriver input

**menu/views/main/features/input/defaulttab.baml** : default input

**menu/views/main/features/input/inputdirectortab.baml** : inputdirector input

**menu/views/main/features/input/kmbprotab.baml** : kmb pro input

**menu/views/main/features/input/kmnettab.baml** : kmnet input

**menu/views/main/features/input/makcutab.baml** : makcu input

**menu/views/main/features/input/unifiedremotetab.baml** : unified remote input

**menu/views/main/features/input/xppentab.baml** : xppen input

**menu/views/main/features/inputview.baml** : input page

**menu/views/main/features/rcs/rcsprofilecontrol.baml** : rcs profile editor

**menu/views/main/features/rcs/rcsview.baml** : rcs page

**menu/views/main/features/triggerbot/triggerboteasyprofilecontrol.baml** : simple triggerbot profile editor

**menu/views/main/features/triggerbot/triggerbotprofilecontrol.baml** : full triggerbot profile editor

**menu/views/main/features/triggerbot/triggerbotview.baml** : triggerbot page

**menu/views/main/features/visualsview.baml** : visuals page

**menu/views/main/games/apexgameview.baml** : apex settings

**menu/views/main/games/battlefieldgameview.baml** : battlefield settings

**menu/views/main/games/bloodstrikegameview.baml** : blood strike settings

**menu/views/main/games/callofdutygameview.baml** : cod settings

**menu/views/main/games/cs2gameview.baml** : cs2 settings

**menu/views/main/games/deadlockgameview.baml** : deadlock settings

**menu/views/main/games/empulsegameview.baml** : empulse settings

**menu/views/main/games/fortnitegameview.baml** : fortnite settings

**menu/views/main/games/fragpunkgameview.baml** : fragpunk settings

**menu/views/main/games/halogameview.baml** : halo settings

**menu/views/main/games/highguardgameview.baml** : highguard settings

**menu/views/main/games/marathongameview.baml** : marathon settings

**menu/views/main/games/marvelrivalsgameview.baml** : marvel rivals settings

**menu/views/main/games/overwatchgameview.baml** : overwatch settings

**menu/views/main/games/pubggameview.baml** : pubg settings

**menu/views/main/games/rainbowsixgameview.baml** : r6 settings

**menu/views/main/games/robloxgameview.baml** : roblox settings

**menu/views/main/games/rustgameview.baml** : rust settings

**menu/views/main/games/splitgate2gameview.baml** : splitgate 2 settings

**menu/views/main/games/stalcraftxgameview.baml** : stalcraft x settings

**menu/views/main/games/strinovagameview.baml** : strinova settings

**menu/views/main/games/thefinalsgameview.baml** : the finals settings

**menu/views/main/games/universalgameview.baml** : works for any game

**menu/views/main/games/valorantgameview.baml** : valorant settings

**menu/views/main/mainview.baml** : main view container

**menu/views/main/preview/featurepreview.baml** : feature preview

**menu/views/main/preview/sidepanel.baml** : side panel

**menu/views/setup/compatibilitycheckview.baml** : compat check in setup

**menu/views/setup/gameselection.baml** : pick ur game in setup

**menu/views/setup/onepc/lookingforgame.baml** : scanning for the game

**menu/views/setup/onepc/onepcsetupview.baml** : one pc setup

**menu/views/setup/onepc/processselectionview.baml** : pick the game process

**menu/views/setup/setupkindselection.baml** : one pc or two pc choice

**menu/views/setup/twopc/calibrationdialog.baml** : calibration popup

**menu/views/setup/twopc/capturecarddeviceselection.baml** : pick capture card

**menu/views/setup/twopc/capturecardpreview.baml** : capture card preview

**menu/views/setup/twopc/ndipreview.baml** : ndi preview

**menu/views/setup/twopc/ndisourceselection.baml** : pick ndi source

**menu/views/setup/twopc/twopccapturemethodselection.baml** : pick capture method

**menu/views/setup/twopc/twopcsetupview.baml** : two pc setup

**resources/avalon_big.png** : big logo

**resources/logo.png** : logo

**resources/flags/cn.svg** : chinese flag

**resources/flags/es.svg** : spanish flag

**resources/flags/fi.svg** : finnish flag

**resources/flags/kr.svg** : korean flag

**resources/flags/ru.svg** : russian flag

**resources/flags/tr.svg** : turkish flag

**resources/flags/us.svg** : us flag

**themes/base/allicons.baml** : all the icons

**themes/base/brushes.baml** : brushes

**themes/base/colors.baml** : colors

**themes/base/converters.baml** : converters

**themes/base/fonts.baml** : fonts

**themes/base/sizes.baml** : sizes

**themes/controls/buttonstyles.baml** : button styles

**themes/controls/checkboxstyles.baml** : checkbox styles

**themes/controls/colorpickerstyles.baml** : color picker styles

**themes/controls/colortogglestyles.baml** : color toggle styles

**themes/controls/comboboxstyles.baml** : combobox styles

**themes/controls/configcardstyles.baml** : config card styles

**themes/controls/contextmenustyles.baml** : context menu styles

**themes/controls/featurecardstyles.baml** : feature card styles

**themes/controls/filepickerstyles.baml** : file picker styles

**themes/controls/geartogglestyles.baml** : gear toggle styles

**themes/controls/keybindpickerstyles.baml** : keybind picker styles

**themes/controls/labeledsliderstyles.baml** : labeled slider styles

**themes/controls/lightraystyles.baml** : light ray styles

**themes/controls/listboxstyles.baml** : listbox styles

**themes/controls/loadingspinnerstyles.baml** : spinner styles

**themes/controls/miscstyles.baml** : misc styles

**themes/controls/modalstyles.baml** : modal styles

**themes/controls/rangesliderstyles.baml** : range slider styles

**themes/controls/scrollbarstyles.baml** : scrollbar styles

**themes/controls/searchboxstyles.baml** : search box styles

**themes/controls/sidepanelstyles.baml** : side panel styles

**themes/controls/sliderstyles.baml** : slider styles

**themes/controls/statcardstyles.baml** : stat card styles

**themes/controls/textboxstyles.baml** : textbox styles

**themes/controls/togglegroupstyles.baml** : toggle group styles

**themes/controls/viewtabstyles.baml** : view tab styles

**themes/generic.baml** : root theme file

**zx_4e23ae116b914ed3038933b7f1ed5f0e.csproj** : junk project file the decompiler spat out
