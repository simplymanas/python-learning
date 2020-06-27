
# Date: 27th Jun 2020
# Lets learn Set Theory in Python
# Few Operations on Sets

# Let's take two sets
first_set = {11, 21, 31, 41, 51}
second_set = {11, 61, 71, 81, 31}

print('First Set  : ' + str(first_set))
print('Second Set : ' + str(second_set))

# The  basic operations are:

# 1. Union of Sets
print('\nUNION of the two sets are (Both in first and second)')
print(set(first_set) | set(second_set))

# inbuilt function
print(first_set.union(second_set))

# 2. Intersection of sets
print('\nIntersection of the two sets are (common to both)')
print(set(first_set) & set(second_set))

# inbuilt function
print(first_set.intersection(second_set))

# 3. Difference of two sets
print('\nDifference of the two sets are (in first but not in second) ')
print(set(first_set) - set(second_set))

# inbuilt function
print(first_set.difference(second_set))

# 4. Symmetric difference of two sets
print('\nSymmetric Difference of the two sets are (excluding the common element of both) ')
print(set(first_set) ^ set(second_set))

# inbuilt function
print(first_set.symmetric_difference(second_set))

print()