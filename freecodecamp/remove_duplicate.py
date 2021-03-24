# remove duplicate character froma  set
# input: "aabbccd"
# output : "abcd"

# using list
def remove_duplicate(input_string):
	if input_string is None:
		return f"its an empty string"

	visited = []
	for input_char in input_string:
		if not visited.__contains__(input_char):
			visited.append(input_char)
	return visited


# using set

def remove_duplicate_set(input_string):
	visited = set()
	output_string = ''

	for char in input_string:
		if char not in visited:
			visited.add(char)
			output_string += char
	return output_string


my_string = "manas"

print(remove_duplicate(my_string))
print(remove_duplicate_set(my_string))
