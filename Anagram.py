

# 9th July 2020
# Manas Dash
# Calculating permutations
# using itertools
# This itertools module implements a number of iterator
# building blocks inspired by constructs from APL, Haskell, and SML.
# also look at the join method

import itertools
from nltk.corpus import wordnet

for p in itertools.permutations(['c', 'a', 'r', 'e']):
	# print (''.join(str(x) for x in p))
	word = ''.join(str(x) for x in p)
	if not (wordnet.synsets(word)):
		print (word, 'is Not a word')
	else:
		print (word, 'is a English word')


# # Output
# care is a English word
# caer is Not a word
# crae is Not a word
# crea is Not a word
# cear is Not a word
# cera is Not a word
# acre is a English word
# acer is a English word
# arce is Not a word
# arec is Not a word
# aecr is Not a word
# aerc is Not a word
# rcae is Not a word
# rcea is Not a word
# race is a English word
# raec is Not a word
# reca is Not a word
# reac is Not a word
# ecar is Not a word
# ecra is Not a word
# eacr is Not a word
# earc is Not a word
# erca is Not a word
# erac is Not a word