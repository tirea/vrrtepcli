#!/usr/bin/python
# -*- coding: utf-8 -*-
#	 This file is part of VrrtepCLI.
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

import os, sys

def navRhyme(word):

	#create rhyme dictionary during runtime
	infilename = os.path.join(os.path.dirname(sys.argv[0]), "naviwords.txt")
	infile = open(infilename,"r")
	rhymdict = {}
	endings = [
	'a',"a'",'aw',"aw'",'ay',"ay'",'ä',"ä'",'e',"e'",'ew',"ew'",'ey',"ey'",'i',"i'",'ì',"ì'",'o',"o'",'u',"u'",
	'ak','akx','al','am','an','ang','ap','apx','ar','at','atx',
	'awk','awkx','awl','awm','awn','awng','awp','awpx','awr','awt','awtx',
	'ayk','aykx','ayl','aym','ayn','ayng','ayp','aypx','ayr','ayt','aytx',
	'äk','äkx','äl','äm','än','äng','äp','äpx','är','ät','ätx',
	'ek','ekx','el','em','en','eng','ep','epx','er','et','etx',
	'ewk','ewkx','ewl','ewm','ewn','ewng','ewp','ewpx','ewr','ewt','ewtx',
	'eyk','eykx','eyl','eym','eyn','eyng','eyp','eypx','eyr','eyt','eytx',
	'ik','ikx','il','im','in','ing','ip','ipx','ir','it','itx',
	'ìk','ìkx','ìl','ìm','ìn','ìng','ìp','ìpx','ìr','ìt','ìtx',
	'ok','okx','ol','om','on','ong','op','opx','or','ot','otx',
	'uk','ukx','ul','um','un','ung','up','upx','ur','ut','utx',
	]
	for ending in endings:
		rhymdict[ending] = []
	
	for line in infile:
		for ending in endings:
			if line.strip()[-len(ending):] == ending:
				rhymdict[ending].append(line.strip())
	
	#print out rhymes for given word
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

	infile.close()
