#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

# {"affix":position}
# (must be unicode not str so len() on them isn't screwed up)
infixes = {
	u"äp":0,
	u"eyk":0,

	u"us":1,
	u"awn":1,
	u"asy":1,
	u"ìsy":1,
	u"ay":1,
	u"ìy":1,
	u"er":1,
	u"ìm":1,
	u"am":1,
	u"ol":1,
	u"iv":1,
	u"aly":1,
	u"ary":1,
	u"ìly":1,
	u"ìry":1,
	u"ìrm":1,
	u"ìlm":1,
	u"arm":1,
	u"alm":1,
	u"ìyev":1,
	u"imv":1,
	u"irv":1,
	u"ilv":1,
	
	u"ei":2,
	u"äng":2,
	u"uy":2,
	u"ats":2
}
# There are more aren't there?

vowels = [u"ll", u"a", u"e", u"i", u"rr", u"o", u"u", u"ä"] # ay, aw, ew & ey will be picked up with a & e

def rif(word, infix, monosyllabic, position=0):
	"""
	rif (recursive infix finder)
	word = str. the word in question
	infix = str. infix to find..?
	monosyllabic = bool. Is the word monosyllabic (shifts pos 2.)
	position = int. 1 or 2 (0 is irrelivent for this)
	"""
	if len(word) <= len(infix):
		return False
	
	
	if word[:len(infix)] == infix and word[len(infix)] in vowels:
		if (position > 0 and infixes[infix] == position and not monosyllabic) \
			or (position < 2 and infixes[infix] < 2 and not monosyllabic) \
			or monosyllabic:
			
			return infix
			
	
	for i in range(3, 1, -1):
		if word[:i] in infix and word[3] in vowels:
			if position < 1:
				position += 1
			return rif(word[i:], infix, monosyllabic, position)
	if word[0] in vowels:
		position += 1

	return rif(word[1:], infix, monosyllabic, position)
	
def vc(word, count=0):
	"""
	Counts the vowels in the word
	word = str. the word you wish to count the vowels in
	count = int. (don't set), it's the amount of vowels
	"""	
	for vowel in vowels:
		if len(vowel) <= len(word) and word[:len(vowel)] == vowel:
			count += 1
			break
	if len(word) <= 1:
		return count
	return vc(word[1:], count)
	
def si(word):
	"""
	Strips the infixes so the vowels can be counted correctly
	word = str. word for infixes to be stripped from
	"""
	# ugh must do the longst ones first
	infix_sorted = [[], [], [], []] # length of infix: 1, 2, 3 (Chars)
	for infix in infixes:
		infix_sorted[len(infix)-1].append(infix)
	for i in range(len(infix_sorted)-1, -1, -1):
		for infix in infix_sorted[i]:
			word = word.replace(infix, "")
	return word
	
if __name__ == "__main__":
	if len(sys.argv) <= 1:
		print "You didn't enter a word?"
		sys.exit()
	
	word = sys.argv[1].decode("utf-8")
	affixes = []
	monosyllabic = vc(si(word)) <= 1 # Is it monosyllabic?
	for infix in infixes:
		if rif(word, infix, monosyllabic):
			affixes.append(infix)
	if affixes:
		print "Affixs: %s" % " ".join(affixes)
	else:
		print "No infixes found"
