# LocalizedMenu
Інструмент локалізації і локалізоване меню для Sublime Text 2/3 Для кінцевого користувача

- Забезпечено простий спосіб додавання нових мов
- Підтримка декількох версій/платформ
- Підтримка загальних меню
- Автоматичне резервне копіювання локальної версії меню
- Автоматична розпакування нових англійських меню

# README.md
- en [English](../README.md)
- es_ES [Español](README.es_ES.md)
- hy [Հայերեն](README.hy.md)
- ru [Русский](README.ru.md)
- uk_UA [Українська](README.uk_UA.md)
- sv_SE [Svenska](README.sv_SE.md)
- zh_CN [简体中文](README.zh_CN.md)
- zh_TW [繁体中文](README.zh_TW.md)

# Цей проект також розміщений на
- [GitHub](https://github.com/zam1024t/LocalizedMenu)
- [OSC开源中国](https://git.oschina.net/zam1024t/LocalizedMenu)
- [Coding.net](https://coding.net/u/zam1024t/p/LocalizedMenu/git)

# Скріншоти
#### Робота в Windows
! [Робота в Windows](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_win.gif)
#### Робота в OS X
! [Робота в OS X](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_osx.gif)
#### Робота в Ubuntu
! [Робота в Ubuntu](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_linux.gif)

# Установка
- За допомогою інструменту управління пакетамиPackage Control
	- установіть [Package Control](https://packagecontrol.io/installation)
	- потім `ctrl + shift + p` вводимо `install package` ENTER та пошук `LocalizedMenu` ENTER
- Вручну
	- завантажити [master.zip](https://github.com/zam1024t/LocalizedMenu/archive/master.zip), розпакуйте в папку `Data\Packages`, затем переименуйте` LocalizedMenu-master` в `LocalizedMenu`
	- git clone to `Packages`
	```
	git clone https://github.com/zam1024t/LocalizedMenu
	```

# Використання
- Перемикання через меню
	- в меню обрати `Preference` -> `Languages` -> `Українська`
- Перемикання в командній панелі
	- `Ctrl + Shift + P`, type`lmxx` (*xx* - код локали) для переключения

# Добавити мову
- скопіювати `locale/en/en.json` в `locale/<locale>/<locale>.json`, перевести на вашу мову
- скопіювати `menu/<version>/en/*` в `menu/<version>/<locale>/*`, перевести на вашу мову
- Наприклад, додамо локалізацію з ім'ям `my` для Sublime Text Build 3126
	- відкрийте `LocalizedMenu`, через `Preference` -> `Languages` -> `Add a language`
	- відкрийте каталог `locale`, створіть каталог `my` скопіюйте в нього вміст каталогу `en`
	- відкрийте jnhbvfybq каталог `my`, перейменуйте `en.json` в `my.json`, відредагуйте так:

	```JavaScript
	{
		"link": "",
		"hidden": false,
		"caption": "MyLanguage",
		"mnemonic": "m"
	}
	```

	- відкрийте каталог `menu/3126`, створіть каталог `my` скопіюйте в нього вміст каталогу `en`
	- переведіть всі `caption` в файлах меню на свою мову
	- Підцепіть мову через `Preference` -> `Languages` -> `Detect` і потім в меню оберіте його `MyLanguage (my)`

	> ** locale configs **<br>
	> link：: цільова пов'язана локаль<br>
	> hidden：: приховати пункт в меню<br>
	> caption：: ім'я мови, код локалі додасться автоматично<br>
	> mnemonic：: гаряча клавіша, необов'язково, переконайтеся, що заголовок містить її, чутливий до регістру

# Надіслати мову
- ім'я локалі повинно бути названо `<languageCode>` или `<languageCode>_<countryCode>`
	- `<languageCode>` малі літери, `<countryCode>` великі літери, (ігноруйте це, якщо працюєте на локальному комп'ютері)
	- Мова: http://www.wikipedia.org/wiki/ISO_639-1
	- Країна: http://www.wikipedia.org/wiki/ISO_3166-1
- Створити відгалуження сховища (fork)
- Зробити запит на pull request

# Переводчики & Участники
- es_ES Español *by [Dastillero](https://github.com/dap39)*
- hy Հայերեն *by [Arman High Foundation](https://github.com/ArmanHigh)*
- ru Русский *by [Dimox](http://dimox.name) & [Ant0sh](https://github.com/Ant0sh)*
- uk_UA Українська *by [Artur Custom] (https://github.com/programist-samouchka)*
- sv_SE Svenska *by [H2SO4JB](https://github.com/H2SO4JB)*
- zh_CN 简体中文 *by [Zam](https://github.com/zam1024t)*
- zh_TW 繁体中文 *by [Zam](https://github.com/zam1024t)*

# Пов'язані обговорення
- https://github.com/wbond/package_control_channel/pull/5665
- https://github.com/rexdf/ChineseLocalization/issues/10

# Ліцензія
[MIT ліцензія](ЛІЦЕНЗІЯ)
