# LocalizedMenu
Herramienta de traducción & menú traducido para usuarios finales de Sublime Text 2/3

- Proporciona un modo sencillo para añadir nuevos idiomas
- Soporta múltiples versiones/plataformas
- Soporta menús comunes compartidos
- Backup automático de menús locales
- Desempaquetado automático de nuevas builds de los menús en inglés

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

# Este proyecto está también alojado en
- [GitHub](https://github.com/zam1024t/LocalizedMenu)
- [OSC开源中国](https://git.oschina.net/zam1024t/LocalizedMenu)
- [Coding.net](https://coding.net/u/zam1024t/p/LocalizedMenu/git)

# Capturas de pantalla
#### Funciona en Windows
![Funciona en Windows](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_win.gif)
#### Funciona en OS X
![Funciona en OS X](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_osx.gif)
#### Funciona en Ubuntu
![Funciona en Ubuntu](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_linux.gif)

# Instalación
- Con Package Control
	- instala [Package Control](https://packagecontrol.io/installation)
	- busca `LocalizedMenu`
- Manulamente
	- descarga [master.zip](https://github.com/zam1024t/LocalizedMenu/archive/master.zip)，unpack to `Packages`，then rename `LocalizedMenu-master` to `LocalizedMenu`
	- clonar con git en `Packages`
	```
	git clone https://github.com/zam1024t/LocalizedMenu
	```

# Uso
- Activar en menú
	- vía `Preferences` -> `Languages`
- Activar en panel de comandos
	- `Ctrl+Shift+P`, escribe`lmxx`(*xx* es el código de idioma) para activar

# Añadir un idioma
- copiar `locale/en/en.json` a `locale/<locale>/<locale>.json`, traduce a tu idioma
- copiar `menu/<version>/en/*` a `menu/<version>/<locale>/*`, traduce a tu idioma
- Por ejemplo, para añadir el idioma `my` para Sublime Text Build 3999
	- abre el directorio `LocalizedMenu`, vía `Preferences` -> `Languages` -> `Add a language`
	- introduce `locale`, copia `en` como `my`
	- introduce `my`, renombra `en.json` a `my.json`, edita como:

	```JavaScript
	{
		"link": "",
		"hidden": false,
		"caption": "MyLanguage",
		"mnemonic": "m"
	}
	```

	- introduce`menu/3999`, copia `en` como `my`, y traduce todas las entradas `caption` en los archivos de menú
	- detecta el idioma vía `Preferences` -> `Languages` -> `Detect`, aparecerá el idioma `MyLanguage (my)`

	> **configuraciones de idioma**<br>
	> link： el idioma al que enlazamos<br>
	> hidden： ocultar el ítem del menú<br>
	> caption： el nombre del idioma, el código se añadirá automáticamente<br>
	> mnemonic： atajo de teclado, opcional, asegurarse que está contenido en captio, es sensible a la capitalización

# Enviar un Idioma
- el idioma debe nombrarse como `<languageCode>` o `<languageCode>_<countryCode>`
	- `<languageCode>` minúsculas, `<countryCode>` mayúsculas, (ignorar si se trbaja en local)
	- Idioma: http://www.wikipedia.org/wiki/ISO_639-1
	- País: http://www.wikipedia.org/wiki/ISO_3166-1
- Crear fork del repo
- Enviar pull request

# Idiomas & Contribuyentes
- es_ES Español *by [Dastillero](https://github.com/dap39)*
- fr_FR Français *by [fxbenard](https://github.com/fxbenard)*
- hy Հայերեն *by [Arman High Foundation](https://github.com/ArmanHigh)*
- pt Português do Brasil *by [JNylson](https://github.com/jnylson)*
- ru Русский *by [Dimox](http://dimox.name) & [Ant0sh](https://github.com/Ant0sh)*
- sv_SE Svenska *by [H2SO4JB](https://github.com/H2SO4JB)*
- zh_CN 简体中文 *by [Zam](https://github.com/zam1024t)*
- zh_TW 繁体中文 *by [Zam](https://github.com/zam1024t)*

# Discusiones relacionadas
- https://github.com/wbond/package_control_channel/pull/5665
- https://github.com/rexdf/ChineseLocalization/issues/10

# Licencias
[The MIT License](LICENSE)
