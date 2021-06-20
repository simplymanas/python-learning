# Even Fibonacci numbers
# Problem 2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


def fibonacci(n):
	first = second = 1
	sum_of_even = 0

	for i in range(n):
		if first > 4000000:
			return
		yield first
		if (first % 2 == 0):
			sum_of_even += first
		first, second = second, first + second
	return sum_of_even


for num in fibonacci(1000):
	print(num)