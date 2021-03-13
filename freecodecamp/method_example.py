# strings are immutable

course = input("enter a course: ")

print(course.upper())  #returns a new string
print(course.find('b'))
print(course.replace('a', 'bb'))


# in operator
print('a' in course)