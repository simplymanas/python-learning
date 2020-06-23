## approach 1
#
# def find_first_duplicate(arr):
#     for index in range(0, len(arr)):
#         for duplicateIndex in range(index + 1, len(arr)):
#             if arr[index] == arr[duplicateIndex]:
#                 print(arr[duplicateIndex])
#
#
#
#
#
# ## approach 2
#
# def find_first_duplicate(arr):
#     lambda arr:arr[map(arr.remove, set(arr))<0]
#

#
# approch 3
def find_first_duplicate(arr):
    seen = set()
    for i in arr:
        if i in seen:
            return i
        seen.add(i)
    return -1



# approach 4

def find_first_duplicate(arr):
    unique_values = set()

    for element in arr:
        if element in unique_values:
            return element
        else:
            unique_values.add(element)
    return -1

## run rabit run

print(find_first_duplicate([1, 2, 3, 4, 5, 3, 2, 4, 5, 6]))