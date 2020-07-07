
# 7th july 2020
# Manas Dash
# else with for loop
# the below else: belongs to the for loop
# for loop’s else clause runs when no break occurs

# Prime number test
for n in range(2, 8):
	for x in range(2, n):
		if n % x == 0:
			print (n, ' = ', x, '*', n // x, ', hence', n, 'is not prime')
			break
	else:
		# no factor found
		print (n, 'is a prime number')
