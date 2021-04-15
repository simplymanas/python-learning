# Largest prime factor
#
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

input_number = 10


def is_prime(the_number):
	for n in range(2, the_number):
		if the_number % n == 0:
			return False
	return True


for number in range(2, input_number):
	if is_prime(number):
		if input_number % number == 0:
			print(number)

