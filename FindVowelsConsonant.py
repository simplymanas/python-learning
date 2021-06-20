def is_consonant(string):
	vowels = 'aeiou'
	return string.isalpha() and string.lower() in vowels


string = "the aaaa bronw fox"
print([ch for ch in string if is_consonant(ch)])
print([ch for ch in string if not is_consonant(ch) and ch is not ' '])

