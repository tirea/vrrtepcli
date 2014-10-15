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

#This file is a pile of hax.

#This file is responsible for stripping down words to their root form, for the
#sake of making Vrrtepcli translate normal sentences and multiple forms of words.

import os
import sys
DEBUG = False
if "-D" in sys.argv:
	DEBUG = True

#NA'VI


zeroinfixes = ['äp','eyk']
oneinfixes = ['iv','us','awn','am','ìm','ìyev','ol','ay','er','alm','ìlm','ìly','aly','arm','ìrm','ìry','ary','imv','iyev','ìy','ìsy','asy']
twoinfixes = ['ats','uy','eiy','äng','ei']
hack = ['irayo si','zerok','tswayon','pängkxo','eyk','oeyktìng','rol','tireapängkxo','kame','toltem','yafkeyk','tslam']
wordhas = []
def outfix(word):
	if DEBUG:
		print "<DEBUG:outfix>"
		print "word="+word
	if exists(word):
		if DEBUG:
			print "</DEBUG:outfix>"
		return word,[]
	if word == '':
		if DEBUG:
			print "</DEBUG:outfix>"
		return word, []
	if word in hack:
		if DEBUG:
			print word
			print "</DEBUG:outfix>"
		return word, []
	for infix in zeroinfixes:
		if infix in word:
			wordhas.append(infix)
			word = word.replace(infix,"",1)
			if word in hack:
				if DEBUG:
					print word
					print "</DEBUG:outfix>"
				return word,wordhas
	for infix in oneinfixes:
		if infix in word:
			wordhas.append(infix)
			word = word.replace(infix,"",1)
			if word in hack:
				if DEBUG:
					print word
					print "</DEBUG:outfix>"
				return word,wordhas
	for infix in twoinfixes:
		if infix in word:
			wordhas.append(infix)
			word = word.replace(infix,"")
			if word in hack:
				if DEBUG:
					print word
					print "</DEBUG:outfix>"
				return word,wordhas
			elif word == "pkxo" or word == "pkxängo":
				word = "pängkxo"
				if DEBUG:
					print word
					print "</DEBUG:outfix>"
				return word, wordhas
			elif word == "ptxe":
				word = "plltxe"
				if DEBUG:
					print word
					print "</DEBUG:outfix>"
				return word, wordhas
			elif word == "mte":
				word = "mllte"
				if DEBUG:
					print "</DEBUG:outfix>"
				return word, wordhas
			elif word == "tireapkxo" or word == "tireapkxängo":
				word = "tireapängkxo"
				if DEBUG:
					print word
					print "</DEBUG:outfix>"
				return word, wordhas
			elif word == "ke" or word == "keie" or word == "kame":
				if DEBUG:
					print word
				word = "kame"
				if "am" in wordhas:
					wordhas.remove('am')
				if DEBUG:
					print "</DEBUG:outfix>"
				return word, wordhas
			elif word == "ttem" or word == "ttolem":
				if DEBUG:
					print word
				word = "toltem"
				wordhas.remove('ol')
				if DEBUG:
					print "</DEBUG:outfix>"
				return word, wordhas
	if word == "ptxe":
		word = "plltxe"
		if DEBUG:
			print "</DEBUG:outfix>"
		return word, wordhas
	if word == "tse'":
		word = "tse'a"
		if DEBUG:
			print word
			print "</DEBUG:outfix>"
			return word, wordhas
	if word == "mte":
		word = "mllte"
		if DEBUG:
			print "</DEBUG:outfix>"
		return word, wordhas
	if word == "":
		word = "eyk"
		wordhas.remove('eyk')
		if DEBUG:
			print word
			print "</DEBUG:outfix>"
		return word, wordhas
	elif word == "'omum":
		word = "omum"
		if DEBUG:
			print "</DEBUG:outfix>"
		return word, wordhas
	elif word == "momum":
		word = "omum"
		wordhas.append('am')
		if DEBUG:
			print "</DEBUG:outfix>"
		return word, wordhas
	elif word == "iro si":
		word = "irayo si"
		wordhas.remove("ay")
		if DEBUG:
			print "</DEBUG:outfix>"
	elif word == "loae si":
		word = "leioae si"
		wordhas.remove("ei")
		if DEBUG:
			print "</DEBUG:outfix>"
	if DEBUG:
		print word
		print "</DEBUG:outfix>"
	return word,wordhas

prefixes = ['ay','a','me','pxe','fì','pe','tsay','tsa','fne','pay','fra','fay','tsuk','ketsuk','tì']
leniting = ['ay','me','pxe','pe','fay','tsay','pay']
prehack = ['ayoe','moe','ayoeng','awnga','tìkangkem si']
posthack = ['ayoel','ayoeti','ayoet','ayoeru','ayoer','ayoeyä','ayoey','ayoeri']
posthack.extend(['moel','moeti','moet','moeru','moer','moeyä','moey','moeri'])
posthack.extend(['ayoengal','ayoengati','ayoengat','ayoengaru','ayoengar','ayoengeyä','ayoengey','ayoengari'])
posthack.extend(['awngal','awngati','awngat','awngaru','awngar','awngeyä','awngey','awngari'])
trialhack = ['pxoe','pxoel','pxoeti','pxoet','pxoeru','pxoer','pxoeyä','pxoey','pxoeri']
trialhack.extend(['pxoeng','pxoengal','pxoengati','pxoengat','pxoengaru','pxoengar','pxoengeyä','pxoengey','pxoengari'])
trialhackfix = ['pxeoe','pxeoel','pxeoeti','pxeoet','pxeoeru','pxeoer','pxeoeyä','pxeoey','pxeoeri']
trialhackfix.extend(['pxeoeng','pxeoengal','pxeoengati','pxeoengat','pxeoengaru','pxeoengar','pxeoengeyä','pxeoengey','pxeoengari'])
def antiprefix(word):
	if DEBUG:
		print "<DEBUG:antiprefix>"
	if (word in posthack) or (word in prehack):
		if DEBUG:
			print "word="+word
		return word, []
	elif word in trialhack:
		word = trialhackfix[trialhack.index(word)]
		if DEBUG:
			print "word="+word
	if word == "peyä":
		return 'poyä',[]
	elif word == "tsari":
		return "tsawri",[]
	elif word.startswith("tìkangkem s"):
		t,s = word.split()
		return t+" "+s,[]
	lenites = False
	wordhas = []
	for prefix in prefixes:
		if DEBUG:
			print "in for, word=",word,";prefix="+prefix+";wordhas=",wordhas
		if word.startswith(prefix):
			if DEBUG:
				print "word="+word+";prefix="+prefix
			word = word.replace(prefix,'',1)
			temp,x = antilenite(prefix[-1]+word)
			if DEBUG:
				print "word=",word
				print "temp=",temp
				print "x=",x
			if exists(temp):
				word = temp
			wordhas.append(prefix)
			if prefix in leniting:
				lenites = True
			if DEBUG:
				print "returning (",word,",",wordhas,")"
			if exists(word):
				return word, wordhas
	if lenites:
		word,lenhas = antilenite(word)
		wordhas.extend(lenhas)
	if DEBUG:
		print "</DEBUG:antiprefix>"
	return word,wordhas
	
suffixes = ['ìlä','sì','ru','ur','r','ìl','l','vit','vi','ti','it','t','eyä','yä','ä','ìri','ri','tsyìp','yu','tu','fkeyk','pe',"nga'"]
adpos = ['äo','eo','io','uo','fa','ftu','hu','ka','fkip','kxamlä','lok','luke','maw','mìkam','mungwrr','ne','nemfa','pxaw','sìn','ta','takip','tafkip','kip	','teri','vay','to','na','pxel','al','a','to']
lenadpos = ['fpi','ìlä','mì','ro','sre','wä','o'] #ìlä was added to suffixes as a hack to avoid wordhas=['ìl','ä'], al is for ayoengal

def antisuffix(word):
	if DEBUG:
		print "<DEBUG:antisuffix>"
	if word.endswith("eltur"):
		return "eltu",['r']
	elif word.endswith("zìsìt"):
		return word,[]
	if exists(word):
		return word,[]
	wordhas = []
	suffixes.extend(adpos)
	suffixes.extend(lenadpos)
	if word.endswith("rr") or word.endswith("ll"):
		return word,wordhas
	for suffix in suffixes:
		if DEBUG:
			print "in for, suffix =",suffix
		if word.endswith(suffix):
			if len(suffix)==1:
				word = word[0:-1]
				if DEBUG:
					print "lensuf = 1, word =",word
			else:
				word = word.replace(suffix,'',1)
				if DEBUG:
					print "else, word =",word
			wordhas.append(suffix)
			if DEBUG:
				print "wordhas:",wordhas
			if suffix == "vit":
				if DEBUG:
					print "suffix is vit"
					print "word =",word
				word = word+"vi"
				if DEBUG:
					print "word =",word
				wordhas.remove('vit')
				if DEBUG:
					print "wordhas:",wordhas
				wordhas.extend(['vi','t'])
				if DEBUG:
					print "wordhas:",wordhas
				break
			elif suffix == "eyä":
				if DEBUG:
					print "suffix is eyä"
					print "word =",word
				if exists(word+"o"):
					word = word+"o"
				elif exists(word+"e"):
					word = word+"e"
				else:
					word = word+"a"
				wordhas.remove('eyä')
				wordhas.append('yä')
				break
		if len(word) == 1:
			word = word+suffix
		if exists(word):
			break
	if DEBUG:
		print "</DEBUG:antisuffix>"
	return word,wordhas

def exists(word):
	try:
		naviwords = open(os.path.join(os.path.dirname(sys.argv[0]), "naviwords.txt"),"r")
	except IOError:
	    naviwords = open(raw_input("filepath of naviwords.txt? : "),"r")

	for line in naviwords:
		if line.strip() == word:
			return True
	return False


lena = ['kx','px','tx','k','p','ts','t']
lenb = ['k','p','t','h','f','s','s']
vowel = ['a','ä','e','i','ì','o','u']
def antilenite(word):
	wordhas = []
	if exists(word):
		return word,wordhas
	for i in range(len(lena)):
		if word.startswith(lenb[i]):
			tmp = word.replace(lenb[i],lena[i],1)
			if exists(tmp):
				return tmp,wordhas
			temp,wordhas = antisuffix(tmp)
			if exists(temp):
				return temp,wordhas
				
	for v in vowel:
		if word.startswith(v):
			tmp = word.replace(v,"'"+v,1)
			if exists(tmp):
				return tmp, wordhas
			temp, wordhas = antisuffix(tmp)
			if exists(temp):
				return temp,wordhas
	return word,wordhas



#ENGLISH -- TODO
