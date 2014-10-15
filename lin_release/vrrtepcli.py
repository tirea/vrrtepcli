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
import root
import grammar

##arguments##
for arg in sys.argv:
    arg.lower()
if sys.argv[-1].startswith('-'):
    params = sys.argv[1:]
else:
    params = sys.argv[1:-1]
DEBUG = False
if "-D" in params:
    DEBUG = True

###TRANSLTATOR###










#get ID of a Na'vi word
def getnavid(wordin):
    wordhas = []
    try:
        metaWords = open(os.path.join(os.path.dirname(sys.argv[0]), "metaWords.txt"),"r")
    except IOError:
        metaWords = open(raw_input("filepath of metaWords.txt? : "),"r")
    navid = 'ERROR'
    if DEBUG:
        print "<DEBUG>"
        print "navid =",navid
    wordin = wordin.lower()
    if DEBUG:
        print "in for, inword = \t"+wordin+"\t"
    isVerb = False
    isNoun = False
    isAdj = False
    isDem = False
    for line in metaWords:
        inword = '\t'+ wordin +'\t'
        if inword in line.lower():
            metaLine = line.lower()
            navid = metaLine[0:metaLine.index('\t')]
            if DEBUG:
                print "navid =",navid
            break
            metaWords.close()
    if navid == 'ERROR':
        try:
            metaWords = open(os.path.join(os.path.dirname(sys.argv[0]), "metaWords.txt"),"r")
        except IOError:
            metaWords = open(raw_input("filepath of metaWords.txt? : "),"r")
        if DEBUG:
            print "ifERROR, navid =",navid
        antiprefixedNoun,prefixes = root.antiprefix(wordin)
        if DEBUG:
            print "antiprefixed wordin =",antiprefixedNoun
        antisuffixedNoun,suffixes = root.antisuffix(antiprefixedNoun)
        if DEBUG:
            print "antisuffixed wordin=",antisuffixedNoun, "try for again"
        outfixedVerb = ""
        outfixedVerb,wordhas = root.outfix(antisuffixedNoun)
        if DEBUG:
            print "outfixed wordin =",outfixedVerb
        antilen = outfixedVerb #antisuffixedNoun
        tmp = []
        lent = False
        if not root.exists(outfixedVerb) and not root.exists(antisuffixedNoun) and not root.exists(antiprefixedNoun):
            antilen,tmp = root.antilenite(outfixedVerb)#antisuffixedNoun
            if DEBUG:
                print "antilenited wordin=",antilen,"try for again"
            lent = True
        if DEBUG:
            print "in for, inword = \t"+antilen+"\t"
        for line in metaWords:
            inword = '\t'+ antilen +'\t'
            if inword in line.lower():
                metaLine = line.lower()
                if "1788" in metaLine or "\tv." in metaLine or "\tvin." in metaLine or "\tvtr." in metaLine or "vim." in metaLine or "vtrm." in metaLine:
                    #1788 is hack for si
                    isVerb = True
                elif "prop." in metaLine or "\tn." in metaLine or "\tpn." in metaLine:
                    isNoun = True
                elif "\tadj." in metaLine:
                    isAdj = True
                elif "\tdem." in metaLine:
                    isDem = True
                if isNoun or isDem or isAdj:
                    navid = metaLine[0:metaLine.index('\t')]
                    prefixes.extend(suffixes)
                    prefixes.extend(tmp)
                    wordhas = prefixes
                    if lent:
                        wordhas.append('lenited')
                if isVerb:
                    navid = metaLine[0:metaLine.index('\t')]
                    wordhas.extend(prefixes)
                    if "us" in wordhas and "tì" in wordhas:
                        wordhas.append("(gerund)")
                        wordhas.extend(suffixes)
                    elif "yu" in suffixes:
                        wordhas.extend(suffixes)

                if DEBUG:
                    print "navid =",navid
                break
                metaWords.close()

    if navid == 'ERROR':
        wordhas = []
    for w in wordhas:
        if wordhas.count(w) > 1:
            while wordhas.count(w) > 1:
                wordhas.remove(w)
    if DEBUG:
        print "</DEBUG:begin Output>"
    return navid,wordhas










#get ID of a local word
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










#translate a Na'vi word to local
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
            semi3 = lst.index('\t')
            lst.remove('\t')
            #y is local word
            y = lst[semi2:semi3]
            for char in y:
                ystr += str(char)
            #z is the part of speech
            z = lst[semi3:-1]
            for char in z:
                zstr += str(char)
    if navid == "ERROR":
        zstr,ystr = "Not","Found"
    localizedWords.close()
    return zstr,ystr










#translate local words to Na'vi
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
#            xstr = unicode(xstr, "utf-8")
            #y is IPA
            y = lst[semi2:semi3]
            for char in y:
                ystr += str(char)
            ystr += "]"
            semi4 = lst.index('\t')
            lst.remove('\t')
#            ystr = unicode(ystr, "utf-8")
            #z is the possible infix else \N
            z = lst[semi3:semi4]
            for char in z:
                zstr += str(char)
#            zstr = unicode(zstr, "utf-8")
            #zz is the part of speech
            zz = lst[semi4:-1]
            for char in zz:
                zzstr += str(char)
#            zzstr = unicode(zzstr, "utf-8")
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
	try:
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
#            ipastr = unicode(ipastr,"utf-8")
	        break
        except ValueError:
            print "Not Found\n"
            exit()

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
#            istr = unicode(istr, "utf-8")
            break
    metaWords.close()
    return istr










def main():
    if '-s' not in params and '-q' not in params and '-g' not in params:
        sysarg = ['vrrtepcli.py','./vrrtepcli.py','/usr/bin/vrrtepcli.py','/usr/local/bin/vrrtepcli']
        if sys.argv[-1].startswith('-') == False and sys.argv[-1] not in sysarg:
            wordin = sys.argv[-1]
            wordin.lower()
        else:
            wordin = raw_input('vrrtep:> ')
            wordin.lower()
    #de
    if '-de' in params:
        lang = '\tde\t'
        uage = 'de'
    #est
    elif '-est' in params:
        lang = '\test\t'
        uage = 'est'
    #hu
    elif '-hu' in params:
        lang = '\thu\t'
        uage = 'hu'
    #nl
    elif '-nl' in params:
        lang = '\tnl\t'
        uage = 'nl'
    #ru
    elif '-ru' in params:
        lang = '\tru\t'
        uage = 'ru'
    #sv
    elif '-sv' in params:
        lang = '\tsv\t'
        uage = 'sv'
    else:
        lang = '\teng\t'
        uage = 'eng'
    if '-n' in params:
        if '-s' in params:
            print "-n argument incompatible with Scramble game.\n"
            sys.exit()
        elif '-q' in params:
            print "-n argument incompatible with Quiz game.\n"
            sys.exit()
        elif '-g' in params:
            print "-n argument incompatible with Grammar Analyzer\n"

        # Put this here because another IF makes wordin undefined when -s or -q is set. --Swoka Ikran
        navid,wordhas = getnavid(wordin)

        if '-ipa' in params and '-l' not in params and '-i' not in params:
            ipa = getnavipa(navid)
            print wordin,ipa

        elif '-i' in params and '-l' not in params and '-ipa' not in params:
            infpos = getnavinfpos(navid)
            print wordin,infpos
        elif '-i' in params and '-ipa' in params and '-l' not in params:
            ipa = getnavipa(navid)
            infpos = getnavinfpos(navid)
            print wordin,ipa,infpos

        else:
            pos,defn = transnav(navid,lang)
            if not wordhas == []:
                print pos,defn,"| affixes:",
                for infix in wordhas:
                    print infix,
                print
            else:
                print pos,defn

        print
    elif '-l' in params and '-q' not in params and '-s' not in params:
        idlist = getlocid(wordin,lang)
        print 'Query matches:'
        for locid in idlist:

            if '-ipa' in params and '-i' not in params:
                pos,defn,ipa = loctrans(locid)
                npos,ndefn = transnav(locid,lang)
                print pos,defn,ipa,'\t('+ndefn+')'
            elif '-i' in params and '-ipa' not in params:
                pos,defn,infx = loctrans(locid)
                npos,ndefn = transnav(locid,lang)
                print pos,defn,infx,'\t('+ndefn+')'
            elif '-ipa' in params and '-i' in params:
                pos,defn,uipa,infx = loctrans(locid)
                npos,ndefn = transnav(locid,lang)
                print pos,defn,uipa,infx,'\t('+ndefn+')'
            else:
                pos,defn = loctrans(locid)
                npos,ndefn = transnav(locid,lang)
                print pos,defn,'\t('+ndefn+')'
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
        print "run 'vrrtepcli -h' for usage."
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
    elif '-g' in params and '-l' not in params:
        if DEBUG:
            print "<DEBUG:Grammar Analyzer>"
            print "params:",params
            print "sys.argv:",sys.argv
        #if "-sent=" in sys.argv[2]:
        #    if DEBUG:
        #        print sys.argv
        #        print sys.argv[2]
        args = []
        sent = ""
        count = 0
        sent_in_argv = False
        for arg in sys.argv:
            if not arg.startswith("-sent="):
                if DEBUG:
                    print "not arg.startswith(-sent=)"
                    print "arg:",arg
                    print "args:",args
                args.append(arg)
                count += 1
            else:
                sent_in_argv = True
                break
        if DEBUG:
            print "sys.argv[count:]",sys.argv[count:]
        if not sent_in_argv:
            sent = raw_input('vrrtep:> ').split()
        else:
            for arg in sys.argv[count:]:
                if DEBUG:
                    print "arg:",arg
                sent += arg
                sent += " "
            args.append(sent)
            #sent = sys.argv[2].replace('-sent=','',1).split()
            sent = sent.replace('-sent=','',1).split()
            if DEBUG:
                print "sys.argv:",sys.argv
                print "sys.argv[2]:",sys.argv[2]
                print "sent:",sent
            if DEBUG:
                print "</DEBUG:Begin Analysis>"
        try:
            grammar.analyze(sent)
        except KeyboardInterrupt:
            print
            sys.exit()
        except EOFError:
            print
            sys.exit()
    else:
        navid,wordhas = getnavid(wordin)
        pos,defn = transnav(navid,lang)
        if not wordhas == []:
            print pos,defn,"| affixes:",
            for infix in wordhas:
                print infix,
            print
        else:
            print pos,defn
        print










try:
    main()
except EOFError:
    print
    try:
        metaWords.close()
        localizedWords.close()
    except NameError:
        pass
    sys.exit()
except KeyboardInterrupt:
    print
    try:
        metaWords.close()
        localizedWords.close()
    except NameError:
        sys.exit()
    sys.exit()
