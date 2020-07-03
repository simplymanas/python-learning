# 1st July 2020
# Transpose a matrix
# also How ZIP behaves

# In Python3, zip method returns a zip object instead of a list.
# This zip object is an iterator. Iterators are lazily evaluated. (text is copied from the Internet)
# We convert the zip object to a list by list(zipped). After this, we can use all the methods of list.
# Iterators can be evaluated only one time. and then they get tired 😢
# They get exhausted, so once_more_as_list output is an empty list.

# Lets define a list
import itertools

a_list = [[1, 2], [3, 4], [5, 6]]

# to transpose it we are using zip()
after_zip = zip(*a_list)

# converting to a list object
output_as_list = list(after_zip)
# output_as_list = list(itertools.tee(after_zip))

# converting again and magic begins
once_more_as_list = list(after_zip)

print(output_as_list)  # output : [(1, 3, 5), (2, 4, 6)]

print(once_more_as_list)  # output : []
print(output_as_list)  # output : [(1, 3, 5), (2, 4, 6)]


