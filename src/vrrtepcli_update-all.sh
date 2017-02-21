#!/bin/sh
#    Vrrtep CLI is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public Licence as published by
#    the Free Software Foundation, either version 3 of the Licence, or
#    (at your option) any later version.
#
#    Vrrtep CLI is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Vrrtep CLI.  If not, see <http://www.gnu.org/licenses/>

#check if user is root.
if [ "$(id -u)" != "0" ]; then
#if not, then update as normal.
rm -f ~/.vrrtepcli/metaWords.txt
rm -f ~/.vrrtepcli/localizedWords.txt
rm -f ~/.vrrtepcli/naviwords.txt
rm -f ~/.vrrtepcli/de.txt
rm -f ~/.vrrtepcli/eng.txt
rm -f ~/.vrrtepcli/est.txt
rm -f ~/.vrrtepcli/hu.txt
rm -f ~/.vrrtepcli/nl.txt
rm -f ~/.vrrtepcli/sv.txt
rm -f ~/.vrrtepcli/dictversion.txt
rm -f ~/.vrrtepcli/root.py
rm -f ~/.vrrtepcli/grammar.py
#upgrade program
wget http://tirea.learnnavi.org/source/vrrtepcli.py
wget http://tirea.learnnavi.org/source/quiz.py
wget http://tirea.learnnavi.org/source/rhyme.py
wget http://tirea.learnnavi.org/source/scramble.py
wget http://tirea.learnnavi.org/source/install.sh
wget http://tirea.learnnavi.org/source/uninstall.sh
wget http://tirea.learnnavi.org/source/vrrtepcli.sh
wget http://tirea.learnnavi.org/source/vrrtepcli_update.sh
wget http://tirea.learnnavi.org/source/vrrtepcli_update-all.sh
wget http://tirea.learnnavi.org/source/root.py
wget http://tirea.skxang.lu/source/grammar.py
#update dictionaries
wget http://tirea.learnnavi.org/source/localizedWords.txt
wget http://tirea.learnnavi.org/source/metaWords.txt
wget http://tirea.learnnavi.org/source/naviwords.txt
wget http://tirea.learnnavi.org/source/de.txt
wget http://tirea.learnnavi.org/source/eng.txt
wget http://tirea.learnnavi.org/source/est.txt
wget http://tirea.learnnavi.org/source/hu.txt
wget http://tirea.learnnavi.org/source/nl.txt
wget http://tirea.learnnavi.org/source/sv.txt
wget http://tirea.learnnavi.org/source/dictversion.txt
mv localizedWords.txt metaWords.txt naviwords.txt de.txt eng.txt est.txt hu.txt nl.txt sv.txt dictversion.txt ~/.vrrtepcli/
mv vrrtepcli.sh vrrtepcli.py quiz.py rhyme.py scramble.py install.sh uninstall.sh vrrtepcli_update.sh vrrtepcli_update-all.sh root.py grammar.py ~/.vrrtepcli
else #user is root, update accordingly
DIR="$( cd "$( dirname "$0" )" && pwd )"
rm -f $DIR/metaWords.txt
rm -f $DIR/localizedWords.txt
rm -f $DIR/naviwords.txt
rm -f $DIR/de.txt
rm -f $DIR/eng.txt
rm -f $DIR/est.txt
rm -f $DIR/hu.txt
rm -f $DIR/nl.txt
rm -f $DIR/sv.txt
rm -f $DIR/dictversion.txt
rm -f $DIR/root.py
rm -f $DIR/grammar.py
#upgrade program
wget http://tirea.learnnavi.org/source/vrrtepcli.py
wget http://tirea.learnnavi.org/source/quiz.py
wget http://tirea.learnnavi.org/source/rhyme.py
wget http://tirea.learnnavi.org/source/scramble.py
wget http://tirea.learnnavi.org/source/install.sh
wget http://tirea.learnnavi.org/source/uninstall.sh
wget http://tirea.learnnavi.org/source/vrrtepcli.sh
wget http://tirea.learnnavi.org/source/vrrtepcli_update.sh
wget http://tirea.learnnavi.org/source/vrrtepcli_update-all.sh
wget http://tirea.learnnavi.org/source/root.py
wget http://tirea.skxang.lu/source/grammar.py
#update dictionaries
wget http://tirea.learnnavi.org/source/localizedWords.txt
wget http://tirea.learnnavi.org/source/metaWords.txt
wget http://tirea.learnnavi.org/source/naviwords.txt
wget http://tirea.learnnavi.org/source/de.txt
wget http://tirea.learnnavi.org/source/eng.txt
wget http://tirea.learnnavi.org/source/est.txt
wget http://tirea.learnnavi.org/source/hu.txt
wget http://tirea.learnnavi.org/source/nl.txt
wget http://tirea.learnnavi.org/source/sv.txt
wget http://tirea.learnnavi.org/source/dictversion.txt
mv localizedWords.txt metaWords.txt naviwords.txt de.txt eng.txt est.txt hu.txt nl.txt sv.txt dictversion.txt root.py grammar.py $DIR
mv vrrtepcli.sh vrrtepcli.py quiz.py rhyme.py scramble.py install.sh uninstall.sh vrrtepcli_update.sh vrrtepcli_update-all.sh root.py grammar.py $DIR
fi
