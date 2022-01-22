# LocalizedMenu
Outil de localisation et menu localisé pour l'utilisateur final de Sublime Text 2/3/4

- Fournit un moyen facile d’ajouter de nouvelles langues
- Support de plusieurs versions/plateformes
 -Support des menus communs
- Sauvegarde automatique des menus traduits
- Décompactage automatique des nouveaux menus en anglais

# README.md
- de_DE [Deutsch](readme/README.de_DE.md)
- en [English](../README.md)
- es_ES [Español](README.es_ES.md)
- fr_FR [Français](README.fr_FR.md)
- hy [Հայերեն](README.hy.md)
- pt_BR [Português do Brasil](README.pt_BR.md)
- ru [Русский](README.ru.md)
- sv_SE [Svenska](README.sv_SE.md)
- zh_CN [简体中文](README.zh_CN.md)
- zh_TW [繁体中文](README.zh_TW.md)

# Ce projet est aussi hébergé sur
- [GitHub](https://github.com/zam1024t/LocalizedMenu)
- [Gitee](https://gitee.com/zam1024t/LocalizedMenu)

# Captures
#### Fonctionne sur Windows
![Work on Windows](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_win.gif)
#### Fonctionne sur OS X
![Work on OS X](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_osx.gif)
#### Fonctionne sur Ubuntu
![Work on Ubuntu](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_linux.gif)

# Installation
- Avec le Package Control
	- Installez [Package Control](https://packagecontrol.io/installation)
	- Cherchez `LocalizedMenu`
- Manuellement
	- Téléchargez [master.zip](https://github.com/zam1024t/LocalizedMenu/archive/master.zip), unzippez dans `Packages`, puis renommez-le de `LocalizedMenu-master` en `LocalizedMenu`
	- git clone dans `Packages`
	```
	git clone https://github.com/zam1024t/LocalizedMenu
	```

# Utilisation
- Depuis le menu
	- via `Preferences` -> `Languages`
- Depuis le panneau de contrôle
	- `Ctrl+Shift+P`, tapez `lmxx`(*xx* est le code de la locale) à utiliser

# Ajout d’une langue
- Copiez `locale/en/en.json` dans `locale/<locale>/<locale>.json`, traduisez dans votre langue
- Copiez `menu/<version>/en/*` dans `menu/<version>/<locale>/*`, traduisez dans votre langue
- Par exemple, now add locale named `vl` pour Sublime Text Build 3999
	- Ouvrez `LocalizedMenu` dir, via `Preference` -> `Languages` -> `Add a language`
	- Dans `locale`, copiez `en` en `vl`
	- Dans `vl`, renommez `en.json` en `vl.json`, modifiez ainsi :

	```JavaScript
	{
		"link": "",
		"hidden": false,
		"caption": "VotreLocale",
		"mnemonic": "m"
	}
	```

	- Allez dans `menu/3999`, copiez `en` en `vl`, et traduisez tous les `caption` présents dans le fichier
	- Detectez la langue dans `Preference` -> `Languages` -> `Detect`, puis affichez `VotreLocale (vl)`

	> **locale configs**<br>
	> link: the target locale linked to<br>
	> hidden: hide menu item<br>
	> caption: language name, locale code will auto add extraly<br>
	> mnemonic: hotkey, optional, make sure caption contain it, Case sensitive

# Proposer une langue
- Le nom de la langue doit être : `<languageCode>` ou `<languageCode>_<countryCode>`
	- `<languageCode>` en minuscule, `<countryCode>` en majuscule
	- Langue : https://www.wikipedia.org/wiki/ISO_639-1
	- Pays : https://www.wikipedia.org/wiki/ISO_3166-1
- Forkez le repo
- Faîtes une pull request

# Proposer des améliorations/corrections au français
- Forkez le repo [GitHub](https://github.com/fxbenard/LocalizedMenu)
- Faîtes votre pull request

# Locales & Contributors
- de_DE Deutsch *by [Standarduser](https://github.com/Standarduser)*
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
