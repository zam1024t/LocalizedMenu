# LocalizedMenu
Översättningsverktyg & Översättningsmeny för Sublime Text 2/3 slutanvändare

- Erbjuder ett enkelt sätt att lägga till nya språk
- Stödjer flera versioner/plattformar
- Stödjer delning av vanliga menyer
- Automatisk säkerhetskopiering av språkmenyer
- Automatisk uppackning av nybyggda engelska menyer

# README.md
- en [English](../README.md)
- es_ES [Español](README.es_ES.md)
- fr_FR [Français](README.fr_FR.md)
- hy [Հայերեն](README.hy.md)
- pt_BR [Português do Brasil](README.pt_BR.md)
- ru [Русский](README.ru.md)
- sv_SE [Svenska](README.sv_SE.md)
- zh_CN [简体中文](README.zh_CN.md)
- zh_TW [繁体中文](README.zh_TW.md)

# Detta projekt är också värd hos
- [GitHub](https://github.com/zam1024t/LocalizedMenu)
- [OSC开源中国](https://git.oschina.net/zam1024t/LocalizedMenu)
- [Coding.net](https://coding.net/u/zam1024t/p/LocalizedMenu/git)

# Skärmdumpar
#### Fungerar i Windows
![Work on Windows](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_win.gif)
#### Fungerar i OS X
![Work on OS X](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_osx.gif)
#### Fungerar i Ubuntu
![Work on Ubuntu](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_linux.gif)

# Installation
- Med Package Control
	- installera [Package Control](https://packagecontrol.io/installation)
	- sök efter `LocalizedMenu`
- Manuellt
	- ladda ned [master.zip](https://github.com/zam1024t/LocalizedMenu/archive/master.zip)，packa upp till `Packages`，byt sedan namn på `LocalizedMenu-master` till `LocalizedMenu`
	- git clone till `Packages`
	```
	git clone https://github.com/zam1024t/LocalizedMenu
	```

# Användning
- Växla i meny
	- via `Inställningar` -> `Språk`
- Växla i kommandopanelen
	- `Ctrl+Shift+P`, skriv`lmxx`(*xx* är den lokala koden) för att växla

# Lägg till ett språk
- kopiera `locale/en/en.json` till `locale/<locale>/<locale>.json`, översätt till ditt språk
- kopiera `menu/<version>/en/*` till `menu/<version>/<locale>/*`, översätt till ditt språk
- Till exempel, lägg nu till språknamnet `my` för Sublime Text Build 3999
	- öppna mappen `LocalizedMenu`, via `Inställningar` -> `Språk` -> `Lägg till ett språk`
	- gå in i `locale`, kopiera `en` till `my`
	- gå in i `my`, byt namn på `en.json` till `my.json`, redigera som:

	```JavaScript
	{
		"link": "",
		"hidden": false,
		"caption": "MittSpråk",
		"mnemonic": "m"
	}
	```

	- gå in i `menu/3999`, kopiera `en` till `my`, och översätt alla `caption` i menyfilerna
	- upptäck språk via `Inställningar` -> `Språk` -> `Upptäck`, sedan visas `MittSpråk (my)`

	> **språkkonfigurationer**<br>
	> link： målet som språket länkas till<br>
	> hidden： dölj menyobjekt<br>
	> caption： språkets namn，landskoden läggs till automatiskt<br>
	> mnemonic： kortkommando，frivillig，se till att caption innehåller det，Skiftlägeskänslig

# Skicka in ett språk
- språkets namn måste namnges som `<språkkod>` eller `<språkkod>_<LANDSKOD>`
	- `<språkkod>` gemener, `<LANDSKOD>` VERSALER, (ignorera detta om du arbetar lokalt)
	- Språk: http://www.wikipedia.org/wiki/ISO_639-1
	- Land: http://www.wikipedia.org/wiki/ISO_3166-1
- Gör en Fork repo
- Gör en Pull request

# Språk & Bidragsgivare
- es_ES Español *av [Dastillero](https://github.com/dap39)*
- fr_FR Français *av [fxbenard](https://github.com/fxbenard)*
- hy Հայերեն *av [Arman High Foundation](https://github.com/ArmanHigh)*
- pt Português do Brasil *av [JNylson](https://github.com/jnylson)*
- ru Русский *av [Dimox](http://dimox.name) & [Ant0sh](https://github.com/Ant0sh)*
- sv_SE Svenska *av [H2SO4JB](https://github.com/H2SO4JB)*
- zh_CN 简体中文 *av [Zam](https://github.com/zam1024t)*
- zh_TW 繁体中文 *av [Zam](https://github.com/zam1024t)*

# Relaterad diskussion
- https://github.com/wbond/package_control_channel/pull/5665
- https://github.com/rexdf/ChineseLocalization/issues/10

# Licens
[The MIT License](LICENSE)
