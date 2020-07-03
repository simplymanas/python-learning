# 3rd July 2020 Manas Dash
# remove duplicate elements from a list


list_with_duplicates = [23, 45, 23, 12, 45, 23, 67, 78]

print(list(set(list_with_duplicates)))  # [67, 12, 45, 78, 23]

# Is this a better way to do it or do you have a better suggestion?
