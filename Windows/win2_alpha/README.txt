Vrrtep CLI was written with Python v2.6.6 and Python v2.7.1 it is most likely not compatible with
Python 3. it should work with 2.5 or whatever else (as far as I know.)
****The included license (GPL) applies to ALL FILES which came packaged in the .zip archive.****

Vrrtep CLI is NOW CROSS-PLATFORM, thanks to Swoka Ikran.

##INSTALLATION##

Just run the install script to install:
Run install.cmd

If you have admin privledges, you now have the option of installing the program for all users. 
All accounts will be able to use the program without installing it themselves. Note that
the dictionary can only be updated by an admin if installed in this manner.

**Windows Vista/7/8 Users**: Right Click the Install.cmd and choose "Run As Administrator"
if you plan to install for all users. This is not required for current-user installations.

##RUNNING##

All you have to do is:

vrrtepcli [args]

TIP: Please run vrrtepcli -h to see the usage info and tips

##UPDATING##

Update vrrtepcli dictionaries by running:

vrrtepcli -u

If the program was installed for all users, updates must be performed
by an administrator. 

On Vista/7/8, you *must* run the command prompt as an administrator.
Failure to do so will result in the update failing.

##UN-INSTALLING##

Open a command prompt and type: vrrtepcli uninstall
(alternately, you can type: uninstall_vcli)

The program will be removed immediately.

If both an all-users and current-user installation exist, the program will ask
which one you want to remove. Admin privledges are required to remove a copy
that was installed for all users.

Vista/7/8 users must run a command prompt as an administrator 
(Start->Programs->Accessories->Right-click Command Prompt->Run As Admin...)
to uninstall an "all users" copy of the program. 

##PROTIPS##

To translate a na'vi word containing infxes, just run the program with local
    language argument and enter a word with infixes inside <>.
The [word] parameter is a nice quick option. it can be a Na'vi or local
    (if -l option specified) word. If you use the [word] argument from terminal,
    ()and <> as well as ' must be escaped. You can use single or double quotes
    around the[word]. This also works for when you would like to search a
    multi-word definition, e.g.: vrrtepcli -l -eng 'for the sake of'
To translate a si verb/phrase such as 'pamrel si' or 'eltur tìtxen si',
    the syntax becomes for example:
    echo "eltur tìtxen si" | vrrtepcli
To translate several words one by one in a single vrrtepcli session,
    the first parameter is the number of words you wish to translate in one session.
    for example to translate 6 words from na'vi to english:
	vrrtepcli 6
To get the infix positions of a Na'vi verb, just type in for example,
	vrrtepcli -n -i yom

##RHYMING DICTIONARY##

Really easy to use. works with and without argument. one word at a time.
for example:

vrrtepcli -r "lì'u"

(notice the quotes, because there as a '(apostrophe/singlequote) character
	in lì'u. see PROTIPS.)

vrrtepcli -r
vrrtep:> lì'u

(no quotes from within the program.)



##SCRAMBLE GAME##



Relatively simple. type in the correctly unscrambled version of what it prompts
    you with.
If you answer correctly, your score goes up a point.
If you answer incorrectly, your score goes down a point. you will be prompted
    to answer correctly until you do, so watch out! but luckily if you get stumped,
    you can:
type ans to see the answer. this will subtract a point from your score.
type /quit or /q or /exit to stop playing The Game.

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


#################
See KNOWN_BUGS for a list of known bugs before reporting. Please do report bugs
	if it is not already on that list.
See LICENSE for licensing information.
################
Thank you for using Vrrtep CLI