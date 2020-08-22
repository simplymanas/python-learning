# 6th July 2020
# Manas Dash
# list comprehension
#   List comprehensions provide a concise way to create lists.
#   Common applications are to make new lists where each element is the result of
#   some operations applied to each member of another sequence or iterable,
#   or to create a subsequence of those elements that satisfy a certain condition.
# source: https://docs.python.org/3/tutorial/datastructures.html

# list comprehension
vegetables = [
	{'name': 'Potato', 'price': 40},
	{'name': 'Tomato', 'price': 20},
	{'name': 'Onion', 'price': 25},
	{'name': 'Pumpkin', 'price': 45}
]

# Regular way
vegetable_names = []

for vegetable in vegetables:
	vegetable_names.append(vegetable['name'])

print(vegetable_names)  # ['Potato', 'Tomato', 'Onion', 'Pumpkin']

# list comprehension
print([vegetable['name'] for vegetable in vegetables])  # ['Potato', 'Tomato', 'Onion', 'Pumpkin']

# adding a condition
print([vegetable['name'] for vegetable in vegetables if vegetable['name'][0] == 'P'])['Potato', 'Pumpkin']

# ['Potato', 'Pumpkin']

# this applies to dictionary as well
