# https://docs.python.org/2/reference/expressions.html#comparisons
# chain comparision in python
# Manas Dash
# Happy Ganesha (22nd aug 2020)
# Operator precedence : https://docs.python.org/2/reference/expressions.html#operator-precedence
# short-circuit operator https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not


strong = 5
stronger = 7
strongest = 9

print(strong > stronger > strongest)

print(strong < stronger < strongest > strong)

print(10 > strong <= 9)
print(5 == strong > 4)

# output
# False
# True
# True
# True
