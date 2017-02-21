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
   #if not root, install everything in ~/.vrrtepcli and make an alias in ~/.bashrc
   mkdir ~/.vrrtepcli
   chmod a+rw ~/.vrrtepcli
   mv vrrtepcli.sh uninstall.sh vrrtepcli_update.sh vrrtepcli_update-all.sh vrrtepcli.py localizedWords.txt metaWords.txt naviwords.txt de.txt est.txt eng.txt hu.txt nl.txt sv.txt ru.txt dictversion.txt scramble.py rhyme.py quiz.py root.py grammar.py ~/.vrrtepcli
   echo "alias vrrtepcli='~/.vrrtepcli/vrrtepcli.sh'" >> ~/.bashrc
   echo "vrrtepcli successfully installed to home folder."
   echo "please restart bash or open a new terminal, and then update by running vrrtepcli -u"
else
   #if user is root, ask where to install the datafiles and executable
   echo "Enter install path for data files:"
   read FILEPATH
   if [ ! -d "$FILEPATH" ]; then
      mkdir $FILEPATH
      mv vrrtepcli.sh install.sh uninstall.sh vrrtepcli_update.sh vrrtepcli.py localizedWords.txt metaWords.txt naviwords.txt de.txt est.txt eng.txt hu.txt nl.txt sv.txt dictversion.txt scramble.py rhyme.py quiz.py root.py grammar.py $FILEPATH
   else
   mv vrrtepcli.sh uninstall.sh vrrtepcli_update.sh vrrtepcli_update-all.sh vrrtepcli.py localizedWords.txt metaWords.txt naviwords.txt de.txt est.txt eng.txt hu.txt nl.txt sv.txt ru.txt dictversion.txt scramble.py rhyme.py quiz.py root.py grammar.py $FILEPATH
   fi
   echo $FILEPATH/vrrtepcli.sh \$@ >> /usr/bin/vrrtepcli
   chmod +x /usr/bin/vrrtepcli
   echo "vrrtepcli successfully installed to $FILEPATH"
   echo "please update by running vrrtepcli -u"
fi
