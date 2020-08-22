# Whole number to digits
# Writing whole numbers in expanded form
# 11th August 2020, Janmasthmai Day
# Manas Dash

whole_number = 16789

#  list comprehension
digits = [int(a) for a in str(whole_number)]
print(digits)

#  map
digits = list(map(int, str(whole_number)))
print(digits)

#  str function
digits = list(str(whole_number))
print(digits)

# which one is simpler or may be better?
print(ord(1))