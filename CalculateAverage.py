
# Variable arguments in python
# Manas Dash
# 13th July 2020
# is used to pass a variable number of arguments to a function.
# It is used to pass a non-keyworded, variable-length argument list.
# the correct order for your parameters is:
#   1. Standard arguments
#   2. *args arguments
#   3. **kwargs arguments
# now you read about this ** :)
# A quiz at the end with answer


def average(*args):
	return sum(args, 0.0) / len(args)


print (average(*[1, 2, 3]))
print (average(1, 2, 3))
print (average(1, 2))
print (average(1, 2), 'is the average')
print ('the average :', average(1, 2*5, 3.5, .4, 5^2, 6/2, 7>4, 8//2))

# output
# 2.0
# 2.0
# 1.5
# 1.5 is the average
# the average of 1 to 8 is : 4.5

# Question: Is there a limit to number og arguments that we can pass
# https://stackoverflow.com/questions/714475/what-is-a-maximum-number-of-arguments-in-a-python-function/714755#714755
