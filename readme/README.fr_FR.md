# LocalizedMenu
Localize Tool & Localized Menu for Sublime Text 2/3 End User

- Provide a easy way to add new languages
- Support multiple version/platform
- Support share common menus
- Auto backup local menus
- Auto unpack new build english menus

# README.md
- en [English](README.md)
- fr_FR [Français](readme/README.fr_FR.md)
- zh_CN [简体中文](readme/README.zh_CN.md)
- zh_TW [繁体中文](readme/README.zh_TW.md)

# Ce projet est aussi hébergé sur
- [GitHub](https://github.com/zam1024t/LocalizedMenu)
- [OSC开源中国](https://git.oschina.net/zam1024t/LocalizedMenu)
- [Coding.net](https://coding.net/u/zam1024t/p/LocalizedMenu/git)

# Captures
#### Fonctionne sur Windows
![Work on Windows](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_win.gif)
#### Fonctionne sur OS X
![Work on OS X](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_osx.gif)
#### Fonctionne sur Ubuntu
![Work on Ubuntu](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_linux.gif)

# Installation
- Avec le Package Control
	- installez [Package Control](https://packagecontrol.io/installation)
	- cherchez `LocalizedMenu`
- Manuellement
	- téléchargez [master.zip](https://github.com/zam1024t/LocalizedMenu/archive/master.zip)，unzippez dans `Packages`，puis renommez-le de `LocalizedMenu-master` en `LocalizedMenu`
	- git clone dans `Packages`
	```
	git clone https://github.com/zam1024t/LocalizedMenu
	```

# Utilisation
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

	- allez dans `menu/3999`, copiez `en` en `my`, et traduisez tous les `caption` présents dans le fichier
	- detectez la langue dans `Preference` -> `Languages` -> `Detect`, puis affichez `MyLanguage (my)`

	> **locale configs**<br>
	> link： the target locale linked to<br>
	> hidden： hide menu item<br>
	> caption： language name，locale code will auto add extraly<br>
	> mnemonic： hotkey，optional，make sure caption contain it，Case sensitive

# Proposer une langue
- locale name must be named as `<languageCode>` or `<languageCode>_<countryCode>`
	- `<languageCode>` lowercase, `<countryCode>` uppercase, (ignore this if work on local)
	- Langue: http://www.wikipedia.org/wiki/ISO_639-1
	- Pays: http://www.wikipedia.org/wiki/ISO_3166-1
- Forkez le repo
- Faites une pull request

# Locales & Contributors
- zh_CN 简体中文 *by [Zam](https://github.com/zam1024t)*
- zh_TW 繁体中文 *by [Zam](https://github.com/zam1024t)*
- fr_FR Français *by [fxbenard](https://github.com/zam1024t)*

# Related discuss
- https://github.com/wbond/package_control_channel/pull/5665
- https://github.com/rexdf/ChineseLocalization/issues/10

# License
[The MIT License](LICENSE)
