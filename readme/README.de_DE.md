# LocalizedMenu
Übersetzungswerkzeug & übersetztes Menü Sublime Text 2/3/4

- Bietet einen einfachen Weg, neue Sprachen hinzuzufügen
- Unterstützt verschiedene Versionen/Plattformen
- Unterstützt das Teilen von Menüs der Community
- Automatisches Backup von lokalen Menüs
- Automatisches Entpacken neu erstellter englischer Menüs

# README.md
- de_DE [Deutsch](readme/README.de_DE.md)
- en [English](README.md)
- es_ES [Español](readme/README.es_ES.md)
- fr_FR [Français](readme/README.fr_FR.md)
- hy [Հայերեն](readme/README.hy.md)
- pt_BR [Português do Brasil](readme/README.pt_BR.md)
- ru [Русский](readme/README.ru.md)
- sv_SE [Svenska](readme/README.sv_SE.md)
- zh_CN [简体中文](readme/README.zh_CN.md)
- zh_TW [繁体中文](readme/README.zh_TW.md)

# Dieses Projekt wird gehostet bei
- [GitHub](https://github.com/zam1024t/LocalizedMenu)
- [Gitee](https://gitee.com/zam1024t/LocalizedMenu)

# Screenshots
#### Funktion unter Windows
![Work on Windows](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_win.gif)
#### Funktion unter OS X
![Work on OS X](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_osx.gif)
#### Funktion unter Ubuntu
![Work on Ubuntu](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_linux.gif)

# Installation
- Über Package Control:
	- Installiere [Package Control](https://packagecontrol.io/installation)
	- Suche nach `LocalizedMenu`
- Manuell:
	- Donwloade [master.zip](https://github.com/zam1024t/LocalizedMenu/archive/master.zip)，entpacke die ZIP-Datei in den Ordner `Packages`，benenne `LocalizedMenu-master` in `LocalizedMenu` um
	- git clone in den Ordner `Packages`
	```
	git clone https://github.com/zam1024t/LocalizedMenu
	```

# Verwendgung
- Sprache über das Menü umschalten:
	- `Preference` -> `Languages`
- Sprache über die Befehls-Palette umschalten:
	- `Ctrl+Shift+P`, tippe `lmxx`(*xx* = Sprache) ein, um die Sprache umzuschalten

# Sprache hinzufügen
- Kopiere `locale/en/en.json` nach `locale/<locale>/<locale>.json`, Datei übersetzen
- Kopiere `menu/<version>/en/*` nach `menu/<version>/<locale>/*`, Dateien übersetzen
- Beispiel: Die Sprache `my` soll für Sublime Text Build 3999 hinzugefügt werden:
	- Öffne den Ordner `LocalizedMenu` über `Preferences` -> `Languages` -> `Sprache hinzufügen...`
	- Öffne den Ordner `locale`, erstelle eine Kopie des Ordners `en` und benenne ihn `my`
	- Öffne den Ordner `my`, benenne die Datei `en.json` in `my.json` um und bearbeite sie wie folgt:

	```JavaScript
	{
		"link": "",
		"hidden": false,
		"caption": "MyLanguage",
		"mnemonic": "m"
	}
	```

	- Öffne den Ordner `menu/3999`, erstelle eine Kopie des Ordners `en` und benenne ihn `my`, übersetze alle `caption`-Felder in den Menü-Dateien
	- Sprache über das Menü `Preferences` -> `Languages` -> `Erkennen` automatisch hinzufügen lassen, `MyLanguage (my)` wird nun um Menü angezeigt

	> **Spracheinstellungen**<br>
	> link： Sprache, auf die verlinkt wird<br>
	> hidden： Menü-Element ausblenden<br>
	> caption： Name der Sprache<br>
	> mnemonic： Tastaturkürzel (optional)，stelle sicher, dass es in `caption` enthalten ist，(Groß-/Kleinschreibung beachten)

# Sprache übermitteln
- Sprache muss als `<languageCode>` oder `<languageCode>_<countryCode>` benannt sein
	- `<languageCode>` Kleinbuchstaben, `<countryCode>` Großbuchstaben, (kann ignoriert werden, wenn man nur lokal arbeitet)
	- Sprache `<languageCode>`: https://www.wikipedia.org/wiki/ISO_639-1
	- Land `<countryCode>`: https://www.wikipedia.org/wiki/ISO_3166-1
- Erstelle einen Fork des Repositorys
- Erstelle einen Pull request

# Sprachen & Mitwirkende
- de_DE Deutsch *by [Standarduser](https://github.com/Standarduser)*
- es_ES Español *by [Dastillero](https://github.com/dap39)*
- fr_FR Français *by [fxbenard](https://github.com/fxbenard)*
- hy Հայերեն *by [Arman High Foundation](https://github.com/ArmanHigh)*
- pt Português do Brasil *by [JNylson](https://github.com/jnylson)*
- ru Русский *by [Dimox](http://dimox.name) & [Ant0sh](https://github.com/Ant0sh)*
- sv_SE Svenska *by [H2SO4JB](https://github.com/H2SO4JB)*
- zh_CN 简体中文 *by [Zam](https://github.com/zam1024t)*
- zh_TW 繁体中文 *by [Zam](https://github.com/zam1024t)*

# Zugehörige Diskussionen
- https://github.com/wbond/package_control_channel/pull/5665
- https://github.com/rexdf/ChineseLocalization/issues/10

# Lizenz
[The MIT License](LICENSE)
