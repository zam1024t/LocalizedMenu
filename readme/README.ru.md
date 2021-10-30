# LocalizedMenu
Инструмент локализации и локализованное меню для Sublime Text 2/3/4  Для конечного пользователя

- Обеспечен простой способ добавления новых языков
- Поддержка нескольких версий/платформ
- Поддержка общих меню
- Автоматическое резервное копирование локальной версии меню
- Автоматическая распаковка новых английских меню

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

# Этот проект также размещен на
- [GitHub](https://github.com/zam1024t/LocalizedMenu)
- [Gitee](https://gitee.com/zam1024t/LocalizedMenu)

# Скриншоты
#### Работа в Windows
! [Работа в Windows](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_win.gif)
#### Работа в OS X
! [Работа в OS X](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_osx.gif)
#### Работа в Ubuntu
! [Работа в Ubuntu](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_linux.gif)

# Установка
- При помощи инструмента управления пакетами Package Control
	- установите [Package Control](https://packagecontrol.io/installation)
	- затем `ctrl + shift + p` вводим `install package` ввод и поиск `LocalizedMenu` ввод
- Вручную
	- скачать [master.zip](https://github.com/zam1024t/LocalizedMenu/archive/master.zip), распакуйте в папку `Data\Packages`, затем переименуйте` LocalizedMenu-master` в `LocalizedMenu`
	- git clone to `Packages`
	```
	git clone https://github.com/zam1024t/LocalizedMenu
	```

# Использование
- Переключение через меню
	- в меню выбрать `Preference` -> `Languages` -> `Русский`
- Переключение в командной панели
	- `Ctrl + Shift + P`, type`lmxx` (*xx* - код локали) для переключения

# Добавить язык
- скопировать `locale/en/en.json` в `locale/<locale>/<locale>.json`, перевести на ваш язык
- скопировать `menu/<version>/en/*` в `menu/<version>/<locale>/*`, перевести на ваш язык
- Например, добавим локализацию с именем `my` для Sublime Text Build 3126
	- откройте `LocalizedMenu`, через `Preference` -> `Languages` -> `Add a language`
	- откройте каталог `locale`, создайте каталог `my` скопируйте в него содержимое каталога `en`
	- откройте полученный каталог `my`, переименуйте `en.json` в `my.json`, отредактируйте так:

	```JavaScript
	{
		"link": "",
		"hidden": false,
		"caption": "MyLanguage",
		"mnemonic": "m"
	}
	```

	- откройте каталог `menu/3126`, создайте каталог `my` скопируйте в него содержимое каталога `en`
	- переведите все `caption` в файлах меню на свой язык
	- Подцепите язык через `Preference` -> `Languages` -> `Detect` и затем в меню выберите его `MyLanguage (my)`

	> ** locale configs **<br>
	> link：: целевая связанная локаль<br>
	> hidden：: скрыть пункт в меню<br>
	> caption：: имя языка, код локали добавится автоматически<br>
	> mnemonic：: горячая клавиша, необязательно, убедитесь, что заголовок содержит ее, чувствительный к регистру

# Отправить язык
- имя локали должно быть названо `<languageCode>` или `<languageCode>_<countryCode>`
	- `<languageCode>` строчные буквы, `<countryCode>` прописные буквы, (игнорируйте это, если работаете на локальном компьютере)
	- Язык: http://www.wikipedia.org/wiki/ISO_639-1
	- Страна: http://www.wikipedia.org/wiki/ISO_3166-1
- Создать ответвление репозитория (fork)
- Сделать запрос на pull request

# Переводчики & Участники
- es_ES Español *by [Dastillero](https://github.com/dap39)*
- hy Հայերեն *by [Arman High Foundation](https://github.com/ArmanHigh)*
- ru Русский *by [Dimox](http://dimox.name) & [Ant0sh](https://github.com/Ant0sh)*
- sv_SE Svenska *by [H2SO4JB](https://github.com/H2SO4JB)*
- zh_CN 简体中文 *by [Zam](https://github.com/zam1024t)*
- zh_TW 繁体中文 *by [Zam](https://github.com/zam1024t)*

# Связанные обсуждения
- https://github.com/wbond/package_control_channel/pull/5665
- https://github.com/rexdf/ChineseLocalization/issues/10

# Лицензия
[MIT лицензия](ЛИЦЕНЗИЯ)
