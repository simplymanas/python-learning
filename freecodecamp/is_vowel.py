# check if the char is a vowel

def is_vowel(char):
	vowels ={'a', 'e', 'i', 'o', 'u'}
	if char in vowels:
		return True
	return False



check = 's'

print(is_vowel(check))