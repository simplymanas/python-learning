# Manas Dash
# 24th July 2020
# the usage of set and max function
# which number is repeated most number of time

numbers = [1, 3, 4, 6, 3, 7, 3, 8, 6, 5, 9, 5, 3, 6, 3, 2, 3]

max_repeated = max(set(numbers), key=numbers.count)

print(f"The number {max_repeated} is repeated maximum number of time in the given list")

# The number 3 is repeated maximum number of time in the given list
