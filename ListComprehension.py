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
# print([vegetable['name'] for vegetable in vegetables if vegetable['name'][0] == 'P'])['Potato', 'Pumpkin']

# ['Potato', 'Pumpkin']

# this applies to dictionary as well

squares = []

# for i in range(10):
# 	squares.append(i * i)

#list comprehension
squares = [i * i for i in range(10)]

print(squares)


# apply function to a list
prices = [1.7, 11.89, 23.99, 22.56]
tax_rate = 0.08


# def get_price_with_tax(price):
# 	return price + (1 * tax_rate)

# result = map(get_price_with_tax, prices)

#list comprehension
result = [price + (1 * tax_rate) for price in prices]

print(list(result))

# list consonant and vowel in a string

def is_consonant(string):
	vowels ='aeiou'
	return string.isalpha() and string.lower() in vowels


string = "the aaaa bronw fox"
print([ch for ch in string if is_consonant(ch)])
print([ch for ch in string if not is_consonant(ch) and ch is not ' '])

