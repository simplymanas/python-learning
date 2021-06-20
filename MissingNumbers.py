def get_missing_number(listOfNumbers):
	print(len(listOfNumbers))
	print(range(listOfNumbers[len(listOfNumbers)-1])[1:])
	# print(set(range(listOfNumbers[len(listOfNumbers)-1])[1:]))
	return set(range(listOfNumbers[len(listOfNumbers)-1])[1:]) - set(listOfNumbers)


l = list(range(1, 100))
l.remove(50)
print(get_missing_number(l))
l.remove(51)
print(get_missing_number(l))
l.remove(52)
l.remove(53)
l.remove(58)
l.remove(59)

print(get_missing_number(l))