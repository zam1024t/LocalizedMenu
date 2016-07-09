# LocalizedMenu
Localize Tool & Localized Menu for Sublime Text 2/3 End User.

- Provide a easy way to add new languages.
- Support multiple version/platform.
- Support share common menus.
- Auto backup local menu.

# Shots
- Work on Windows
![Work on Windows](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_win.gif)
- Work on OS X
![Work on OS X](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_osx.gif)
- Work on Ubuntu
![Work on Ubuntu](https://raw.githubusercontent.com/zam1024t/LocalizedMenu/shots/shots/LocalizedMenu_linux.gif)

### Installtion
git clone to Sublime Text `Packages` dir.

### Usage
Swith language via `Preference` -> `Languages`.

### Add A Language
- cp `locale/en/en.json` to `locale/<locale>/<locale>.json`, localize to your language.
- cp `menu/<version>/en/*` to `menu/<version>/<locale>/*`, localize to your language.

### Submit A Language
- Fork repo.
- Make pull request.

### Locales & Contributors
Language: http://www.wikipedia.org/wiki/ISO_639-1
Country: http://www.wikipedia.org/wiki/ISO_3166-1
- zh_CN 简体中文 by [Zam](https://github.com/zam1024t/LocalizedMenu)
- zh_TW 繁体中文 by [Zam](https://github.com/zam1024t/LocalizedMenu)

### License
[The MIT License](LICENSE).
