# remove charcter if backspace is there
# A < b < C
# output C

def remove_backspace(input):
	stack = []
	for char in input:
		if char != '<':
			stack.append(char)
		else:
			stack.pop()
	return stack


thestack = 'a<b<cdddd'

print(remove_backspace(thestack))
