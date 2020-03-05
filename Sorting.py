# Sorting python dictionary by value
import operator

dictToSort = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
# sorted(dictToSort.items(), key=lambda x: x[1])
# print(sorted(dictToSort.items(), key=lambda x: x[1]))


print(sorted(dictToSort.items(), key=operator.itemgetter(1)))


