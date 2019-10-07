# LocalizedMenu
Інструмент локалізації та локалізоване меню для Sublime Text 2/3  Для кінцевого користувача

- Забезпечено простий механізм додавання нових мов
- Підтримка декількох версій/платформ
- Підтримка загальних меню
- Автоматичне резервне копіювання локальної версії меню
- Автоматичне розгортання нових англійських меню

# README.md
- en [English](../README.md)
- es_ES [Español](README.es_ES.md)
- hy [Հայերեն](README.hy.md)
- ru [Русский](README.ru.md)
- sv_SE [Svenska](README.sv_SE.md)
- uk_UA [Українська](README.uk_UA.md)
- zh_CN [简体中文](README.zh_CN.md)
- zh_TW [繁体中文](README.zh_TW.md)

# Цей проект також розміщено на:
- [GitHub](https://github.com/zam1024t/LocalizedMenu)
- [OSC开源中国](https://git.oschina.net/zam1024t/LocalizedMenu)
- [Coding.net](https://coding.net/u/zam1024t/p/LocalizedMenu/git)

# Знімки екрану:
#### Робота у Windows
! [Робота у Windows](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_win.gif)
#### Робота в macOS
! [Робота в macOS](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_osx.gif)
#### Рoбота в Ubuntu
! [Рoбота в Ubuntu](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_linux.gif)

# Встановлення
- За допомогою інструмента керування пакетами Package Control
	- встановіть [Package Control](https://packagecontrol.io/installation)
	- потім `ctrl + shift + p` вводимо `install package` Enter та пошук `LocalizedMenu` Enter
- Руками
	- завантажте [master.zip](https://github.com/zam1024t/LocalizedMenu/archive/master.zip), розархівуйте в теку `Data\Packages`, потім переіменуйте ` LocalizedMenu-master` в `LocalizedMenu`
	- git clone to `Packages`
	```
	git clone https://github.com/zam1024t/LocalizedMenu
	```

# Використання
- Перемикання мови через меню
	- в меню виберіть `Preference` -> `Languages` -> `Українська`
- Перемикання мови в командній панелі
	- `Ctrl + Shift + P`, введіть `lmxx` (*xx* - код локалі) для перемикання

# Додати мову
- скопіюйте `locale/en/en.json` у `locale/<locale>/<locale>.json`, перекладіть на Вашу мову
- скопіюйте `menu/<version>/en/*` у `menu/<version>/<locale>/*`, перекладіть на Вашу мову
- Наприклад, додамо локалізацію з іменем `my` для Sublime Text Build 3126
	- відкрийте `LocalizedMenu`, через `Preference` -> `Languages` -> `Add a language`
	- відкрийте теку `locale`, створіть теку `my` скопіюйте в неї вміст каталогу `en`
	- відкрийте отриманий каталог `my`, переіменуйте `en.json` в `my.json`, відредагуйте файл так:

	```JavaScript
	{
		"link": "",
		"hidden": false,
		"caption": "MyLanguage",
		"mnemonic": "m"
	}
	```

	- відкрийте теку `menu/3126`, створіть каталог `my` скопіюйте в неї вміст директорії `en`
	- перекладіть всі `caption` в файлах меню на свою мову
	- додайте мову через `Preference` -> `Languages` -> `Detect`, а потім виберіть `MyLanguage (my)`

	> ** locale configs **<br>
	> link：: цільова пов'язана локаль<br>
	> hidden：: приховати пункт в меню<br>
	> caption：: назва мови, код локалі додається автоматично<br>
	> mnemonic：: гаряча клавіша, не обов'язково, переконайтеся, що заголовок містить її, чутливий до регістру
# Надіслати переклад
- ім'я локалі повинно мати назву `<languageCode>` або `<languageCode>_<countryCode>`
	- `<languageCode>` маленькі літери, `<countryCode>` великі літери, (можна ігнорувати, якщо працюєте на локальному комп'ютері)
	- Мова: http://www.wikipedia.org/wiki/ISO_639-1
	- Країна: http://www.wikipedia.org/wiki/ISO_3166-1
- Створити форк (fork)
- Створити запит на pull request

# Перекладачі та  учасники
- es_ES Español *by [Dastillero](https://github.com/dap39)*
- hy Հայերեն *by [Arman High Foundation](https://github.com/ArmanHigh)*
- ru Русский *by [Dimox](http://dimox.name) & [Ant0sh](https://github.com/Ant0sh)*
- sv_SE Svenska *by [H2SO4JB](https://github.com/H2SO4JB)*
- uk_UA Українська *by [Andrii Kondratiev](https://github.com/keedhost)*
- zh_CN 简体中文 *by [Zam](https://github.com/zam1024t)*
- zh_TW 繁体中文 *by [Zam](https://github.com/zam1024t)*

# Пов'язані обговорення
- https://github.com/wbond/package_control_channel/pull/5665
- https://github.com/rexdf/ChineseLocalization/issues/10

# Ліцензія
[MIT ліцензія](ЛІЦЕНЗІЯ)
