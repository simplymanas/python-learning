# Membership testing
# Performance  check using TIC-TOC
# Manas Dash , 8th jul 2020
# The operators in and not in test for membership. x in s evaluates to True
# if x is a member of s, and False otherwise. x not in s returns the negation of x in s.
from pytictoc import TicToc


def check_number(element, elements):
	for item in elements:
		if item == element:
			return True
	return False


numbers = [1, 2, 3, 0, 4, 5]

# this way
print('\nUsing function and finding from list', numbers)
t = TicToc()
t.tic()
print(check_number(2, numbers))  # True
print(check_number(22, numbers))  # False
t.toc()

# or this way using membership testing
print('\nUsing membership testing and finding from list', numbers)
t = TicToc()
t.tic()
print(2 in numbers)  # True
print(22 in numbers)  # False
t.toc()

# Output
# Using function and finding from list [1, 2, 3, 0, 4, 5]
# True
# False
# Elapsed time is 0.000012 seconds.
#
# Using membership testing and finding from list [1, 2, 3, 0, 4, 5]
# True
# False
# Elapsed time is 0.000006 seconds
