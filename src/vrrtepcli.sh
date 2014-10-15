#!/bin/bash
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

#if normal user/install to ~/.vrrtepcli
if [ -d "~/.vrrtepcli" ]; then

	if [ "$1" = "uninstall" ]
	then
		~/.vrrtepcli/uninstall.sh
		clear
		echo -e "Vrrtep CLI successfully uninstalled.\n"
		exit 0

	elif [ "$1" = "-u" ]
	then
		if [ "$2" = "--all" ]
		then
        		~/.vrrtepcli/vrrtepcli_update-all.sh
        		clear
	        	echo -e "VrrtepCLI upgraded.\n"
        		exit 0
		else
			~/.vrrtepcli/vrrtepcli_update.sh
			clear
			echo -e "Vrrtep CLI dictionary updated.\n"
			exit 0
		fi

	elif [ "$1" = "-v" ]
	then
		echo "Vrrtep CLI v2.1 [BETA]"
		echo "Dictionary Version:"
		cat ~/.vrrtepcli/dictversion.txt
		exit 0

	elif [ "$1" = "-h" ]
	then
		echo
		echo "Vrrtep Command-line Interface Na'vi Translator v2.1 [BETA]"
		echo "by Tirea Aean. Licensed under GNU General Public License."
		echo
		echo "Usage: vrrtepcli [-args][word]"
		echo -ne "       vrrtepcli -g [-sent=\"<na'vi string>\"]"
		echo
		echo "----------------------------------------------------------"
		echo "valid arguments:"
		echo "----------------------------------------------------------"
		echo "0-9+ (any integer): loop the program that many times"
		echo "-l : translate from a local language to Na'vi"
		echo "----------------"
		echo "local languages:"
		echo "----------------"
		echo "-eng : english (default if no language specified)"
		echo "-est : Estonian"
		echo "-de : German"
		echo "-hu : Hungarian"
		echo "-nl : Dutch"
		echo "-ru : Russian"
		echo "-sv : Swedish"
		echo "---------------------------------"
		echo "-ipa : show Na'vi IPA in response"
		echo "-i : show possible Na'vi infix"
		echo "---------------------------------"
		echo "-n : translate from Na'vi to local language (default if no -l, overrides -l)"
		echo "---------------------------------"
		echo "-r : na'vi rhyming dictionary"
		echo "---------------------------------"
		echo "-s : na'vi word scramble game"
		echo "---------------------------------"
		echo "-q : na'vi quiz game (-l and lang arguments valid)"
		echo "-g : vrrtep analytics (grammar analysis)"
		echo -ne "-g -sent=\"\<words\>\" : vrrtep analytics"
		echo "---------------------------------"
		echo "-h : show this help menu"
		echo "---------------------------------"
		echo "-u : update the vrrtepcli dictionaries"
		echo "-u --all : upgrade the entire program including dictionaries."
		echo "-v : check the vrrtepcli dictionary version"
		echo "---------------------------------"

	elif [[ "$1" =~ ^[0-9]+$ ]]
	then
		echo "Vrrtep CLI v2.1 [BETA] by Tirea Aean"
		echo "Linux version"
		echo "run 'vrrtepcli -h' for usage"
		echo
		y=0
		#for typing vrrtepcli [num] and entering the program to be prompted for a nav word
		if [ "$2" = "" ]
		then
			while [ $y -lt $1 ]
			do
			python ~/.vrrtepcli/vrrtepcli.py -n
			y=$(( $y + 1 ))
			done
		#for typing vrrtepcli [num] -l and picking up command line words
		elif [ "$2" = "-l" ]
		then
			if [[ "$3" =~ ^$ ]]
			then
				y=0
				while [ $y -lt $1 ]
				do
					python $DIR/vrrtepcli.py -l
					y=$(( $y + 1 ))
				done
			fi
			for a in "$@"
			do
			if [[ "$a" =~ ^[0-9]+$ ]]
			then
				true
			elif [[ "$a" =~ ^- ]]
			then
				true
			else
				if [[ "$3" =~ ^-de ]]
				then
					python ~/.vrrtepcli/vrrtepcli.py -l -de ${a}
				elif [[ "$3" =~ ^-est ]]
				then
					python ~/.vrrtepcli/vrrtepcli.py -l -est ${a}
				elif [[ "$3" =~ ^-eng ]]
				then
					python ~/.vrrtepcli/vrrtepcli.py -l -eng ${a}
				elif [[ "$3" =~ ^-hu ]]
				then
					python ~/.vrrtepcli/vrrtepcli.py -l -hu ${a}
				elif [[ "$3" =~ ^-nl ]]
				then
					python ~/.vrrtepcli/vrrtepcli.py -l -nl ${a}
				elif [[ "$3" =~ ^-sv ]]
				then
					python ~/.vrrtepcli/vrrtepcli.py -l -sv ${a}
				else
					python ~/.vrrtepcli/vrrtepcli.py -l ${a}
				fi
			fi
			done
		#for typing vrrtepcli [num] and picking up command line words
		else
			#while [ $y -lt $1 ]
			#do
			#python ~/.vrrtepcli/vrrtepcli.py $2 $3 $4 $5 $6
			for a in "$@"
			do
			if [[ "$a" =~ ^[0-9]+$ ]]
			then
				true
			elif [[ "$a" =~ ^-  ]]
			then
		    		true
			else
				python ~/.vrrtepcli/vrrtepcli.py ${a}
			fi
       			done
			#y=$(( $y + 1 ))
			#done
		fi
	else
	#default usage with no arguments, or with a param arg
		if [ "$1" = "" ]
		then
			echo "Vrrtep CLI v2.1 [BETA] by Tirea Aean"
			echo "Linux version"
			echo "run 'vrrtepcli -h' for usage"
			echo
			#echo -e "Vrrtep CLI v2.1 | Run 'vrrtepcli -h' for usage.\n"
			python ~/.vrrtepcli/vrrtepcli.py -n
		else
			echo "Vrrtep CLI v2.1 [BETA] by Tirea Aean"
			echo "Linux version"
			echo "run 'vrrtepcli -h' for usage"
			echo
			python ~/.vrrtepcli/vrrtepcli.py $1 $2 $3 $4 $5
		fi
	fi

else #if root install to custom dir
	DIR="$( cd "$( dirname "$0" )" && pwd )"

	if [ "$1" = "uninstall" ]
	then
        	$DIR/uninstall.sh
	        clear
        	echo -e "Vrrtep CLI successfully uninstalled.\n"
	        exit 0

	elif [ "$1" = "-u" ]
	then
		if [ "$2" = "--all" ]
		then
		        $DIR/vrrtepcli_update-all.sh
		        clear
		        echo -e "VrrtepCLI upgraded.\n"
		        exit 0
		else
			$DIR/vrrtepcli_update.sh
			clear
			echo -e "Vrrtep CLI dictionary updated.\n"
			exit 0
		fi

	elif [ "$1" = "-v" ]
	then
		echo "Vrrtep CLI v2.1 [BETA]"
		echo "Dictionary Version:"
		cat $DIR/dictversion.txt
		exit 0

	elif [ "$1" = "-g" ]
	then
		echo "Vrrtep Analytics"
		echo
		$DIR/vrrtepcli.py $@

	elif [ "$1" = "-h" ]
	then
		echo
		echo "Vrrtep Command-line Interface Na'vi Translator v2.1 [BETA]"
		echo "by Tirea Aean. Licensed under GNU General Public License."
		echo
		echo "Usage: vrrtepcli [-args][word]"
		echo -ne "       vrrtepcli -g [-sent=\"<na'vi string>\"]"
		echo
		echo "---------------------------------------------------------"
		echo "valid arguments:"
		echo "---------------------------------------------------------"
		echo "0-9+ (any integer): loop the program that many times"
		echo "-l : translate from a local language to Na'vi"
		echo "----------------"
		echo "local languages:"
		echo "----------------"
		echo "-eng : english (default if no language specified)"
		echo "-est : Estonian"
		echo "-de : German"
		echo "-hu : Hungarian"
		echo "-nl : Dutch"
		echo "-ru : Russian"
		echo "-sv : Swedish"
		echo "---------------------------------"
		echo "-ipa : show Na'vi IPA in response"
		echo "-i : show possible Na'vi infix"
		echo "---------------------------------"
		echo "-n : translate from Na'vi to local language (default if no -l, overrides -l)"
		echo "---------------------------------"
		echo "-r : na'vi rhyming dictionary"
		echo "---------------------------------"
		echo "-s : na'vi word scramble game"
		echo "---------------------------------"
		echo "-q : na'vi quiz game (-l and lang arguments valid)"
		echo "-g : vrrtep analytics (grammar analysis)"
		echo -ne "-g -sent=\"<words>\" : vrrtep analytics"
		echo
		echo "---------------------------------"
		echo "-h : show this help menu"
		echo "---------------------------------"
		echo "-u : update the vrrtepcli dictionaries"
		echo "-u --all : upgrade the entire program including dictionaries."
		echo "-v : check the vrrtepcli dictionary version"
		echo "---------------------------------"

	elif [[ "$1" =~ ^[0-9]+$ ]]
	then
		echo "Vrrtep CLI v2.1 [BETA] by Tirea Aean"
		echo "Linux version"
		echo "run 'vrrtepcli -h' for usage"
		echo
		y=0
		#for typing vrrtepcli [num] and entering the program to be prompted for a nav word
		if [ "$2" = "" ]
		then
			while [ $y -lt $1 ]
			do
			python $DIR/vrrtepcli.py -n
			y=$(( $y + 1 ))
			done
		#for typing vrrtepcli [num] -l and picking up command line words
		elif [ "$2" = "-l" ]
		then
			if [[ "$3" =~ ^$ ]]
			then
				y=0
				while [ $y -lt $1 ]
				do
					python $DIR/vrrtepcli.py -l
					y=$(( $y + 1 ))
				done
			fi
			for a in "$@"
			do
			if [[ "$a" =~ ^[0-9]+$ ]]
			then
				true
			elif [[ "$a" =~ ^- ]]
			then
				true
			else
				if [[ "$3" =~ ^-de ]]
				then
					python $DIR/vrrtepcli.py -l -de ${a}
				elif [[ "$3" =~ ^-est ]]
				then
					python $DIR/vrrtepcli.py -l -est ${a}
				elif [[ "$3" =~ ^-eng ]]
				then
					python $DIR/vrrtepcli.py -l -eng ${a}
				elif [[ "$3" =~ ^-hu ]]
				then
					python $DIR/vrrtepcli.py -l -hu ${a}
				elif [[ "$3" =~ ^-nl ]]
				then
					python $DIR/vrrtepcli.py -l -nl ${a}
				elif [[ "$3" =~ ^-sv ]]
				then
					python $DIR/vrrtepcli.py -l -sv ${a}
				elif [[ "$3" =~ ^$ ]]
				then
					python $DIR/vrrtepcli.py -l -eng ${a}
				else
					python $DIR/vrrtepcli.py -l ${a}
				fi
			fi
			done
		#for typing vrrtepcli [num] and picking up command line words
		else
			#while [ $y -lt $1 ]
			#do
			#python $DIR/vrrtepcli.py $2 $3 $4 $5 $6
			for a in "$@"
			do
			if [[ "$a" =~ ^[0-9]+$ ]]
			then
				true
			elif [[ "$a" =~ ^-  ]]
			then
	    			true
			else
				python $DIR/vrrtepcli.py ${a}
		    	fi
	       		done
			#y=$(( $y + 1 ))
			#done
		fi
	else
	#default usage with no arguments, or with a param arg
		if [ "$1" = "" ]
		then
			echo "Vrrtep CLI v2.1 [BETA] by Tirea Aean"
			echo "Linux version"
			echo "run 'vrrtepcli -h' for usage"
			echo
			#echo -e "Vrrtep CLI v2.1 | Run 'vrrtepcli -h' for usage.\n"
			python $DIR/vrrtepcli.py -n
		else
			echo "Vrrtep CLI v2.1 [BETA] by Tirea Aean"
			echo "Linux version"
			echo "run 'vrrtepcli -h' for usage"
			echo
			python $DIR/vrrtepcli.py $1 $2 $3 $4 $5
		fi
	fi

fi
