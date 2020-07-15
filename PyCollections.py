# Manas Dash
# 15th July 2020
# collections — Container datatypes
# This module implements specialized container datatypes providing
# alternatives to Python’s general purpose built-in containers, dict, list, set, and tuple.
# A Counter is a dict subclass for counting hashable objects.
# It is a collection where elements are stored as dictionary keys
# and their counts are stored as dictionary values.
# https://docs.python.org/3/library/collections.html


# find out how many times a letter is repeated in a sentence
from collections import Counter
mouse = Counter("Manually Operated Utility Selection Equipment")
print(mouse)

# output
# Counter({'e': 5, 't': 5, 'l': 4, ' ': 4, 'i': 4, 'a': 3, 'n': 3, 'u': 2, 'y': 2, 'p': 2, 'M': 1,
# 'O': 1, 'r': 1, 'd': 1, 'U': 1, 'S': 1, 'c': 1, 'o': 1, 'E': 1, 'q': 1, 'm': 1})