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


# trick 4

# swapping variables
a = 5
b = 6

a, b = b, a

print(a, b)


# how to sort a python dictionary

dict
