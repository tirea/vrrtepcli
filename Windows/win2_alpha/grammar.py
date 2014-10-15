#!/usr/bin/python
# -*- coding: utf-8 -*-
#	Vrrtep CLI is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public Licence as published by
#	the Free Software Foundation, either version 3 of the Licence, or
#	(at your option) any later version.
#
#	Vrrtep CLI is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with Vrrtep CLI.  If not, see <http://www.gnu.org/licenses/>

#grammar.py is a lexical analyzer for Na'vi.
#it tells you whether your Na'vi sentence is 
#grammatically valid or not.

from root import *

import sys
DEBUG = False
if '-D' in sys.argv:
	DEBUG = True

#main analysis function
def analyze(sentence):#pass it sys.argv[2:]
	if DEBUG:
		print "<DEBUG:analyze>"
		print sentence
	wordcount = 1
	ptosArray = []
	print "words:"
	for word in sentence:
		if DEBUG:
			print word
		ptos = pos(word)
		ptosArray.append(ptos)
		if DEBUG:
			print ptosArray
			print "</DEBUG:analyze>"
		print "%-20s%-10s" % ('['+str(wordcount)+']POS='+ptos,'WORD='+word)
		wordcount += 1
	print
	clauses = breakIntoClauses(sentence)
	print "clauses:"
	for cl in clauses:
		print "%-20s" % ('[<='+str(cl)+']'),
		for c in clauses[cl]:
			print "%s" % c,
		print
		print
	if DEBUG:
		print "</DEBUG:analyze>"
	if 'e.' in ptosArray:
		print "INVALID: illegal word(s) used."
		sys.exit()
	if 'vtr.' in ptosArray:
		print "transitive validation:"
		cc = 1 #count
		for cl in clauses.values():
			print '['+str(cc)+']',
			parseTransitive(cl)
			cc += 1
		print
	if 'vin.' in ptosArray:
		cc = 1
		print "intransitive validation:"
		for cl in clauses.values():
			print '['+str(cc)+']',
			parseIntransitive(cl)
			cc += 1
		print
	if 'a' in sentence:
		print "attribution validation:"
		parseAttribution(sentence)
		print
	
#@return string
def pos(word):
	if DEBUG:
		print "<DEBUG:pos>"
	if 'b' in word:
		if DEBUG:
			print "has b"
		return 'e.'
	elif 'c' in word:
		if DEBUG:
			print "has c"
		return 'e.'
	elif 'd' in word:
		if DEBUG:
			print "has d"
		return 'e.'
	elif 'ng' not in word and 'g' in word:
		if DEBUG:
			print "has g"
		return 'e.'
	elif (('kx' not in word) and ('px' not in word) and ('tx' not in word)) and ('x' in word):
		if DEBUG:
			print "has x"
		return 'e.'
	elif 'q' in word:
		return 'e.'
	try:
		metaWords = open(os.path.join(os.path.dirname(sys.argv[0]), "metaWords.txt"),"r")
	except IOError:
		metaWords = open(raw_input("filepath of metaWords.txt? : "),"r")
	POS = "e."
	
	## This decoding is important!
        ## Removing it breaks Windows support for sentences with ä and ì in them.
        uin=word.decode(sys.stdin.encoding)
        uin=uin.encode("utf-8")
	for line in metaWords:
		## Changed word -> uin
		if '\t'+uin+'\t' in line:
			if DEBUG:
				print word,'\n'+line
			if "vin." in line:
				POS = "vin."
			elif "pn." in line:
				POS = "pn."
			elif "adv." in line:
				POS = "adv."
			elif "v." in line:
				POS = "v."
			elif "n." in line:
				POS = "n."
			elif "vim." in line:
				POS = "vim."
			elif "vtr." in line:
				POS = "vtr."
			elif "vtrm." in line:
				POS = "vtrm."
			elif "svin." in line:
				POS = "svin."
			elif "adj." in line:
				POS = "adj."
			elif "adp." in line:
				POS = "adp."
			elif "conj." in line:
				POS = "conj."
			elif "part." in line:
				POS = "part."
			elif "1788" in line:#hack for si
				POS = "aux. vin."
			elif "svin." in line:
				POS = "svin."
			elif "intj." in line:
				POS = "intj."
			elif "num." in line:
				POS = "num."
			break
	metaWords.close()
	if not exists(word):
		if DEBUG:
			print word
			print "</DEBUG:pos>"
			 
		if exists(antilenite(outfix(antiprefix(antisuffix(word)[0])[0])[0])[0]):
			return pos(antilenite(outfix(antiprefix(antisuffix(word)[0])[0])[0])[0]) # recursion win!
		else:
			if DEBUG:
				print "Non-afixed version of ",word,", ",antilen, " does not exist!"
	if DEBUG:
		print "</DEBUG:pos>"
	return POS

#@return dictionary					
def breakIntoClauses(sentence): #pass it an array
	sentence.append('$_end_$')
	conjunctions = ['fte','fteke','fu','slä','talun','taluna','taweyk','taweyka','tengfya','tengkrr']
	conjunctions.extend(['txo','txokefyaw','ulte','vaykrr','hufwa','tup','ftxey','alunta','fuke','alu','ki'])
	conjunctions.extend(['natkeneng','takrra','akrrta','mawkrra','akrrmaw','$_end_$'])#$_end_$ is a hack to get all clauses separated
	clauses = {}
	hasConj = False
	if DEBUG:
		print "<DEBUG:breakIntoClauses>"
		print sentence
		print conjunctions
		print hasConj
	for w in sentence:
		if w in conjunctions:
			hasConj = True
			break
		else:
			hasConj = False
	if DEBUG:
		print hasConj
	if not hasConj:
		clauses[0] = sentence
		if DEBUG:
			print sentence
			print clauses
			print "</DEBUG:breakIntoClauses>"
		return clauses
	tmp = 0
	for x in range(len(sentence)):
		if DEBUG:
			print "x=",x
			print "sentence[x]=",sentence[x]
		if sentence[x] in conjunctions:
			if DEBUG:
				print "pre-clauses:",clauses
			clauses.update({x:sentence[tmp:x]})
			if DEBUG:
				print "post-clauses:",clauses
			tmp = x
			if DEBUG:
				print "tmp=",tmp
				print "x=",x
	if DEBUG:
		print "</DEBUG:breakIntoClauses>"
	return clauses

#@print
def parseTransitive(clause): #pass it an array
	if DEBUG:
		print "<DEBUG:parseTransitive>"
	hasAgent = False
	hasPatient = False
	agentCount = 0
	patientCount = 0
	ptosArray = []
	#check that there is -l and -t are a pair
	for word in clause:
		if DEBUG:
			print "word in clause:",word
		ptosArray.append(pos(word))
		if DEBUG:
			print "ptosArray:",ptosArray
			print "pos("+word+"):",pos(word)
		wordpos = pos(word)
		if wordpos == 'n.' or wordpos == 'pn.':
			if word.endswith('l') and exists(word[0:-1]):
				hasAgent = True
				agentCount +=1
			elif word.endswith('ìl') and exists(word[0:-3]): #because ì is actually two characters in one
				hasAgent = True
				agentCount += 1
			elif word.endswith('ti') and exists(word[0:-2]):
				hasPatient = True
				patientCount += 1
			elif word.endswith('it') and exists(word[0:-2]):
				hasPatient = True
				patientCount += 1
			elif word.endswith('t') and exists(word[0:-1]):
				hasPatient = True
				patientCount += 1
			elif word == "futa" or word == "tsata" or word == "fayluta":
				hasPatient = True
				patientCount += 1
	if 'vtr.' not in ptosArray and 'vtrm.' not in ptosArray:
		print #do nothing
	else:
		print "clause has",agentCount,"agent(s) and",patientCount,"patient(s)"
		if 'vm.' in ptosArray or 'vtrm.' in ptosArray or 'vim.' in ptosArray: #if modal
			if hasAgent and hasPatient:
				print "valid."
			elif (not hasAgent) and hasPatient:
				print "valid."
			elif hasAgent and (not hasPatient):
				print "invalid: missing patient." 
			elif (not hasAgent) and (not hasPatient):
				print "invalid: missing agent; missing patient"
			print "verb/modal order validation:"
			modals = ['vm.','vtrm.','vim.']
			verbs = ['v.','vtr.','vin.','svin.']
			for modal in modals:
				for verb in verbs:
					if modal in ptosArray and verb in ptosArray:
						if ptosArray.index(verb) < ptosArray.index(modal):
							print "invalid: modal verb follows secondary"
		elif 'part.' in ptosArray: #hack for a and ma
			print "valid."
		else:
			if hasAgent and hasPatient:
				print "valid."
			if (not hasAgent) and hasPatient:
				print "invalid: missing agent."
			elif hasAgent and (not hasPatient):
				print "invalid: missing patient." 
			elif (not hasAgent) and (not hasPatient):
				print "invalid: missing agent; missing patient" 
	if DEBUG:
		print "</DEBUG:parseTransitive>"



#@print		
def parseIntransitive(clause): #pass array
	hasAgent = False
	hasPatient = False
	agentCount = 0
	patientCount = 0
	ptosArray = []
	#check that there is -l and -t are a pair
	for word in clause:
		ptosArray.append(pos(word))
		if pos(word) == 'n.':
			if word.endswith('l') and exists(word[0:-1]):
				hasAgent = True
				agentCount +=1
			elif word.endswith('ìl') and exists(word[0:-3]): #because ì is actually two characters in one
				hasAgent = True
				agentCount += 1
			elif word.endswith('ti') and exists(word[0:-2]):
				hasPatient = True
				patientCount += 1
			elif word.endswith('it') and exists(word[0:-2]):
				hasPatient = True
				patientCount += 1
			elif word.endswith('t') and exists(word[0:-1]):
				hasPatient = True
				patientCount += 1
	if agentCount + patientCount > 0 and 'a' not in clause:
		print "clause has",agentCount,"agent(s) and",patientCount,"patient(s) - SHOULD have NONE!"
	else:
		if 'vtr.' in ptosArray or 'vtrm.' in ptosArray:
			print #nothing
		else:
			print "valid."

#@print
def parseAttribution(sentence):
	#test if a attribution is to at least one noun
	if pos(sentence[sentence.index('a')-1]) == 'n.' or pos(sentence[sentence.index('a')+1]) == 'n.':
		print "valid."
	else:
		print "invalid: part. a not attributing to noun"			
