# remove duplicate character froma  set
# input: "aabbccd"
# output : "abcd"


def remove_duplicate(input_string):
	if input_string is None:
		return f"its an empty string"

	visited = []
	for input_char in input_string:
		if not visited.__contains__(input_char):
			visited.append(input_char)
	return visited


my_string = "aabbccd"

print(remove_duplicate(my_string))