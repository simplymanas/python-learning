def intersect_list(firstList, secondList):
	result, secondList_copy = [], secondList[:]
	for element in firstList:
		if (element in secondList_copy):
			result.append(element)
			secondList_copy.remove(element)
	return result

print(intersect_list([1,2,3,4,5],[8,9,7,3,0]))




