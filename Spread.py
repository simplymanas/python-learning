# spread
# Manas Dash
# 24th aug 2020
# Implements javascript's [].concat(...arr). Flattens the list(non-deep) and returns a list.

def spread(arg):
	ret = []
	for i in arg:
		if isinstance(i, list):
			ret.extend(i)
		else:
			ret.append(i)
	return ret


print(spread([1, 2, 3, [4, 5, 6], [7], 8, 9]))
print(spread(['The', 'quick', 'brown', ['fox', 'jumps', 'over'], ['the'], 'lazy', 'dog']))


# Output
# [1,2,3,4,5,6,7,8,9]
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
