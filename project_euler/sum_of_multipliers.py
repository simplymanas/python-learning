# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

sum_of_multipliers = 0
multipliers_of_3 = []
multipliers_of_5 = []

for x in range(1000):
	if x % 3 == 0 or x % 5 == 0:
		sum_of_multipliers += x

print(sum_of_multipliers)
print(sum(n for n in range(1, 1000) if (n % 3 == 0 or n % 5 == 0)))
