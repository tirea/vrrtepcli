# -*- coding: utf-8 -*- 
#!/usr/bin/python
#
#    This file is part of VrrtepCLI.
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
#This module is both a rhyme searcher and txt/html rhyming dictionary generator
import os, sys
#comment out next line for generator
def navRhyme(word):
#un-comment next line for generator
#def main():
	infilename = os.path.join(os.path.dirname(sys.argv[0]), "naviwords.txt")
	infile = open(infilename,"r")
	rhymdict = {}
	endings = [
		'a', 'ap', 'äp', 'ar', 'at', 'aw', 'ay', 'ä', 'ak', 'awk',
		'awkx', 'akx', 'awl', 'al', 'am', 'awm', 'awn', 'an', 'awng',
		'ang', 'a\'', 'e', 'en', 'eng', 'ep', 'er', 'ey', 'et', 'eyk',
		'ew', 'eyng', 'ewk', 'eyp', 'e\'', 'ek', 'ekx', 'el', 'em', 'i',
		'ì', 'ik', 'ìk', 'ikx', 'il', 'ìl', 'im', 'ìm', 'ìn', 'in',
		'ìng', 'ip', 'ìp', 'ir', 'it', 'ìt', 'll', 'o', 'ok', 'okx',
		'ol', 'om', 'on', 'ong', 'op', 'or', 'otx', 'o\'', 'rr', 'u',
		'uk', 'ul', 'um', 'un', 'ung', 'up', 'ur', 'ut', 'utx',
	]

	for ending in endings:
		rhymdict[ending] = []
	
	for line in infile:
		for ending in endings:
			if line.strip()[-len(ending):] == ending:
				rhymdict[ending].append(line.strip())
	
#comment out next 15 lines for generator.
	if len(word) != 0:
		if word[-1] in rhymdict:
			for rhyme in rhymdict[word[-1]]:
				print unicode(rhyme,"utf-8")+",",
		elif word[-5:] in rhymdict:
			for rhyme in rhymdict[word[-5:]]:
				print unicode(rhyme,"utf-8")+",",
		elif word[-4:] in rhymdict:
			for rhyme in rhymdict[word[-4:]]:
				print unicode(rhyme,"utf-8")+",",
		elif word[-3:] in rhymdict:
			for rhyme in rhymdict[word[-3:]]:
				print unicode(rhyme,"utf-8")+",",
		elif word[-2:] in rhymdict:
			for rhyme in rhymdict[word[-2:]]:
				print unicode(rhyme,"utf-8")+",",
	else:
		pass
#####--GENERATOR--######
#uncomment all following necessary lines to use the generator.
#	print """
#
#<html> 
#<head> 
#<meta http-equiv="content-type" content="text/html; charset=utf-8" /> 
#</head> 
#<body> 
#<h1>Na'vi Rhyming Dictionary</h1> 
#<h3>Based on Na'vi Dictionary v.11.863</h3> 
#<h4>Compiled by Tirea Aean on 18 May 2011</h4> 
#<hr> 
#*This dictionary's entries are not in alphabetical order...yet*<br>
#*Note that MANY more rhymes are possible with using suffixes and enclitic adpositions.*<br>
#<br> 
#>Use the Find function with Ctrl+F to search the page.<br> 
#>It is most useful to search for some specific heading such as em: or u:<br> 
#>It may also be very helpful if you are searching for the rhymes of a specific<br> 
#>>>word, to search the word with a comma attached after it.<br> 
#<hr> 
#<br> 
#"""
#	for i in range(len(rhymdict)): #required uncomment
#		print #required uncomment
		#for html
#		print '<br>'
		#for txt
#		print rhymdict.keys()[i]+':\n'
		#for html
#		print rhymdict.keys()[i]+':<br><br>'
#		for val in rhymdict.values()[i]: #required uncomment
#			print val+',',  #requred uncomment
		#for txt
#		print '\n\n'
		#for html
#		print '<br><br>'
	infile.close()
#un-commnet for generator
#main()
