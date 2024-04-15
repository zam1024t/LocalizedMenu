# LocalizedMenu
Lokalizációs eszköz és lokalizált menü a Sublime Text 2/3/4-hez

- Lehetővé teszi új nyelvek könnyű hozzáadását
- Több verziót és platformot is támogat
- Támogatja a közös menük megosztását
- Helyi menük automatikus visszaállítása
- Az újonnan készített angol menük automatikus kicsomagolása

# README.md
- de_DE [Deutsch](readme/README.de_DE.md)
- en [English](README.md)
- es_ES [Español](readme/README.es_ES.md)
- fr_FR [Français](readme/README.fr_FR.md)
- hu [Magyar](readme/README.hu.md)
- hy [Հայերեն](readme/README.hy.md)
- pt_BR [Português do Brasil](readme/README.pt_BR.md)
- ru [Русский](readme/README.ru.md)
- sv_SE [Svenska](readme/README.sv_SE.md)
- zh_CN [简体中文](readme/README.zh_CN.md)
- zh_TW [繁体中文](readme/README.zh_TW.md)

# Ez a projekt elérhető a következő helyeken is
- [GitHub](https://github.com/zam1024t/LocalizedMenu)
- [Gitee](https://gitee.com/zam1024t/LocalizedMenu)

# Képernyőképek
#### Windows
![Windows](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_win.gif)
#### OS X
![OS X](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_osx.gif)
#### Ubuntu
![Ubuntu](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_linux.gif)

# Telepítés
- Package Control használatával
	- telepítsd a [Package Control-t](https://packagecontrol.io/installation),
	- keress rá a `LocalizedMenu` kulcsszóra
- Manuálisan
	- töltsd le a [master.zip](https://github.com/zam1024t/LocalizedMenu/archive/master.zip) fájlt，csomagold ki a `Packages` alá，utána pedig nevezd át a `LocalizedMenu-master`-t `LocalizedMenu`-re,
	- klónozd a következő Git adattárat a `Packages`-be
	```
	git clone https://github.com/zam1024t/LocalizedMenu
	```

# Használat
- Váltás a menün keresztül
	- a `Preferences` -> `Languages` menüpontban
- Váltás a parancstáblán keresztül
	- `Ctrl+Shift+P`, írd be, hogy `lmxx` (ahol *xx* a nyelvkód)

# Nyelv hozzáadása
- Másold a `locale/en/en.json`-t a `locale/<nyelvkód>/<nyelvkód>.json` helyre, majd fordítsd le a saját nyelvedre.
- Másold a `menu/<verzió>/en/*` alatt levő fájlokat a `menu/<verzió>/<nyelvkód>/*` mappába, majd fordítsd le őket a saját nyelvedre.
- Például, a `my` nyelvkód Sublime Text Build 3999-hez való hozzáadásához:
	- nyisd meg a `LocalizedMenu` mappát a `Preferences` -> `Languages` -> `Add a language` menüponton keresztül,
	- lépj be a `locale` mappába, készíts egy `my` nevű másolatot az `en` mappáról,
	- lépj be a `my` mappába, nevezd át az `en.json`-t `my.json`-re, majd szerkeszd át így:

	```JavaScript
	{
		"link": "",
		"hidden": false,
		"caption": "MyLanguage",
		"mnemonic": "m"
	}
	```

	- lépj be a `menu/3999` mappába, készíts másolatot az `en` mappáról `my` néven, és fordíts le minden `caption` attribútumot a menü fájlokban,
	- használd a nyelv észlelését a `Preference` -> `Languages` -> `Detect` menüponttal, majd válaszd a `MyLanguage (my)` elemet.

	> **nyelvkód konfigurációk**<br>
	> link： a cél nyelvkód, amihez hozzá lesz rendelve<br>
	> hidden： menüelem elrejtése<br>
	> caption： nyelv neve. A nyelvkód automatikusan lesz hozzáadva.<br>
	> mnemonic： opcionális, kis-/nagybetűre érzékeny gyorsbillentyű. A caption-nek tartalmaznia kell ezt a betűt.

# Nyelv beküldése
- A nyelvkód neve a következő kell legyen: `<nyelvkód>` vagy `<nyelvkód>_<országkód>`:
	- A `<nyelvkód>` teljesen kisbetűs, az `<országkód>` teljesen nagybetűs (hagyd ezt figyelmen kívül, ha a saját gépeden dolgozol),
	- Nyelv: https://www.wikipedia.org/wiki/ISO_639-1
	- Ország: https://www.wikipedia.org/wiki/ISO_3166-1
- Készíts másolatot (fork) az adattárról.
- Készíts egy pull request-et.

# Elérhető nyelvek és fordítók
- de_DE Deutsch: *[Standarduser](https://github.com/Standarduser)*
- es Español: *[Christopher](https://t.me/Azriel_7589)*
- es_ES Español: *[Dastillero](https://github.com/dap39)*
- fr_FR Français: *[fxbenard](https://github.com/fxbenard)*
- hu Magyar: *[Tamás Balog](https://github.com/picimako)*
- hy Հայերեն: *[Arman High Foundation](https://github.com/ArmanHigh)*
- pt Português do Brasil: *[JNylson](https://github.com/jnylson)*
- ru Русский: *[Dimox](http://dimox.name) & [Ant0sh](https://github.com/Ant0sh) & [Maksim Arhipov](https://github.com/OSPanel)*
- sv_SE Svenska: *[H2SO4JB](https://github.com/H2SO4JB)*
- zh_CN 简体中文: *[Zam](https://github.com/zam1024t)*
- zh_TW 繁体中文: *[Zam](https://github.com/zam1024t)*

# Kapcsolódó diskurzus
- https://github.com/wbond/package_control_channel/pull/5665
- https://github.com/rexdf/ChineseLocalization/issues/10

# Licenc
[The MIT License](LICENSE)
