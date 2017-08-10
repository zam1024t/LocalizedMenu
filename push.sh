#!/bin/bash

# git checkout master
# git checkout multiple_push push.sh
# git reset HEAD
# chmod +x push.sh
# ./push.sh

git checkout master
if [[ `git diff --name-only` != '' ]]; then
	echo 'Has uncommit changes.'
	exit 0
fi
lastcommit=`git log -n 1 --pretty=format:"%H"`

# push to oschina
read -p "Start set statics for oschina... (press any key to continue, wait 9s)" -t 9 -n 1
git push osc master -f
sed -i 's/<br>//g' *.md
sed -i 's/<br>//g' readme/*.md
sed -i 's/raw.githubusercontent.com\/zam1024t\/LocalizedMenu/git.oschina.net\/zam1024t\/LocalizedMenu\/raw/g' *.md
sed -i 's/raw.githubusercontent.com\/zam1024t\/LocalizedMenu/git.oschina.net\/zam1024t\/LocalizedMenu\/raw/g' readme/*.md
git commit -m"set statics for oschina" .
git push osc master
read -p "set statics for oschina, Done. (press any key to continue, wait 9s)" -t 9 -n 1

# push to coding
git reset $lastcommit
git checkout .
read -p "Start set statics for coding... (press any key to continue, wait 9s)" -t 9 -n 1
git push coding master -f
sed -i 's/raw.githubusercontent.com\/zam1024t\/LocalizedMenu/coding.net\/u\/zam1024t\/p\/LocalizedMenu\/git\/raw/g' *.md
sed -i 's/raw.githubusercontent.com\/zam1024t\/LocalizedMenu/coding.net\/u\/zam1024t\/p\/LocalizedMenu\/git\/raw/g' readme/*.md
git commit -m"set statics for coding" .
git push coding master
read -p "set statics for coding, Done. (press any key to continue, wait 9s)" -t 9 -n 1

# clean changes
git reset $lastcommit
git checkout .
echo 'All done.'
