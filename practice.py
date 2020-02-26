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

def showCalender( year, month ):
    "this function shows a calendear for a given month and year"
    calToShow = calendar.month(year, month)
    print(calToShow)
    return;

def printinfo( name, age ):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age ", age)
   return;

showCalender(2020,6)
printinfo('manas','20')