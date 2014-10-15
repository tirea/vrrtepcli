#!/usr/bin/python
# -*- coding: utf-8 -*-
#This file is part of vrrtepCLI
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
import random
import os, sys
from time import sleep, asctime

#this function saves the score and saves the high score
def saveHighScore(score,correct,count):

    #FILE IO
    saveFile = open(os.path.join(os.path.dirname(sys.argv[0]), "SCRAMBLE_SCORES.txt"),"a")
    #save the quiz score
    saveFile.write(asctime()+" : "+str(score)+" "+str(correct)+"/"+str(count)+"\n")
    saveFile.close()
    
    saveFile = open(os.path.join(os.path.dirname(sys.argv[0]), "SCRAMBLE_SCORES.txt"),"r")
    highScoresFile = open(os.path.join(os.path.dirname(sys.argv[0]), "SCRAMBLE_HIGH_SCORE.txt"),"a")
    
    #sort out and find high score
    scores = []
    for line in saveFile:
        SCORE = line[27:-1]
        scores.append(SCORE)
    scores.sort()
    
    #hack for 100% in the scores, cuz it sorts 33.3 < 100 < 66.6
    for score in scores:
        if '100.0' not in score:
            highScore = scores[0]
        else:
            highScore = score
            break

    #Save the high score
    highScoresFile.write("Scramble High Score: "+str(highScore)+"\n")
    print "Scramble High Score: "+str(highScore)
#this function scrambles the word. obviously. ;D
def scramble(word):
    
    s=word.lower()
    st=[]
    #append chars of word to a split list
    for char in word:
        st.append(char)
        #keep the two constituents of ì together in right order
        while "\xac" in st:
            st[st.index('\xc3')] = st[st.index('\xc3')] + st[st.index('\xac')]
            del(st[st.index('\xac')])
        #keep the two constituents of Ì together in right order
        while "\x8c" in st:
            st[st.index('\xc3')] = st[st.index('\xc3')] + st[st.index('\x8c')]
            del(st[st.index('\x8c')])
        #keep the two constituents of ä together in right order
        while "\xa4" in st:
            st[st.index('\xc3')] = st[st.index('\xc3')] + st[st.index('\xa4')]
            del(st[st.index('\xa4')])
    n=0
    rst=[]
    #make a list same size as word, random ints as entries
    while n!=len(st):
        rno=random.randint(0,len(st)-1)
        if rst.count(rno)==0:
            rst.append(rno)
            n=n+1
    #print rst
    n=0
    ost=''
    #make a string of the the split list with indices = entries of random int list
    while n!=len(st):
        ost=ost+ st[rst[n]]
        n=n+1
    return s,ost

#make sure user input is not blank (so far..)
def validate():
    aword = unicode(raw_input('vrrtep:> '),sys.stdin.encoding).lower()
    while aword == "":
        aword = unicode(raw_input('vrrtep:> '),sys.stdin.encoding).lower()
    return aword

#make the questions not go in alpha order.
def listscramble(lyst):
    random.shuffle(lyst)
    return 

#scramble lists, play, and keep score.
def game():
    filename = os.path.join(os.path.dirname(sys.argv[0]), "naviwords.txt")
    wordfile = open(filename,"r")
    wordlist = []
    for line in wordfile:
        wordlist.append(line.strip())
    listscramble(wordlist)
    count=0.0
    correct = 0.0
    score=0

    # Irayo Kä'eng for the unicode fix :)
    # ~Swoka Ikran    
    for word in wordlist:
        os.system('cls')
        word,scr = scramble(word)
        word = unicode(word,"utf-8")
        print 'word: '+unicode(scr,"utf-8")+'\n'
        #print 'debug (answer): '+word+'\n'
        a = validate()
        anagram = False
        if a!= word and a!="/quit" and a!="/exit" and a!="/q" and a!="ans":
            ####anagram filter####
            # Windows support - Convert variable "a" back to UTF-8, since unicode() can't convert 
            # the list to UTF-16.
            if a.encode("utf-8") in wordlist and len(a) == len(word):
                for letter in list(a):
                    if letter not in list(word):
                        anagram = False
                        break
                    else:
                        anagram = True
                if anagram:
                    count += 1
                    correct = correct + 1
                    score = correct / count * 100
                    print'\nSrane! >:D','score:',int(correct),"/",int(count),"(",score,'% )\n'            
                    sleep(1.5)
            else:
                count += 1
                score = correct / count * 100
                print "\nKehe. :\\",'score:',int(correct),"/",int(count),"(",score,'% )'
                print "ans:",word
                sleep(2)
        if a == word:
            count += 1            
            correct = correct + 1
            score = correct / count * 100
            print'\nSrane! >:D','score:',int(correct),"/",int(count),"(",score,'% )\n'            
            sleep(1.5)
        elif a == "ans":
            count += 1
            score = correct / count * 100
            print "ans:",word
            print 'score:',int(correct),"/",int(count),"(",score,'% )\n'
            sleep(2)
        elif a == "/quit" or a == "/exit" or a == "/q":
            if count == 0:
                count += 1
            score = correct / count * 100
            break
        
    print 'score:',int(correct),"/",int(count),"(",score,'% )\n'
    saveHighScore(score,int(correct),int(count))
