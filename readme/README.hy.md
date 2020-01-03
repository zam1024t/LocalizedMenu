# LocalizedMenu
Տեղայնացման գործիք և տեղայնացված ընտրացուցակ Sublime Text 2/3 վերջնական օգտվողի համար

- Տրամադրված է նոր լեզուներ ավելացնելու հեշտ եղանակ
- Մի քանի տարբերակների/հարթակների օժանդակում
- Ընդհանուր ընտրացուցակների օժանդակում
- Տեղային ընտրացուցակների ինքնաշխատ պահուստավորում
- Անգլերեն նոր ընտրացուցակների ինքնաշխատ ապափաթեթավորում

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

# Այս նախագիծը նաև ներկայացված է այստեղ՝
- [GitHub](https://github.com/zam1024t/LocalizedMenu)
- [OSC开源中国](https://git.oschina.net/zam1024t/LocalizedMenu)
- [Coding.net](https://coding.net/u/zam1024t/p/LocalizedMenu/git)

# Էկրանահաններ
#### Աշխատանքը Windows-ում
![Work on Windows](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_win.gif)
#### Աշխատանքը OS X-ում
![Work on OS X](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_osx.gif)
#### Աշխատանքը Ubuntu-ում
![Work on Ubuntu](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_linux.gif)

# Տեղադրում
- Package Control-ը օգտագործելու միջոցով
	- տեղադրել [Package Control](https://packagecontrol.io/installation)
	- սեղմել `ctrl + shift + p`, մուտքագրել `install package`, սեղմել Enter և որոնել `LocalizedMenu`, սեղմել Enter
- Ձեռքով
	- ներբեռնել [master.zip](https://github.com/zam1024t/LocalizedMenu/archive/master.zip)，ապափաթեթավորել `Data\Packages` պանակի մեջ，հետո անվանափոխել `LocalizedMenu-master`-ը `LocalizedMenu`-ի
	- git clone to `Packages`
	```
	git clone https://github.com/zam1024t/LocalizedMenu
	```

# Օգտագործում
- Փոխարկումը ընտրացուցակի միջոցով
	- մտնել `Preference` -> `Languages` և ընտրել ցանկացած լեզուն
- Փոխարկումը հրահանգների վահանակի միջոցով
	- սեղմել `Ctrl+Shift+P`, մուտքագրել `lmxx` (*xx*-ը տեղայնացման կոդն է) փոխարկելու համար

# Լեզու ավելացնելը
- պատճենել `locale/en/en.json`-ը `locale/<locale>/<locale>.json`-ի մեջ, թարգմանել նոր լեզվի
- պատճենել `menu/<version>/en/*`-ը `menu/<version>/<locale>/*`-ի մեջ, թարգմանել նոր լեզվի
- Օրինակ Sublime Text Build 3999-ի համար `my` անվանումով նոր տեղայնացում ավելացնելու համար պետք է՝
	- մտնել `LocalizedMenu`-ի պանակի մեջ՝ ընտրելով `Preference` -> `Languages` -> `Add a language`
	- մտնել `locale` պանակը, ստեղծել `my` անվանումով պանակ և պատճենել նրա մեջ `en`-ի պարունակությունը
	- մտնել `my` պանակը և անվանափոխել `en.json`-ը `my.json`-ի, խմբագրել այսպես՝

	```JavaScript
	{
		"link": "",
		"hidden": false,
		"caption": "MyLanguage",
		"mnemonic": "m"
	}
	```

	- մտնել `menu/3999`,`my` անվանումով պանակ ստեղծել և պատճենել `en`-ի պարունակությունը նրա մեջ
	- թարգմանել բոլոր `caption`-ները ընտրացուցակի նիշքերում
	- հայտնաբերել լեզուն ընտրելով `Preference` -> `Languages` -> `Detect`, հետո ընտրացուցակում ընտրել այն `MyLanguage (my)`

	> **locale configs**<br>
	> link： նպատակային կապված տեղայնացում<br>
	> hidden： ընտրացուցակում թաքցնել միավորը<br>
	> caption： լեզվի անվանումը, տեղայնացման կոդը ինքնաշխատորեն կավելացվի<br>
	> mnemonic： ստեղների զուգակցում，անպայման չէ，համոզվեք, որ խորագիրը պարունակում է այն，տառաշարազգայուն է

# Լեզուն առաջարկելը
- տեղայնացման լեզուն պետք է անվանված լինի `<languageCode>` կամ `<languageCode>_<countryCode>`
	- `<languageCode>` ստորին տառաշար, `<countryCode>` վերին տառաշար, (անտեսեք սա, եթե աշխատում եք տեղային համակարգչի վրա)
	- Լեզու՝ http://www.wikipedia.org/wiki/ISO_639-1
	- Երկիր՝ http://www.wikipedia.org/wiki/ISO_3166-1
- Ստեղծել շտեմարանի ճյուղավորում (fork)
- Ստեղծել pull request-ի հարցում

# Տեղայնացումներ և աջակցողներ
- es_ES Español *by [Dastillero](https://github.com/dap39)*
- fr_FR Français *by [fxbenard](https://github.com/fxbenard)*
- hy Հայերեն *by [Arman High Foundation](https://github.com/ArmanHigh)*
- pt Português do Brasil *by [JNylson](https://github.com/jnylson)*
- ru Русский *by [Dimox](http://dimox.name) & [Ant0sh](https://github.com/Ant0sh)*
- sv_SE Svenska *by [H2SO4JB](https://github.com/H2SO4JB)*
- zh_CN 简体中文 *by [Zam](https://github.com/zam1024t)*
- zh_TW 繁体中文 *by [Zam](https://github.com/zam1024t)*

# Կապված քննարկումներ
- https://github.com/wbond/package_control_channel/pull/5665
- https://github.com/rexdf/ChineseLocalization/issues/10

# Թույլատրագիր
[MIT թույլատրագիր](ԹՈՒՅԼԱՏՐԱԳԻՐ)
