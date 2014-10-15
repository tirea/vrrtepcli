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
#if not, uninstall normally:
rm -rf ~/.vrrtepcli
sed -i".bak" '$d' ~/.bashrc
echo "vrrtepcli successfully uninstalled."
else #user is root, uninstall from custom dir
DIR="$( cd "$( dirname "$0" )" && pwd )"
rm $DIR/vrrtepcli.sh $DIR/install.sh $DIR/uninstall.sh $DIR/vrrtepcli_update.sh $DIR/vrrtepcli.py $DIR/localizedWords.txt $DIR/metaWords.txt $DIR/naviwords.txt $DIR/de.txt $DIR/est.txt $DIR/eng.txt $DIR/hu.txt $DIR/nl.txt $DIR/ptbr.txt $DIR/sv.txt $DIR/dictversion.txt $DIR/scramble.py $DIR/rhyme.py $DIR/quiz.py $DIR/quiz.pyc $DIR/rhyme.pyc $DIR/scramble.pyc
rm /usr/bin/vrrtepcli
echo "vrrtepcli successfully uninstalled."
fi
