# looks like list but are immutable
# no accidental deletion

numbers = [1, 2, 3]
numbers = (1, 2, 3)
numbers[0] =3 # 'tuple' object does not support item assignment
