#!/usr/bin/python
# -*- coding: utf-8 -*-
#    This file is part of Vrrtep CLI
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
import sys, os, random
from time import sleep, asctime
#this function saves the score and saves the high score
def saveHighScore(score,correct,count):
    
    #FILE IO
    saveFile = open(os.path.join(os.path.dirname(sys.argv[0]), "QUIZ_SCORES.txt"),"a")
    #save the quiz score
    saveFile.write(asctime()+" : "+str(score)+" "+str(correct)+"/"+str(count)+"\n")
    saveFile.close()
    
    saveFile = open(os.path.join(os.path.dirname(sys.argv[0]), "QUIZ_SCORES.txt"),"r")
    highScoresFile = open(os.path.join(os.path.dirname(sys.argv[0]), "QUIZ_HIGH_SCORE.txt"),"w")
    
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
    highScoresFile.write("Quiz High Score: "+str(highScore)+"\n")
    print "Quiz High Score: "+str(highScore)

#get valid integer in a certain range
def getValidInt(question, minimum, maximum):

    # use a bad value to enter the loop
    value = maximum + 1

    # compose the prompt
    prompt = question + "[" + str(minimum) + "-" + str(maximum) + "]:> "

    # continue to get values until the user enters a valid one
    try:
        while value == "" or value < minimum or value > maximum:
            value = raw_input(prompt)
            if len(value) != 0:
                try:
                    value = int(value)
                except ValueError:
                    pass
        return value
    except EOFError:
        print
        sys.exit()
    except KeyboardInterrupt:
        print
        sys.exit()
        
#####################################        
#rid chance of duplicate quiz OPTIONS
#original Autoit code by Swoka Ikran
def ValidateAnswers(answer):
    for x in range(1,3):
        for y in range(1,3):
            if x == y:
                continue # Prevent checking the answer against itself.
            if answer[x] == answer[y]:
                return False #Reject them since we have duplicates
    return True #They're acceptable, use them.
#####################################

def GetNewAnswers(fileb):
    infile2 = os.path.join(os.path.dirname(sys.argv[0]), fileb)
    file2 = open(infile2, 'r')
    f2content = file2.readlines()
    
    #set up options
    ONE=random.randint(0, len(f2content)-1)
    TWO=random.randint(0, len(f2content)-1)
    THREE=random.randint(0, len(f2content)-1)
    options = [ONE,TWO,THREE]
    
    return options

def quiz(filea,fileb):
    #FILE IO
    infile1 = os.path.join(os.path.dirname(sys.argv[0]), filea)
    infile2 = os.path.join(os.path.dirname(sys.argv[0]), fileb)
    file1 = open(infile1, 'r')
    file2 = open(infile2, 'r')
    
    f1content = file1.readlines()
    f2content = file2.readlines()
    
    count = 0.0
    correct = 0.0
    score = 0
    while count < len(f1content):
        os.system('clear')
    
        wordnum = random.randint(0, len(f1content)-1)
   
        print 'Word:', f1content[wordnum], ''
        
        ####################################
        #choose answers, returns a list with indices 1,2,3 as answers
        #original Autoit code by Swoka Ikran#
        options = GetNewAnswers(fileb)
        while not ValidateAnswers(options):
            options = GetNewAnswers(fileb)
        #####################################
            
        #randomly decide which option is the answer
        options[random.randint(0, 2)] = wordnum
        
        print '1 -', f2content[options[0]],
        print '2 -', f2content[options[1]],
        print '3 -', f2content[options[2]]

        answer = getValidInt('vrrtep',1,5)
    
        if answer == 4:
            count += 1
            score = correct / count * 100
            print 'ans:',f2content[wordnum],
            print 'score:',int(correct),"/",int(count),"(",score,'% )\n'
            sleep(2)
        elif answer == 5:
            if count == 0:
                count = count + 1
            score = correct / count * 100
            break
        elif options[answer-1] == wordnum:
            count += 1
            correct = correct + 1
            score = correct / count * 100
            print'\nSrane! >:D','score:',int(correct),"/",int(count),"(",score,'% )\n'
            sleep(1.5)
        else:
            count += 1
            score = correct / count * 100
            print "\nKehe. >:\\ ",'score:',int(correct),"/",int(count),"(",score,'% )'
            print 'ans:',f2content[wordnum]
            sleep(2)
    print 'score:',int(correct),"/",int(count),"(",score,'% )\n'
    
    saveHighScore(score,int(correct),int(count))
#quiz("naviwords.txt","eng.txt")