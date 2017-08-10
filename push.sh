#!/bin/bash

# git checkout master
# git checkout multiple_push push.sh
# git reset HEAD
# chmod +x push.sh
# ./push.sh

# set remote osc
# git remote add osc https://git.oschina.net/zam1024t/LocalizedMenu
git remote add osc https://gitee.com/zam1024t/LocalizedMenu

# set remote coding
git remote add coding https://coding.net/zam1024t/LocalizedMenu

git checkout master
if [[ `git diff --name-only` != '' ]]; then
	echo 'Has uncommit changes.'
	exit 0
fi
lastcommit=`git log -n 1 --pretty=format:"%H"`

# push to oschina
read -p "Start set shots for oschina... (press any key to continue, wait 9s)" -t 9 -n 1
git push osc master -f
sed -i 's/<br>//g' *.md
sed -i 's/<br>//g' readme/*.md
sed -i 's/raw.githubusercontent.com\/zam1024t\/LocalizedMenu/git.oschina.net\/zam1024t\/LocalizedMenu\/raw/g' *.md
sed -i 's/raw.githubusercontent.com\/zam1024t\/LocalizedMenu/git.oschina.net\/zam1024t\/LocalizedMenu\/raw/g' readme/*.md
git commit -m"set shots for oschina" .
git push osc master
read -p "set shots for oschina, Done. (press any key to continue, wait 9s)" -t 9 -n 1

# push to coding
git reset $lastcommit
git checkout .
read -p "Start set shots for coding... (press any key to continue, wait 9s)" -t 9 -n 1
git push coding master -f
sed -i 's/raw.githubusercontent.com\/zam1024t\/LocalizedMenu/coding.net\/u\/zam1024t\/p\/LocalizedMenu\/git\/raw/g' *.md
sed -i 's/raw.githubusercontent.com\/zam1024t\/LocalizedMenu/coding.net\/u\/zam1024t\/p\/LocalizedMenu\/git\/raw/g' readme/*.md
git commit -m"set shots for coding" .
git push coding master
read -p "set shots for coding, Done. (press any key to continue, wait 9s)" -t 9 -n 1

# clean changes
git reset $lastcommit
git checkout .
echo 'All done.'
