# LocalizedMenu
Uirlis Logánaithe & Roghchlár Logánaithe do Sublime Text 2/3/4 Úsáideoir Deiridh

- Bealach éasca a sholáthar chun teangacha nua a chur leis
- Tacaíocht a thabhairt do leaganacha/ardáin iolracha
- Tacaíocht a thabhairt do roinnt biachláir choiteanna
- Cúltaca uathoibríoch de bhiachláir áitiúla
- Biachláir nua-thógtha Béarla a dhíphacáil go huathoibríoch

# README.md
- de_DE [Deutsch](readme/README.de_DE.md)
- en [English](README.md)
- es_ES [Español](readme/README.es_ES.md)
- fr_FR [Français](readme/README.fr_FR.md)
- ga_IE [Gaeilge](readme/README.ga_IE.md)
- hu [Magyar](readme/README.hu.md)
- hy [Հայերեն](readme/README.hy.md)
- pt_BR [Português do Brasil](readme/README.pt_BR.md)
- ru [Русский](readme/README.ru.md)
- sv_SE [Svenska](readme/README.sv_SE.md)
- zh_CN [简体中文](readme/README.zh_CN.md)
- zh_TW [繁体中文](readme/README.zh_TW.md)

# Tá an tionscadal seo á óstáil freisin ag
- [GitHub](https://github.com/zam1024t/LocalizedMenu)
- [Gitee](https://gitee.com/zam1024t/LocalizedMenu)

# Seat scáileáin
#### Obair ar Windows
![Work on Windows](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_win.gif)
#### Obair ar OS X
![Work on OS X](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_osx.gif)
#### Obair ar Ubuntu
![Work on Ubuntu](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_linux.gif)

# Suiteáil
- Le Rialú Pacáiste
	- suiteáil [Package Control](https://packagecontrol.io/installation)
	- cuardach a dhéanamh ar `LocalizedMenu`
- De láimh
	- íoslódáil [master.zip](https://github.com/zam1024t/LocalizedMenu/archive/master.zip)，díphacáil chuig `Packages`，ansin athainmnigh `LocalizedMenu-master` go `LocalizedMenu`
	- git clone go `Packages`
	```
	git clone https://github.com/zam1024t/LocalizedMenu
	```

# Úsáid
- Scoránaigh sa roghchlár
	- trí `Preference` -> `Languages`
- Scoránaigh sa  command panel
	-`Ctrl+Shift+P`, clóscríobh`lmxx`(*xx* an cód logánta) chun athrú

# Cuir Teanga Leis
- cóipeáil `locale/en/en.json` go `locale/<locale>/<locale>.json`, logánú chuig do theanga
- cóipeáil `menu/<version>/en/*` go `menu/<version>/<locale>/*`, logánú chuig do theanga
- Mar shampla, cuir logán darb ainm `my` leis anois le haghaidh Sublime Text Build 3999.
	- oscailte `LocalizedMenu` eolaire, trí `Preference` -> `Languages` -> `Add a language`
	- cuir isteach `locale`, cóipeáil `en` go `my`
	- cuir isteach `my`, athainmnigh `en.json` go `my.json`, cuir in eagar mar:

	```JavaScript
	{
		"link": "",
		"hidden": false,
		"caption": "MoTheanga",
		"mnemonic": "m"
	}
	```

	- cuir isteach `menu/3999`, cóipeáil `en` go `my`, agus aistrigh gach `fotheideal` i gcomhaid an roghchláir
	- teanga a bhrath trí `Preference` -> `Languages` -> `Detect`, ansin taispeáint `MoTheanga (mo)`
	> **locale configs**<br>
		> nasc: an logán sprice atá nasctha leis<br>
		> i bhfolach: mír roghchláir a cheilt<br>
		> fotheideal: ainm na teanga, cuirfear cód logáin leis go huathoibríoch<br>
		> mnemonic: eochair the, roghnach, cinntigh go bhfuil sé sna fotheidil, íogair ó thaobh cás de

# Cuir Teanga Isteach
- ní mór ainm an logáin a bheith mar `<Cód teanga>` nó `<Cód teanga>_<Cód tíre>`
	- `<CódTeanga>` litreacha beaga, `<CódTíre>` litreacha móra, (neamhaird a dhéanamh de seo má oibríonn tú go háitiúil)
	- Teanga: https://www.wikipedia.org/wiki/ISO_639-1
	- Tír: https://www.wikipedia.org/wiki/ISO_3166-1
- Stóras forc
- Déan iarratas tarraingthe

# Logáin & Rannpháirtithe
- de_DE Deutsch *ag [Standarduser](https://github.com/Standarduser)*
- es Español *ag [Christopher](https://t.me/Azriel_7589)*
- es_ES Español *ag [Dastillero](https://github.com/dap39)*
- fr_FR Français *ag [fxbenard](https://github.com/fxbenard)*
- ga_IE Gaeilge *ag [Aindriú](https://github.com/aindriu80)*
- hu Magyar *ag [Tamás Balog](https://github.com/picimako)*
- hy Հայերեն *ag [Arman High Foundation](https://github.com/ArmanHigh)*
- pt Português do Brasil *ag [JNylson](https://github.com/jnylson)*
- ru Русский *ag [Dimox](http://dimox.name) & [Ant0sh](https://github.com/Ant0sh) & [Maksim Arhipov](https://github.com/OSPanel)*
- sv_SE Svenska *ag [H2SO4JB](https://github.com/H2SO4JB)*
- zh_CN 简体中文 *ag [Zam](https://github.com/zam1024t)*
- zh_TW 繁体中文 *ag [Zam](https://github.com/zam1024t)*

# Pléigh ghaolmhar
- https://github.com/wbond/package_control_channel/pull/5665
- https://github.com/rexdf/ChineseLocalization/issues/10

# Ceadúnas
[The MIT License](LICENSE)
