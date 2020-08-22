
# fibonacci using yield : (29th june 2020)
# The yield keyword in Python is used to create generators.
# A generator is a type of collection that produces items on-the-fly and
# can only be iterated once. By using generators you can improve your
# application's performance and consume less memory as compared to normal collections,
# so it provides a nice boost in performance.
# The Rule for fibonacci is xn = xn−1 + xn−2


def fibonacci(n):
	first = second = 1
	for i in range(n):
		yield first
		first, second = second, first + second


for num in fibonacci(100):
	print(num)


