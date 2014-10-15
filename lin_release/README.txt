Vrrtep CLI was written with Python v2.6.6 and Python v2.7.1 it is most likely not compatible with
Python 3. it should work with 2.5 or whatever else (as far as I know.)

****The included license (GPL) applies to ALL FILES which came packaged in the
	.tar.gz (or .zip) archive.****

Vrrtep CLI is NOW CROSS-PLATFORM, thanks to Swoka Ikran.

##INSTALLATION##

Just run the install script to install:

run ./install.sh in a terminal after switching to the correct directory.

NOTICE: after doing this you will need to restart bash. Do this by closing
the terminal and opening a new one, or running bash in the current terminal.

### If you install as root, you can choose the install directory###

##RUNNING##

all you have to do is:


vrrtepcli [args]


TIP: please do run vrrtepcli -h to see the usage info and tips


##UPDATING##

update vrrtepcli dictionaries by running:


vrrtepcli -u

upgrade vrrtepcli program files by running:


vrrtepcli -u --all


###You will need to update as root if you installed as root!###

##UN-INSTALLING##
uninstall vrrtepcli by running:

vrrtepcli uninstall

!!!!!!!NOTICE!!!!!!!
* this script WILL delete the last line from ~/.bashrc
  This is because the install script writes an alias command at the end.
* it DOES back up, but only one copy at a time and it overwrites 
  the backup each time. Please do not run this script except 
  some point AFTER running install script.
!!!!!!!!!!!!!!!!!!!!

if you installed as root, you must uninstall as root.

sudo vrrtepcli uninstall

##PROTIPS##

NEW! vrrtepcli now recognizes affixed words WITHOUT extra < > or -
    just enter the word as it is, and vrrtepcli will try to translate it

The [word] parameter is a nice quick option. it can be a Na'vi or local
    (if -l option specified) word. If you use the [word] argument from terminal,
    all ' (glottal stop apostrophe) must be escaped. You have to use \ before
    each '. OR You can use single or double quotes around the[word].
To translate a si verb or a phrase such as 'pamrel si' or 'eltur tìtxen si',
    the syntax becomes for example:
    echo eltur tìtxen si | vrrtepcli
To translate several words one by one in a single vrrtepcli session,
    the first parameter is the number of words you wish to translate in one session.
    for example to translate 6 words from na'vi to english:
	vrrtepcli 6
    TIP: if using all arguments (not interactive), it's easiest to just use 
    this syntax on command line: (for when yuo dont know the exact number of words.)
    (This only works in commandline. using `vrrtepcli 0` to enter interactive does no good.)
	vrrtepcli 0 -l this is a whole sentence
To get the infix positions of a Na'vi verb, just type in for example,
	vrrtepcli -n -i yom
To get the IPA of a Na'vi word, type in for example,
	vrrtepcli -n -ipa atxkxerel
You can of course also get both ipa and infix positions by typing for example,
	vrrtepcli -n -i -ipa yemstokx

##RHYMING DICTIONARY##

Really easy to use. works with and without argument. one word at a time.
for example:

vrrtepcli -r "lì'u"

OR

vrrtepcli -r lì\'u

(notice the quotes or slash, because the '(apostrophe/singlequote) character
	must be escaped. if there is no ' in the word, you do not need a \ or "". see PROTIPS.)

vrrtepcli -r
vrrtep:> lì'u

(no quotes or slashes necessary from within the program.)

##SCRAMBLE GAME##

Relatively simple. type in the correctly unscrambled version of what it prompts
    you with.
If you answer correctly, your score goes up a point.
If you answer incorrectly, your score goes down a point. you will be prompted
    to answer correctly until you do, so watch out! but luckily if you get stumped,
    you can:
type ans to see the answer. this will subtract a point from your score.
type /quit or /q or /exit to stop playing The Game.

VrrtepCLI scramble Keeps track of your high scores and all past scores! just look at the scores files 
	in the directory where vrrtepcli is installed.

##QUIZ GAME##

to play, use the command

vrrtepcli -q

the default is to play with na'vi questions->english answers. To answer in other 
languages, append that language's flag. for example, to answer in Swedish:

vrrtepcli -q -sv

Use the -l flag to play in the local questions->na'vi answers direction.
for example, the following will play Dutch questions and Na'vi answers:

vrrtepcli -q -l -nl

Rules are relatively simple. like a text based CLI ToV or SoL program.

You are shown a word and a 3-list of choices. enter in the number of your 
choice.

If you get it correct, your score goes up a point.
If you are wronge, your score goes down.
You can see the answer by typing the number 4. You lose a point.
Either way, after you answer, the next question is asked.

quit the game by answering with the number 5.

VrrtepCLI Quiz Keeps track of all and high scores! Check out the scores files in the vrrtepcli install directory.


##Vrrtep Analytics: Grammatical ANalysis##

NEW! [IN BETA; SLOW]:

vrrtepcli -g

OR

vrrtepcli -g -sent="<na'vi sentence here>"

allows you to know whether or not your sentence is grammatically correct or not.

IN BETA: THERE ARE BUGS. AND IT IS SLOW AS THE SIZE OF THE SENTENCE GROWS.


#################
See KNOWN_BUGS for a list of known bugs before reporting. Please do report bugs
	if it is not already on that list.
See LICENSE for licensing information.
################
Thank you for using Vrrtep CLI
