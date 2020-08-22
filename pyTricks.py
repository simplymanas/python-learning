# trick1
# ##merge two dictionaries in python 3
#
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'x': 5, 'y': 6}
#
# z = {**dict1, **dict2}
# print(z)


# trick2
# test multiple flag at once

# x, y, z = 0, 1, 0
# #
# # if x == 1 or y == 1 or z == 1:
# #     print('passed')
# #
# # if 1 in (x, y, z):
# #     print('passed')
# #
# # ## test true
# #
# # if x or y or z:
# #     print('passed')
# #
# # if any((x, y, z)):
# #     print('passed')

# trick 3
# # Print even number within a range of 20
#
# evens = [x for x in range(20) if x % 2 == 0]
# print(evens)
#
# # lambda functions
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
# def square(n):
#     return n ** n
#
#
# squares = list(map(lambda x: x ** 2, numbers))
# print(squares)


# # trick 4
#
# # swapping variables
# a = 5
# b = 6
#
# a, b = b, a
#
# print(a, b)
#
#
# # how to sort a python dictionary
#
# dict
#
#

# Manas Dash
# 16th July 2020
# Get the size in bytes
# Returns the length of a string in bytes.
# utf-8 encodes a given string and find its length.
#
# def size_in_bytes(string):
# 	return len(string.encode('utf-8'))
#
# # a smily cost how much
# print (size_in_bytes('😀'))  # 4 byte
#
# # techster took 8 bytes
# print (size_in_bytes('techster'))
#
# # and a new line character
# print (size_in_bytes('\n'))  # 1
#
# # my byte size is
# print (size_in_bytes('manas'))  # 5
#
# # What's your size in bytes 😀


# Manas Dash
# 20th July 2020
# Check if a list contains all unique element

# def all_unique(input_list):
# 	return len(input_list) == len(set(input_list))
#
#
# x = [11, 13, 14, 15, 16, 18]
# y = [11, 13, 14, 15, 16, 18, 11]
#
#
# print(all_unique(x))  # True
# print(all_unique(y))  # False


# multiple inputs

# x, y = input('numbers').split()
# print(x,y)

#
# # which number is repeated most number of time
#
# numbers = [1, 3, 4, 6, 3, 7, 3, 8, 6, 5, 9, 5, 3, 6, 3, 2, 3]
#
# max_repeated = max(set(numbers), key=numbers.count)
#
# print(f"The number {max_repeated} is repeated maximum number of time in the given list")
#
# # even number of square
# # list comprehension
#
# even_squares = [i ** 2 for i in range(20) if i % 2 == 1]
# print(even_squares)
#

# a = int(input())
# print('Multiple of 5', 'Not a Multiple of 5')[a % 5 == 0]
#
# Loader = "Loading";
# count = 5
# print(Loader)
# while count != 0:
# 	import time
#
# 	print(".")
# 	count -= 1
# 	time.sleep(0.3)

# # Ways to print square and cube
# # 27th july 2020
# # Manas Dash
#
# print('1st way')
# for x in range(1, 11):
# 	print(repr(x).rjust(2), repr(x * x).rjust(3), repr(x * x * x).rjust(4))
#
# print('2nd way')
# for x in range(1, 11):
# 	print("%2d %3d %4d" % (x, x * x, x * x * x))
#
# '''
# Output
# 1st way
#  1   1    1
#  2   4    8
#  3   9   27
#  4  16   64
#  5  25  125
#  6  36  216
#  7  49  343
#  8  64  512
#  9  81  729
# 10 100 1000
# 2nd way
#  1   1    1
#  2   4    8
#  3   9   27
#  4  16   64
#  5  25  125
#  6  36  216
#  7  49  343
#  8  64  512
#  9  81  729
# 10 100 1000'''

#
# def test():
#     """Stupid test function"""
#     L = [i for i in range(100)]
#
# if __name__ == '__main__':
#     import timeit
#     print(timeit.timeit("test()", setup="from __main__ import test"))


# print emojis
# you can import emoji as a library as well
# but try without the libraries
# Manas Dash
# 14th August 2020

print("\U0001f600")
print("\u2665")
print("\N{Black heart suit}")
print("\N{grinning face}")
print("\N{slightly smiling face}")
print("\N{Beating heart}")
print("\N{thinking face}")
print("\N{zipper-mouth face}")
print("\N{face with head-bandage}")
