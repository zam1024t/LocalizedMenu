# LocalizedMenu
Localize Tool & Localized Menu for Sublime Text 2/3 End User

- Provide a easy way to add new languages
- Support multiple version/platform
- Support share common menus
- Auto backup local menus
- Auto unpack new build english menus

# README.md
- en [English](README.md)
- es_ES [Español](readme/README.es_ES.md)
- fr_FR [Français](readme/README.fr_FR.md)
- hy [Հայերեն](readme/README.hy.md)
- pt_BR [Português do Brasil](readme/README.pt_BR.md)
- ru [Русский](readme/README.ru.md)
- sv_SE [Svenska](readme/README.sv_SE.md)
- zh_CN [简体中文](readme/README.zh_CN.md)
- zh_TW [繁体中文](readme/README.zh_TW.md)

# This project is also hosted at
- [GitHub](https://github.com/zam1024t/LocalizedMenu)
- [OSC开源中国](https://git.oschina.net/zam1024t/LocalizedMenu)
- [Coding.net](https://coding.net/u/zam1024t/p/LocalizedMenu/git)

# Shots
#### Work on Windows
![Work on Windows](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_win.gif)
#### Work on OS X
![Work on OS X](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_osx.gif)
#### Work on Ubuntu
![Work on Ubuntu](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_linux.gif)

# Installation
- With Package Control
	- install [Package Control](https://packagecontrol.io/installation)
	- search for `LocalizedMenu`
- Manually
	- donwload [master.zip](https://github.com/zam1024t/LocalizedMenu/archive/master.zip)，unpack to `Packages`，then rename `LocalizedMenu-master` to `LocalizedMenu`
	- git clone to `Packages`
	```
	git clone https://github.com/zam1024t/LocalizedMenu
	```

# Usage
- Toggle in menu
	- via `Preference` -> `Languages`
- Toggle in command panel
	- `Ctrl+Shift+P`, type`lmxx`(*xx* is the locale code) to toggle

# Add A Language
- copy `locale/en/en.json` to `locale/<locale>/<locale>.json`, localize to your language
- copy `menu/<version>/en/*` to `menu/<version>/<locale>/*`, localize to your language
- For example, now add locale named `my` for Sublime Text Build 3999
	- open `LocalizedMenu` dir, via `Preference` -> `Languages` -> `Add a language`
	- enter `locale`, copy `en` to `my`
	- enter `my`, rename `en.json` to `my.json`, edit as:

	```JavaScript
	{
		"link": "",
		"hidden": false,
		"caption": "MyLanguage",
		"mnemonic": "m"
	}
	```

	- enter`menu/3999`, copy `en` to `my`, and tranlate all `caption` in menu files
	- detect language via `Preference` -> `Languages` -> `Detect`, then `MyLanguage (my)` display

	> **locale configs**<br>
	> link： the target locale linked to<br>
	> hidden： hide menu item<br>
	> caption： language name，locale code will auto add extraly<br>
	> mnemonic： hotkey，optional，make sure caption contain it，Case sensitive

# Submit A Language
- locale name must be named as `<languageCode>` or `<languageCode>_<countryCode>`
	- `<languageCode>` lowercase, `<countryCode>` uppercase, (ignore this if work on local)
	- Language: https://www.wikipedia.org/wiki/ISO_639-1
	- Country: https://www.wikipedia.org/wiki/ISO_3166-1
- Fork repo
- Make pull request

# Locales & Contributors
- es_ES Español *by [Dastillero](https://github.com/dap39)*
- fr_FR Français *by [fxbenard](https://github.com/fxbenard)*
- hy Հայերեն *by [Arman High Foundation](https://github.com/ArmanHigh)*
- pt Português do Brasil *by [JNylson](https://github.com/jnylson)*
- ru Русский *by [Dimox](http://dimox.name) & [Ant0sh](https://github.com/Ant0sh)*
- sv_SE Svenska *by [H2SO4JB](https://github.com/H2SO4JB)*
- zh_CN 简体中文 *by [Zam](https://github.com/zam1024t)*
- zh_TW 繁体中文 *by [Zam](https://github.com/zam1024t)*

# Related discuss
- https://github.com/wbond/package_control_channel/pull/5665
- https://github.com/rexdf/ChineseLocalization/issues/10

# License
[The MIT License](LICENSE)
