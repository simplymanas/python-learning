# Most frequntly occuring item in an array
# [1,3,1,3,2,1,2,2,2] is 1

def most_frequent(given_list):
	max_item = None
	max_count = 0
	mf_dict = {}
	for item in given_list:
		mf_dict[item] = mf_dict.get(item,0) + 1
		if max_count < mf_dict.get(item,0) + 1:
			max_item = item
			max_count = mf_dict.get(item,0) + 1
	return max_item

list1 = [1,3,3,3,3,1,3,2,1,2,2,2]
print (most_frequent(list1))


# NOTE: The following input values will be used  for testing your solution.
# most_frequent(list1) should return 1
list11 = [1, 3, 1, 3, 2, 1]
print (most_frequent(list11))
# most_frequent(list2) should return 3
list2 = [3, 3, 1, 3, 2, 1]
print (most_frequent(list2))
# most_frequent(list3) should return None
list3 = []
print (most_frequent(list3))
# most_frequent(list4) should return 0
list4 = [0]
print (most_frequent(list4))
# most_frequent(list5) should return -1
list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]
print (most_frequent(list5))