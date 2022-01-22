# LocalizedMenu
LocalizedMenu(Localize Tool & Localized Menu)是一个为[Sublime Text 2/3/4](https://www.sublimetext.com)终端用户(非git用户/非开发者)设计，用来做菜单多语言化(汉化)的简单易用工具，包含各种语言菜单。

- 提供了一个简单快捷添加多语言的途径
- 支持多种语言/多个版本/多个平台同时使用
- 支持公共菜单共用
- 支持首次使用自动备份本地菜单
- 支持自动生成新版本的英文菜单

# README.md同时有以下语言的版本
- de_DE [Deutsch](readme/README.de_DE.md)
- en [English](../README.md)
- es_ES [Español](README.es_ES.md)
- fr_FR [Français](README.fr_FR.md)
- hy [Հայերեն](README.hy.md)
- pt_BR [Português do Brasil](README.pt_BR.md)
- ru [Русский](README.ru.md)
- sv_SE [Svenska](README.sv_SE.md)
- zh_CN [简体中文](README.zh_CN.md)
- zh_TW [繁体中文](README.zh_TW.md)

# 本项目同时托管在
- [GitHub](https://github.com/zam1024t/LocalizedMenu)
- [Gitee](https://gitee.com/zam1024t/LocalizedMenu)

*主要是为了方便中国大陆的用户，GitHub有时访问会慢。*

# 使用截图
#### 在Windows中使用
![在Windows中使用](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_win.gif)
#### 在OS X中使用
![在OS X中使用](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_osx.gif)
#### 在Ubuntu(Linux)中使用
![在Ubuntu(Linux)中使用](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_linux.gif)

# 安装方法
- 通过Package Control安装
	- 首先要先安装[Package Control](https://packagecontrol.io/installation)
	- 搜索`LocalizedMenu`并安装
- 手动下载安装(以下任选一)
	- 下载[master.zip](https://github.com/zam1024t/LocalizedMenu/archive/master.zip)安装包，解压到`Packages`目录中，然后将`LocalizedMenu-master`命名为`LocalizedMenu`
	- 使用git克隆到`Packages`目录中
	```
	git clone https://github.com/zam1024t/LocalizedMenu
	```

# 使用方法
- 选择菜单切换语言
	- 依次展开菜单`Preference` -> `Languages`
- 通过命令面板切换语言
	- 用`Ctrl+Shift+P`打开命令面板，输入`lmxx`(*xx*为语言代码)选择切换语言

# <a name="add-a-language"></a>怎样添加翻译语言
- 打开`LocalizedMenu`插件目录`Preference` -> `Languages` -> `Add a language`
- 复制`locale/en/en.json`到`locale/<locale>/<locale>.json`, 修改成对应的翻译
- 复制`menu/<version>/en/*`到`menu/<version>/<locale>/*`, 修改成对应的翻译
- 举个例子，现在为Sublime Text Build 3999添加一个语言代码为`my`的汉化菜单
	- 打开`LocalizedMenu`插件目录`Preference` -> `Languages` -> `Add a language`
	- 进入`locale`目录, 复制`en`目录并命名为`my`
	- 进入`my`目录把`en.json`改名为`my.json`, 并修改为

	```JavaScript
	{
		"link": "",
		"hidden": false,
		"caption": "本帅专用翻译",
		"mnemonic": "m"
	}
	```

	- 进入目录`menu/3999`, 复制`en`目录并命名为`my`, 并将各菜单文件中的`caption`项汉化，如果有，记得后面附加上热键`(<字母>)`。
	- 发现新添加的语言`Preference` -> `Languages` -> `Detect`,然后语言菜单中就有刚添加的`本帅专用翻译 (my)`的菜单项了。

	> **locale配置项说明**<br>
	> link： 要链接到的语言代码<br>
	> hidden： 是否隐藏菜单项<br>
	> caption： 语言名，语言代码会在菜单中加括号自动带上<br>
	> mnemonic： 热键，可选，请确保caption有这个字母，区分大小写

# <a name="submit-a-language"></a>怎样提交翻译语言
- 语言代码的命名必须是这样的：`<languageCode>`或`<languageCode>_<countryCode>`
	- `<languageCode>`要小写, `<countryCode>`要大写(当然你若在本地使用，命名请随意！)
	- 各语言的ISO标准代码: http://www.wikipedia.org/wiki/ISO_639-1
	- 各国家的ISO标准代码: http://www.wikipedia.org/wiki/ISO_3166-1
- Fork本项目到你的库中
- 添加的语言翻译后提交pull request

# 语言及贡献者
- de_DE Deutsch *by [Standarduser](https://github.com/Standarduser)*
- es_ES Español *by [Dastillero](https://github.com/dap39)*
- fr_FR Français *by [fxbenard](https://github.com/fxbenard)*
- hy Հայերեն *by [Arman High Foundation](https://github.com/ArmanHigh)*
- pt Português do Brasil *by [JNylson](https://github.com/jnylson)*
- ru Русский *by [Dimox](http://dimox.name) & [Ant0sh](https://github.com/Ant0sh)*
- sv_SE Svenska *by [H2SO4JB](https://github.com/H2SO4JB)*
- zh_CN 简体中文 *by [Zam](https://github.com/zam1024t)*
- zh_TW 繁体中文 *by [Zam](https://github.com/zam1024t)*

# 问题反馈
- [GitHub issues](https://github.com/zam1024t/LocalizedMenu/issues)
- [zam1024t@gmail.com](mailto:zam1024t@gmail.com)

# 常见问题(FAQ)
- 问：安装插件后不小心把原始的en翻译给改乱或改错了怎么办？<br>
  答：卸载本插件后重新安装即可。

# 项目关联讨论
- https://github.com/wbond/package_control_channel/pull/5665
- https://github.com/rexdf/ChineseLocalization/issues/10

# 开源许可协议
[The MIT License](LICENSE)
