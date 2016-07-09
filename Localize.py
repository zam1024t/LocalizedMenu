import sublime, sublime_plugin
import os, re, json, codecs

__version__ = '1.0.0'

p = sublime.platform()
version = sublime.version()
v = version[0]

ps = os.path.abspath(__file__).split(os.sep)
pName = ps[-2]
pkgs = sublime.packages_path()
if not pkgs:
	pkgs = os.sep.join(ps[:-2])
dDir = pkgs+os.sep+'Default'
pDir = pkgs+os.sep+pName
mDir = pDir+os.sep+'menu'
lDir = pDir+os.sep+'locale'

mExt = '.sublime-menu.json'
sFile = pName + '.sublime-settings'
cFile = pName + '.sublime-commands'

class LocalizeRunCommand(sublime_plugin.WindowCommand):
	def run(self, action):
		if action == 'reset':
			restoreMenu()
			saveSetting('locale', '')
			return
		elif action == 'detect':
			makeMenu('', True)
			makeCommand('', True)
			return
		elif action == 'add':
			self.window.run_command("open_dir", {"dir": pDir})
		elif action == 'submit':
			self.window.run_command("open_url", {"url": "https://github.com/zam1024t/"+pName+"#submit-a-language"})

class LocalizeCommand(sublime_plugin.ApplicationCommand):
	def run(self, locale):
		saveSetting('locale', locale)
	def is_checked(self, locale):
		return locale == getSetting('locale')

def setLocale(locale, force = False):
	if not locale:
		return

	if (not force) and locale == getSetting('locale'):
		return

	link = getLink(locale)
	if link:
		locale = link

	m = {}
	d = os.path.join(mDir, v, locale)
	m.update(findMenu(d))

	sDir = ''
	d = os.path.join(mDir, version)
	if not os.path.isdir(d):
		sDir = findSimilarVer()
		if not sDir:
			return
		d = os.path.join(mDir, sDir)

	d = os.path.join(d, locale)
	if not os.path.isdir(d):
		return
	m.update(findMenu(d))

	d = os.path.join(d, p)
	m.update(findMenu(d))

	d = os.path.join(d, sublime.arch())
	m.update(findMenu(d))

	updateMenu(m)
	sublime.status_message('Locale ' + locale + ' has loaded.')

def getLink(locale):
	f = os.path.join(lDir, locale, locale+'.json')
	if not os.path.isfile(f):
		return locale
	conf = getJson(f)
	if isset(conf, 'link') and conf['link']:
		locale = conf['link']
	return locale

def findSimilarVer():
	sVer = ''
	for item in os.listdir(mDir):
		subDir = os.path.join(mDir, item)
		if os.path.isdir(subDir) and item.isdigit() and item < version:
			sVer = item
	return sVer

def isset(dict, key):
	try:
		locale = dict[key]
	except KeyError:
		return False
	return True

def updateHotkey(menu):
	for idx, value in enumerate(menu):
		if isset(value, 'mnemonic') and isset(value, 'caption'):
			if value['mnemonic'] not in value['caption']:
				altKey = '('+value['mnemonic'].upper()+')'
				if altKey in value['caption']:
					value['mnemonic'] = value['mnemonic'].upper()
		if isset(value, 'children'):
			value['children'] = updateHotkey(value['children'])
		menu[idx] = value
	return menu

def makeCommand(locale, force = False):
	if not locale and not force:
		return

	f = os.path.join(pDir, '.command.json')
	if not os.path.isfile(f):
		return
	command = getJson(f)

	for item in sorted(os.listdir(lDir)):
		f = os.path.join(lDir, item, item+'.json')
		if os.path.isfile(f):
			conf = getJson(f)
			if isset(conf, 'hidden') and conf['hidden']:
				continue
			caption = item
			if isset(conf, 'caption') and conf['caption']:
				caption = conf['caption']
			command.append({
				"command": "localize",
				"args": {
					"locale": item
				},
				"caption": pName+': ' + caption + ' ('+item+')'
			})
	saveJson(os.path.join(pDir, cFile), command)

def findMenu(d):
	m = {}
	if not os.path.isdir(d):
		return m
	for item in os.listdir(d):
		filename = os.path.join(d, item)
		if os.path.isfile(filename) and item.endswith(mExt):
			m[item] = filename
	return m

def makeMenu(locale, force = False):
	if not locale and not force:
		return
	f = os.path.join(lDir, locale, 'menu.json')
	if not os.path.isfile(f):
		link = getLink(locale)
		if link:
			f = os.path.join(lDir, link, 'menu.json')
	if not os.path.isfile(f):
		f = os.path.join(pDir, '.menu.json')
	menu = getJson(f)

	for item in sorted(os.listdir(lDir)):
		f = os.path.join(lDir, item, item+'.json')
		if os.path.isfile(f):
			conf = getJson(f)
			if isset(conf, 'hidden') and conf['hidden']:
				continue
			caption = item
			if isset(conf, 'caption') and conf['caption']:
				caption = conf['caption']
			menu[0]['children'][1]['children'].append({
				"command": "localize",
				"checkbox": True,
				"args": {
					"locale": item
				},
				"caption": caption + ' ('+item+')'
			})
	mFile = os.path.join(pDir, 'Main.sublime-menu')
	saveJson(mFile, menu)

def updateMenu(m):
	if not os.path.isdir(dDir):
		os.makedirs(dDir)
	for k in m:
		target = os.path.join(dDir, k[:-5])
		menu = getJson(m[k])
		menu = updateHotkey(menu)
		if p == 'osx' and target[-17:].upper() == 'Main.sublime-menu'.upper():
			menu[8]['caption'] = 'Preferences'
			menu[8]['mnemonic'] = 'n'
		saveJson(target, menu)

def backupMenu():
	if not os.path.isdir(dDir):
		return
	if not getSetting('auto_backup', True):
		return
	bDir = os.path.join(mDir, version, 'backup')
	if not os.path.isdir(bDir):
		os.makedirs(bDir)
	for item in os.listdir(dDir):
		filename = os.path.join(dDir, item)
		if os.path.isfile(filename) and item.endswith(mExt[:-5]):
			target = os.path.join(bDir, item + mExt[-5:])
			open(target, 'wb').write(open(filename, 'rb').read())

def restoreMenu():
	if not os.path.isdir(dDir):
		os.makedirs(dDir)
	for item in os.listdir(dDir):
		filename = os.path.join(dDir, item)
		if os.path.isfile(filename) and item.endswith(mExt[:-5]):
			os.remove(filename)
	bDir = os.path.join(mDir, version, 'backup')
	if not os.path.isdir(bDir):
		return
	for item in os.listdir(bDir):
		filename = os.path.join(bDir, item)
		if os.path.isfile(filename) and item.endswith(mExt):
			target = os.path.join(dDir, item[:-5])
			open(target, 'wb').write(open(filename, 'rb').read())

def getSetting(key, value = None):
	conf = sublime.load_settings(sFile)
	return conf.get(key, value)

def setSetting(setting, key, value = None):
	setting.set(key, value)
	return setting

def saveSetting(key, value = None):
	conf = sublime.load_settings(sFile)
	conf.set(key, value)
	return sublime.save_settings(sFile)

def getJson(filename):
	if not os.path.isfile(filename):
		return
	data = ''
	with codecs.open(filename, 'rb', 'utf-8') as file:
		for line in file:
			if line.lstrip().startswith('//'):
				continue
			data = data + "\n" + line
	data = re.sub(",[ \t\r\n]+}", '}', data)
	data = re.sub(",[ \t\r\n]+\]", ']', data)
	arr = []
	try:
		arr = json.loads(data)
	except ValueError:
		pass
	return arr

def saveJson(path, data):
	data = json.dumps(data, ensure_ascii = False, indent = 4).encode('utf-8')
	open(path, 'wb').write(data)

def plugin_loaded():
	sublime.set_timeout(init, 200)

def init():
	locale = ''
	firstRun = False
	fFile = os.path.join(pDir, '.firstRun')
	if not os.path.isfile(fFile):
		firstRun = True
		backupMenu()
		open(fFile, 'wt').write('')
		locale = getSetting('locale', '')
	makeMenu(locale, firstRun)
	makeCommand(locale, firstRun)
	setLocale(locale, firstRun)

	s = sublime.load_settings(sFile)
	s.add_on_change('locale', updateLocale)

def updateLocale():
	locale = getSetting('locale')
	if not locale:
		return
	lFile = os.path.join(pDir, '.lastRun')
	if os.path.isfile(lFile) and open(lFile, 'r').read() == locale:
		return
	makeMenu(locale, True)
	makeCommand(locale, True)
	setLocale(locale, True)
	open(lFile, 'wt').write(locale)

if (v == '2'):
	init()
