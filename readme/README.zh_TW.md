# LocalizedMenu
LocalizedMenu(Localize Tool & Localized Menu)是一個為[Sublime Text 2/3/4](https://www.sublimetext.com)終端用戶(非git用戶/非開發者)設計，用來做菜單多語言化(漢化)的簡單易用工具，包含各種語言菜單。

- 提供了一個簡單快捷添加多語言的途徑
- 支持多種語言/多個版本/多個平臺同時使用
- 支持公共菜單共用
- 支持首次使用自動備份本地菜單
- 支持自動生成新版本的英文菜單

# README.md同時有以下語言的版本
- en [English](../README.md)
- es_ES [Español](README.es_ES.md)
- fr_FR [Français](README.fr_FR.md)
- hy [Հայերեն](README.hy.md)
- pt_BR [Português do Brasil](README.pt_BR.md)
- ru [Русский](README.ru.md)
- sv_SE [Svenska](README.sv_SE.md)
- zh_CN [简体中文](README.zh_CN.md)
- zh_TW [繁体中文](README.zh_TW.md)

# 本項目同時托管在
- [GitHub](https://github.com/zam1024t/LocalizedMenu)
- [Gitee](https://gitee.com/zam1024t/LocalizedMenu)

*主要是為了方便中國大陸的用戶，GitHub有時訪問會慢。*

# 使用截圖
#### 在Windows中使用
![在Windows中使用](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_win.gif)
#### 在OS X中使用
![在OS X中使用](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_osx.gif)
#### 在Ubuntu(Linux)中使用
![在Ubuntu(Linux)中使用](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_linux.gif)

# 安裝方法
- 通過Package Control安裝
	- 首先要先安裝[Package Control](https://packagecontrol.io/installation)
	- 搜索`LocalizedMenu`並安裝
- 手動下載安裝(以下任選一)
	- 下載[master.zip](https://github.com/zam1024t/LocalizedMenu/archive/master.zip)安裝包，解壓到`Packages`目錄中，然後將`LocalizedMenu-master`命名為`LocalizedMenu`
	- 使用git克隆到`Packages`目錄中
	```
	git clone https://github.com/zam1024t/LocalizedMenu
	```

# 使用方法
- 選擇菜單切換語言
	- 依次展開菜單`Preference` -> `Languages`
- 通過命令面板切換語言
	- 用`Ctrl+Shift+P`打開命令面板，輸入`lmxx`(*xx*為語言代碼)選擇切換語言

# <a name="add-a-language"></a>怎樣添加翻譯語言
- 打開`LocalizedMenu`插件目錄`Preference` -> `Languages` -> `Add a language`
- 復制`locale/en/en.json`到`locale/<locale>/<locale>.json`, 修改成對應的翻譯
- 復制`menu/<version>/en/*`到`menu/<version>/<locale>/*`, 修改成對應的翻譯
- 舉個例子，現在為Sublime Text Build 3999添加一個語言代碼為`my`的漢化菜單
	- 打開`LocalizedMenu`插件目錄`Preference` -> `Languages` -> `Add a language`
	- 進入`locale`目錄, 復制`en`目錄並命名為`my`
	- 進入`my`目錄把`en.json`改名為`my.json`, 並修改為

	```JavaScript
	{
		"link": "",
		"hidden": false,
		"caption": "本帥專用翻譯",
		"mnemonic": "m"
	}
	```

	- 進入目錄`menu/3999`, 復制`en`目錄並命名為`my`, 並將各菜單文件中的`caption`項漢化，如果有，記得後面附加上熱鍵`(<字母>)`。
	- 發現新添加的語言`Preference` -> `Languages` -> `Detect`,然後語言菜單中就有剛添加的`本帥專用翻譯 (my)`的菜單項了。

	> **locale配置項說明**<br>
	> link： 要鏈接到的語言代碼<br>
	> hidden： 是否隱藏菜單項<br>
	> caption： 語言名，語言代碼會在菜單中加括號自動帶上<br>
	> mnemonic： 熱鍵，可選，請確保caption有這個字母，區分大小寫

# <a name="submit-a-language"></a>怎樣提交翻譯語言
- 語言代碼的命名必須是這樣的：`<languageCode>`或`<languageCode>_<countryCode>`
	- `<languageCode>`要小寫, `<countryCode>`要大寫(當然你若在本地使用，命名請隨意！)
	- 各語言的ISO標準代碼: http://www.wikipedia.org/wiki/ISO_639-1
	- 各國家的ISO標準代碼: http://www.wikipedia.org/wiki/ISO_3166-1
- Fork本項目到你的庫中
- 添加的語言翻譯後提交pull request

# 語言及貢獻者
- es_ES Español *by [Dastillero](https://github.com/dap39)*
- fr_FR Français *by [fxbenard](https://github.com/fxbenard)*
- hy Հայերեն *by [Arman High Foundation](https://github.com/ArmanHigh)*
- pt Português do Brasil *by [JNylson](https://github.com/jnylson)*
- ru Русский *by [Dimox](http://dimox.name) & [Ant0sh](https://github.com/Ant0sh)*
- sv_SE Svenska *by [H2SO4JB](https://github.com/H2SO4JB)*
- zh_CN 简体中文 *by [Zam](https://github.com/zam1024t)*
- zh_TW 繁体中文 *by [Zam](https://github.com/zam1024t)*

# 問題反饋
- [GitHub issues](https://github.com/zam1024t/LocalizedMenu/issues)
- [zam1024t@gmail.com](mailto:zam1024t@gmail.com)

# 常見問題(FAQ)
- 問：安裝插件後不小心把原始的en翻譯給改亂或改錯了怎麽辦？<br>
  答：卸載本插件後重新安裝即可。

# 項目關聯討論
- https://github.com/wbond/package_control_channel/pull/5665
- https://github.com/rexdf/ChineseLocalization/issues/10

# 開源許可協議
[The MIT License](LICENSE)
