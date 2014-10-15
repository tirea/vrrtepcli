#!/usr/bin/python
# -*- coding: utf-8 -*-
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

import sys
import os
from rhyme import navRhyme
from quiz import quiz
from scramble import game

##arguments##
for arg in sys.argv:
    arg.lower()
if sys.argv[-1].startswith('-'):
    params = sys.argv[1:]
else:
    params = sys.argv[1:-1]

###TRANSLTATOR###

#Get ID of Na'vi word
def getnavid(wordin):
    try:
        metaWords = open(os.path.join(os.path.dirname(sys.argv[0]), "metaWords.txt"),"r")
    except IOError:
        metaWords = open(raw_input("filepath of metaWords.txt? : "),"r")
    navid = 'ERROR'
    wordin = wordin.lower()
    for line in metaWords:
        inword = '\t'+ wordin +'\t'
        
        ## This decoding is important!
        ## Removing it breaks Windows support for N->E dictionary.
        uin=inword.decode("latin-1")
        uin=uin.encode("utf-8")

        if uin in line.lower():
        #if inword in line.lower():
            metaLine = line.lower()
            navid = metaLine[0:metaLine.index('\t')]
            break
    metaWords.close()
    return navid

#Get ID of a localized word
def getlocid(wordin,lang):
    try:
        localizedWords = open(os.path.join(os.path.dirname(sys.argv[0]), "localizedWords.txt"),"r")
    except IOError:
        localizedWords = open(raw_input("filepath of localizedWords.txt? : "),"r")
    idlist = []
    wordin = wordin.lower()
    for line in localizedWords:
        inword = '\t'+ wordin + '\t'
        endword = r'//' + wordin + '\t'
        wordcomma = '\t' + wordin + ','
        wordspace = '\t' + wordin + ' '
        spacecomma = ' ' + wordin + ','
        spaceword = ' '+ wordin + '\t'
        #resolve coding issues once and for all
        #Do not remove <!--
        inword = inword.decode("latin-1")
        inword = inword.encode("utf-8")
        endword = endword.decode("latin-1")
        endword = endword.encode("utf-8")
        wordcomma = wordcomma.decode("latin-1")
        wordcomma = wordcomma.encode("utf-8")
        wordspace = wordspace.decode("latin-1")
        wordspace = wordspace.encode("utf-8")
        spacecomma = spacecomma.decode("latin-1")
        spacecomma = spacecomma.encode("utf-8")
        spaceword = spaceword.decode("latin-1")
        spaceword = spaceword.encode("utf-8")
        #-->
        if lang in line and inword in line.lower():
            localizedLine = line.lower()
            locid = localizedLine[0:localizedLine.index('\t')]
            idlist.append(locid)
        elif lang in line and wordcomma in line.lower():
            localizedLine = line.lower()
            locid = localizedLine[0:localizedLine.index('\t')]
            idlist.append(locid)
        elif lang in line and wordspace in line.lower():
            localizedLine = line.lower()
            locid = localizedLine[0:localizedLine.index('\t')]
            idlist.append(locid)
        elif lang in line and spaceword in line.lower():
            localizedLine = line.lower()
            locid = localizedLine[0:localizedLine.index('\t')]
            idlist.append(locid)
        elif lang in line and spacecomma in line.lower():
            localizedLine = line.lower()
            locid = localizedLine[0:localizedLine.index('\t')]
            idlist.append(locid)
        elif lang in line and endword in line.lower():
            localizedLine = line.lower()
            locid = localizedLine[0:localizedLine.index('\t')]
            idlist.append(locid)
    localizedWords.close()
    return idlist

def transnav(navid,lang):
    try:
        localizedWords = open(os.path.join(os.path.dirname(sys.argv[0]), "localizedWords.txt"),"r")
    except IOError:
        localizedWords = open(raw_input("filepath of localizedWords.txt? : "),"r")
    lst = []
    xstr = ""
    ystr = ""
    zstr = ""
    for line in localizedWords:
        localid = line[0:line.index('\t')]
        if navid == localid and lang in line:
            localizedLine = line.lower()
            for char in localizedLine:
                lst.append(char)
            semi = lst.index('\t')
            lst.remove('\t')
            semi2 = lst.index('\t')
            lst.remove('\t')
            #x is the language
            x = lst[semi:semi2]
            for char in x:
                xstr += str(char)
            xstr = unicode(xstr,"utf-8")
            semi3 = lst.index('\t')
            lst.remove('\t')
            #y is local word
            y = lst[semi2:semi3]
            for char in y:
                ystr += str(char)
            ystr = unicode(ystr,"utf-8")
            #z is the part of speech
            z = lst[semi3:-1]
            for char in z:
                zstr += str(char)
            zstr = unicode(zstr,"utf-8")
    if navid == "ERROR":
        zstr,ystr = "Not","Found"
    localizedWords.close()
    return zstr,ystr

#Translates local words to Na'vi
def loctrans(locid):
    try:
        metaWords = open(os.path.join(os.path.dirname(sys.argv[0]), "metaWords.txt"),"r")
    except IOError:
        metaWords = open(raw_input("filepath of metaWords.txt? : "),"r")
    lst = []
    xstr = ""
    ystr = "["
    zstr = ""
    zzstr = ""
    for line in metaWords:
        localid = line[0:line.index('\t')]
        if locid == localid:
            metaLine = line.lower()
            for char in metaLine:
                lst.append(char)
            semi = lst.index('\t')
            lst.remove('\t')
            semi2 = lst.index('\t')
            lst.remove('\t')
            #x is the na'vi word
            x = lst[semi:semi2]
            for char in x:
                xstr += str(char)
            semi3 = lst.index('\t')
            lst.remove('\t')
            #unicode necessary for good output
            xstr = unicode(xstr, "utf-8")
            #y is IPA
            y = lst[semi2:semi3]
            for char in y:
                ystr += str(char)
            ystr += "]"
            semi4 = lst.index('\t')
            lst.remove('\t')
            #DO NOT UNCOMMENT THIS! IT MAKES THE PROGRAM CRASH.
            #ystr = unicode(ystr, "utf-8")
            
            #z is the possible infix else \N
            z = lst[semi3:semi4]
            for char in z:
                zstr += str(char)
            #unicode necessary for good output
            zstr = unicode(zstr, "utf-8")
            #zz is the part of speech
            zz = lst[semi4:-1]
            for char in zz:
                zzstr += str(char)
            #unicode necessary for good output
            zzstr = unicode(zzstr, "utf-8")
            if '-ipa' in params and '-i' not in params:
                metaWords.close()
                return zzstr,xstr,ystr
            elif '-i' in params and '-ipa' not in params:
                metaWords.close()
                return zzstr,xstr,zstr
            elif '-ipa' in params and '-i' in params:
                metaWords.close()
                return zzstr,xstr,ystr,zstr
            else:
                metaWords.close()
                return zzstr,xstr

#get ipa of Na'vi word from Na'vi word
def getnavipa(navid):
    try:
        metaWords = open(os.path.join(os.path.dirname(sys.argv[0]), "metaWords.txt"),"r")
    except IOError:
        metaWords = open(raw_input("filepath of metaWords.txt? : "),"r")
    lst = []
    ipastr = "["
    for line in metaWords:
        id = int(line[0:line.index('\t')])
        if int(navid) == id:
            metaLine = line.lower()
            for char in metaLine:
                lst.append(char)
            semi = lst.index('\t')
            lst.remove('\t')
            semi2 = lst.index('\t')
            lst.remove('\t')
            semi3 = lst.index('\t')
            lst.remove('\t')
            ipa = lst[semi2:semi3]
            for char in ipa:
                ipastr += str(char)
            ipastr += "]"
            ipastr = unicode(ipastr,"utf-8")
            break
    metaWords.close()
    return ipastr

#get infix positions of Na'vi word from Na'vi word
def getnavinfpos(navid):
    try:
        metaWords = open(os.path.join(os.path.dirname(sys.argv[0]), "metaWords.txt"),"r")
    except IOError:
        metaWords = open(raw_input("filepath of metaWords.txt? : "),"r")
    lst = []
    istr = ""
    for line in metaWords:
        id = int(line[0:line.index('\t')])
        if int(navid) == id:
            metaLine = line.lower()
            for char in metaLine:
                lst.append(char)
            semi = lst.index('\t')
            lst.remove('\t')
            semi2 = lst.index('\t')
            lst.remove('\t')
            semi3 = lst.index('\t')
            lst.remove('\t')
            semi4 = lst.index('\t')
            lst.remove('\t')
            i = lst[semi3:semi4]
            for char in i:
                istr += str(char)
            istr = unicode(istr, "utf-8")
            break
    metaWords.close()
    return istr
            
def main():
    if '-s' not in params and '-q' not in params:
        sysarg = ['vrrtepcli.py','./vrrtepcli.py','/usr/bin/vrrtepcli.py','/usr/local/bin/vrrtepcli']
        if sys.argv[-1].startswith('-') == False and sys.argv[-1] not in sysarg:
            wordin = sys.argv[-1]
            wordin.lower()
        else:
            wordin = raw_input('vrrtep:> ')
            ## Fixes here to support unicode.
            ## You can't make Latin-1 or UTF-8 from STDIN, so workaround used...
            ##
            ## NEVER ATTEMPT TO CONVERT DIRECTLY! Doing so breaks unicode support for arguments!
            wordin = unicode(wordin,sys.stdin.encoding)
            wordin = wordin.encode("latin-1")
            ## End fixes
            wordin.lower()
        
    #ptbr
    if '-ptbr' in params:
        lang = '\tptbr\t'
        uage = 'ptbr'
    #sv
    elif '-sv' in params:
        lang = '\tsv\t'
        uage = 'sv'
    #hu
    elif '-hu' in params:
        lang = '\thu\t'
        uage = 'hu'
    #nl
    elif '-nl' in params:
        lang = '\tnl\t'
        uage = 'nl'
    #est
    elif '-est' in params:
        lang = '\test\t'
        uage = 'est'
    #de
    elif '-de' in params:
        lang = '\tde\t'
        uage = 'de'
    else:
        lang = '\teng\t'
        uage = 'eng'

    #These if statements are heavily customized for Windows. Much of it cannot
    #and should not be copied directly from the Linux revision.
    if '-n' in params:
        if '-s' in params and '-n' in params:
            print "-n argument is incompatible with Scramble game.\n"
            sys.exit()
        elif '-q' in params and '-n' in params:
            print "-n argument is incompatible with Quiz game.\n"
            sys.exit()
        
        # Put this here because wordin is undefined when the above are true...
        navid = getnavid(wordin)
        if '-ipa' in params and '-l' not in params and '-i' not in params:
            print "IPA is not supported on Windows platforms.\n"
            sys.exit()
            #ipa = getnavipa(navid)
            #wordin = unicode(wordin,"latin-1")
            #print wordin,ipa
        elif '-i' in params and '-l' not in params and '-ipa' not in params:
            infpos = getnavinfpos(navid)
            wordin = unicode(wordin,"latin-1")
            print wordin,infpos
        elif '-i' in params and '-ipa' in params and '-l' not in params:
            print "IPA is not supported on Windows platforms.\n"
            sys.exit()
            #ipa = getnavipa(navid)
            #infpos = getnavinfpos(navid)
            #wordin = unicode(wordin,"latin-1")
            #print wordin,ipa,infpos 
        else:
            pos,defn = transnav(navid,lang)
            print pos,defn
        print
    elif '-l' in params and '-q' not in params and '-s' not in params:
        idlist = getlocid(wordin,lang)
        print 'Query matches:'
        for locid in idlist:
            if '-ipa' in params and '-i' not in params:
                print "IPA is not supported on Windows platforms.\n"
                sys.exit()
                #pos,defn,ipa = loctrans(locid)
                #print pos,defn,ipa
            elif '-i' in params and '-ipa' not in params:
                pos,defn,infx = loctrans(locid)
                print pos,defn,infx
            elif '-ipa' in params and '-i' in params:
                print "IPA is not supported on Windows platforms.\n"
                sys.exit()
                #pos,defn,uipa,infx = loctrans(locid)
                #print pos,defn,uipa,infx
            else:
                pos,defn = loctrans(locid)
                print pos,defn
        print
    elif '-r' in params:
        navRhyme(wordin)
        print
        print

    elif '-q' in params and '-l' in params:
        quiz(uage+'.txt','naviwords.txt')
    elif '-q' in params and '-l' not in params:
        quiz('naviwords.txt',uage+'.txt')
        print

    elif '-s' in params and '-l' in params:
        print "No local language support in vCLI Scramble\n"
        print "Run 'vrrtepcli -h' for usage."
        sys.exit()
    elif '-s' in params and '-l' not in params:
        try:
            game()
        except KeyboardInterrupt:
            print
            sys.exit()
        except EOFError:
            print
            sys.exit()
        print
    else:
        navid = getnavid(wordin)
        pos,defn = transnav(navid,lang)
        print pos,defn
        print
try:
    main()
except EOFError:
    print
    metaWords.close()
    localizedWords.close()
    sys.exit()
except KeyboardInterrupt:
    print
    try:
        metaWords.close()
        localizedWords.close()
    except NameError:
        sys.exit()
    sys.exit()

