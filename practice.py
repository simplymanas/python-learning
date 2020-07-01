import math
import time
import calendar

# print("hello world")
# days = ['Monday', 'Tuesday', 'Wednesday',
#         'Thursday', 'Friday']
# a = b = c = 20
# x, y, z = 1, 2, 3
#
# print(a)
# print(b)
# print(c)
# print(x)
# print(y)
# print(z)
#
# print(days)

# list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
# tinylist = [123, 'john']
#
# print (list)          # Prints complete list
# print (list[0]  )     # Prints first element of the list
# print (list[1:3] )    # Prints elements starting from 2nd till 3rd
# print (list[2:]   )   # Prints elements starting from 3rd element
# print (tinylist * 2)  # Prints list two times
# print (list + tinylist) # Prints concatenated lists


dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

# print(dict['one'])      # Prints value for 'one' key
# print (dict[2] )         # Prints value for 2 key
# print (tinydict )         # Prints complete dictionary
# print (tinydict.keys())   # Prints all the keys
# print (tinydict.values()) # Prints all the values
#
# print(oct(19))

# operation

a = 10

# print(9//2)
# print(9.0//2.0)
# print(-11//3)
#
#
# print(-11.0//3)
# print(10**2)

# print(~a)
# # print(math.sqrt(56))
# # print(abs(10))
# print(math.pi)
# print(math.e)
#
# x = 'the quick'
#
# if('l' in x):
# #     print('yes')
# para_str = """this is a long string that is made up of
# several lines and non-printable characters such as
# TAB ( \t ) and they will show up that way when displayed.
# NEWLINEs within the string, whether explicitly given like
# this within the brackets [ \n ], or just a NEWLINE within
# the variable assignment will also show up.
# """
# print(para_str)

# str = "this is String example....wow!!!";
# print ("str.capitalize() : ", str.capitalize())
#

# list = ['physics', 'chemistry', 1997, 2000];
# print ("Value available at index 2 : ")
# print (list[2])
# list[2] = 2001;
# print ("New value available at index 2 : ")
# print (list[2])
# list.append('psycho')
# print(list)
# del list
# print(list)

# tup = ('physics', 'chemistry', 1997, 2000);
# print( tup);
# del tup;
# print ("After deleting tup : ")
# print (tup)

#
# # dictorionary
#
# capital = {'India': 'New Delhi', 'Australia': 'sydney', 'Japan': 'tokyo'}
#
# capital['Pakistan'] = 'isalambad'
#
# print(capital)
#
# print(capital['India'])


# ticks = time.time()
# print("Number of ticks since 12:00am, January 1, 1970:", ticks)
#
# localTime = time.localtime(time.time());
# print(time.asctime(localTime))

# cal = calendar.month(2020, 2)
# print("Here is the calendar:")
# print(cal)
# print(calendar.leapdays(2020, 2021))

# def showCalender( year, month ):
#     "this function shows a calendear for a given month and year"
#     calToShow = calendar.month(year, month)
#     print(calToShow)
#     return;
#
# def printinfo( name, age ):
#    "This prints a passed info into this function"
#    print("Name: ", name)
#    print("Age ", age)
#    return;
#
# showCalender(2020,6)
# printinfo('manas','20')

# # Call by reference
# def changeme( mylist ):
#    "This changes a passed list into this function"
#    mylist = [ 1,2,3,4];
#    print("Values inside the function: ", mylist)
#    return
#
# # Now you can call changeme function
# mylist = [10,20,30];
# changeme( mylist );
# print ("Values outside the function: ", mylist)
#
#
# # Function definition is here
# def printinfo(arg1, *vartuple):
#     "This prints a variable passed arguments"
#     print("Output is: ")
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return;
#
#
# # Now you can call printinfo function
# printinfo(10)
# printinfo(70, 60, 50, 90, 99, 989)


# lambda fucntion


# Function definition is here
# sum = lambda arg1, arg2: arg1 + arg2;
#
# # Now you can call sum as a function
# print("Value of total : ", sum( 10, 20 ))
# print("Value of total : ", sum( 20, 20 ))

from typing import List, Any

#
# def all_the_same(elements: List[Any]) -> bool:
#
#     if List == []:
#         return False
#     for x in List:
#         if x != List[0]:
#             return False
#     return True
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(all_the_same([1, 1, 1]))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert all_the_same([1, 1, 1]) == True
#     assert all_the_same([1, 2, 1]) == False
#     assert all_the_same(['a', 'a', 'a']) == True
#     assert all_the_same([]) == True
#     assert all_the_same([1]) == True
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# mylist = [23, 45, 23, 12, 45, 67, 78]
# print(max(mylist))
# print(min(mylist))


# Quiz : There's no way to "reset" a generator. Do you "kya tod hai"


# 2nd July 2020
# enumeration
class ActorRank:
	Idiot, SuperStar, Star, Hero, Cartoon = range(5)


print (ActorRank.SuperStar)
