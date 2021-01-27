numbers = [9, 9, 9, 8]

print(numbers)


def add_one(numbers):
	carry = 1
	ctr = len(numbers) - 1
	result = []

	for num in numbers[::-1]:
		print(f"num {num}")
		total = num + carry
		print(f"total {total}")
		if total == 10:
			carry = 1
			result.append(total % 10)
		else:
			carry = 0
			result.append(total % 10)
			ctr = ctr - 1
			print(f"result {result}")
	if carry == 1:
		result.insert(0, 1)
	return result


print(add_one(numbers))
