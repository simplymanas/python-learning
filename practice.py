# # print("hello world")
# # days = ['Monday', 'Tuesday', 'Wednesday',
# #         'Thursday', 'Friday']
# # a = b = c = 20
# # x, y, z = 1, 2, 3
# #
# # print(a)
# # print(b)
# # print(c)
# # print(x)
# # print(y)
# # print(z)
# #
# # print(days)
#
# # list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
# # tinylist = [123, 'john']
# #
# # print (list)          # Prints complete list
# # print (list[0]  )     # Prints first element of the list
# # print (list[1:3] )    # Prints elements starting from 2nd till 3rd
# # print (list[2:]   )   # Prints elements starting from 3rd element
# # print (tinylist * 2)  # Prints list two times
# # print (list + tinylist) # Prints concatenated lists
#
#
# dict = {}
# dict['one'] = "This is one"
# dict[2] = "This is two"
#
# tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
#
# # print(dict['one'])      # Prints value for 'one' key
# # print (dict[2] )         # Prints value for 2 key
# # print (tinydict )         # Prints complete dictionary
# # print (tinydict.keys())   # Prints all the keys
# # print (tinydict.values()) # Prints all the values
# #
# # print(oct(19))
#
# # operation
#
# a = 10
#
# # print(9//2)
# # print(9.0//2.0)
# # print(-11//3)
# #
# #
# # print(-11.0//3)
# # print(10**2)
#
# # print(~a)
# # # print(math.sqrt(56))
# # # print(abs(10))
# # print(math.pi)
# # print(math.e)
# #
# # x = 'the quick'
# #
# # if('l' in x):
# # #     print('yes')
# # para_str = """this is a long string that is made up of
# # several lines and non-printable characters such as
# # TAB ( \t ) and they will show up that way when displayed.
# # NEWLINEs within the string, whether explicitly given like
# # this within the brackets [ \n ], or just a NEWLINE within
# # the variable assignment will also show up.
# # """
# # print(para_str)
#
# # str = "this is String example....wow!!!";
# # print ("str.capitalize() : ", str.capitalize())
# #
#
# # list = ['physics', 'chemistry', 1997, 2000];
# # print ("Value available at index 2 : ")
# # print (list[2])
# # list[2] = 2001;
# # print ("New value available at index 2 : ")
# # print (list[2])
# # list.append('psycho')
# # print(list)
# # del list
# # print(list)
#
# # tup = ('physics', 'chemistry', 1997, 2000);
# # print( tup);
# # del tup;
# # print ("After deleting tup : ")
# # print (tup)
#
# #
# # # dictorionary
# #
# # capital = {'India': 'New Delhi', 'Australia': 'sydney', 'Japan': 'tokyo'}
# #
# # capital['Pakistan'] = 'isalambad'
# #
# # print(capital)
# #
# # print(capital['India'])
#
#
# # ticks = time.time()
# # print("Number of ticks since 12:00am, January 1, 1970:", ticks)
# #
# # localTime = time.localtime(time.time());
# # print(time.asctime(localTime))
#
# # cal = calendar.month(2020, 2)
# # print("Here is the calendar:")
# # print(cal)
# # print(calendar.leapdays(2020, 2021))
#
# # def showCalender( year, month ):
# #     "this function shows a calendear for a given month and year"
# #     calToShow = calendar.month(year, month)
# #     print(calToShow)
# #     return;
# #
# # def printinfo( name, age ):
# #    "This prints a passed info into this function"
# #    print("Name: ", name)
# #    print("Age ", age)
# #    return;
# #
# # showCalender(2020,6)
# # printinfo('manas','20')
#
# # # Call by reference
# # def changeme( mylist ):
# #    "This changes a passed list into this function"
# #    mylist = [ 1,2,3,4];
# #    print("Values inside the function: ", mylist)
# #    return
# #
# # # Now you can call changeme function
# # mylist = [10,20,30];
# # changeme( mylist );
# # print ("Values outside the function: ", mylist)
# #
# #
# # # Function definition is here
# # def printinfo(arg1, *vartuple):
# #     "This prints a variable passed arguments"
# #     print("Output is: ")
# #     print(arg1)
# #     for var in vartuple:
# #         print(var)
# #     return;
# #
# #
# # # Now you can call printinfo function
# # printinfo(10)
# # printinfo(70, 60, 50, 90, 99, 989)
#
#
# # lambda fucntion
#
#
# # Function definition is here
# # sum = lambda arg1, arg2: arg1 + arg2;
# #
# # # Now you can call sum as a function
# # print("Value of total : ", sum( 10, 20 ))
# # print("Value of total : ", sum( 20, 20 ))
#
# #
# # def all_the_same(elements: List[Any]) -> bool:
# #
# #     if List == []:
# #         return False
# #     for x in List:
# #         if x != List[0]:
# #             return False
# #     return True
# #
# #
# # if __name__ == '__main__':
# #     print("Example:")
# #     print(all_the_same([1, 1, 1]))
# #
# #     # These "asserts" are used for self-checking and not for an auto-testing
# #     assert all_the_same([1, 1, 1]) == True
# #     assert all_the_same([1, 2, 1]) == False
# #     assert all_the_same(['a', 'a', 'a']) == True
# #     assert all_the_same([]) == True
# #     assert all_the_same([1]) == True
# #     print("Coding complete? Click 'Check' to earn cool rewards!")
#
# # mylist = [23, 45, 23, 12, 45, 67, 78]
# # print(max(mylist))
# # print(min(mylist))
#
#
# # Quiz : There's no way to "reset" a generator. Do you "kya tod hai"
#
#
# # 2nd July 2020
# # enumeration
#
#
# '''
# Created on 02-Jul-2020
#
# @author: manas
#
# How to create enumeration
# '''
# #
# # # may be a quick way
# # class ActorRank:
# # 	Zero, SuperStar, Star, Hero, Cartoon = range(5)
# #
# #
# # print(ActorRank.SuperStar)
# #
# #
# # # the other way is to use what comes with python , Enum class
# # from enum import Enum
# #
# #
# # class Color(Enum):
# # 	RED = 1
# # 	GREEN = 2
# # 	BLUE = 3
# #
# #
# # # Enumeration members have human readable string representations:
# # print('1 here')
# # print (Color.RED)  # Color.RED
# #
# # # while their repr has more information:
# # print (repr(Color.RED))  # <Color.RED: 1>
# #
# # # The type of an enumeration member is the enumeration it belongs to:
# # print (type (Color.RED)) # <enum 'Color'>
# #
# # # verify isinstance
# # print (isinstance (Color.GREEN, Color))  # True
# #
# # # Enum members also have a property that contains just their item name:
# # print (Color.RED.name)  # RED
# #
# # # Also Enumerations support iteration, try to explore more
# # # https://docs.python.org/3/library/enum.html#enum.Enum
#
# #
# # class Color:
# #   RED = 1
# #   GREEN = 2
# #   BLUE = 3
# #
# # print (Color.RED)
#
# # remove duplicate elements from a list
# # Is this a better way to do it ot do you have a better suggestion?
#
# # mylist = [23, 45, 23, 12, 45, 23, 67, 78]
# #
# # print(list(set(mylist)))  # [67, 12, 45, 78, 23]
#
# #
# # smallest = None
# # print("Before:", smallest)
# # for itervar in [3, 41, 12, 9, 74, 15]:
# #     if smallest is None or itervar < smallest:
# #         smallest = itervar
# #         break
# #     print("Loop:", itervar, smallest)
# # print("Smallest:", smallest)
# #
# #
# # print(0 == 0.0)
# # print(0 is 0.0)
# #
# # print(0 is not 0.0)
#
#
# # import urllib.request
# # fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# # for line in fhand:
# #     print(line.decode().strip())
# #
# # class PartyAnimal:
# #     x = 0
# #     name = ''
# #     def __init__(self, nam):
# #         self.name = nam
# #         print(self.name,'constructed')
# #     def party(self):
# #         self.x = self.x + 1
# #         print(self.name,'party count',self.x)
# #
# # q = PartyAnimal('Quincy')
# # m = PartyAnimal('Miya')
# #
# # q.party()
# # m.party()
# # q.party()
#
#
#
# # 5th july 2020
# # Manas Dash
# # how do I : A cool library
# # try these in command line
#
# #https://github.com/gleitz/howdoi
# #pip install howdoi
#
#
#
# manasdash ~ % howdoi format date bash
# # put current date as yyyy-mm-dd in $date
# # -1 -> explicit current date, bash >=4.3 defaults to current time if not provided
# # -2 -> start time for shell
# printf -v date '%(%Y-%m-%d)T\n' -1
#
# # put current date as yyyy-mm-dd HH:MM:SS in $date
# printf -v date '%(%Y-%m-%d %H:%M:%S)T\n' -1
#
# # to print directly remove -v flag, as such:
# printf '%(%Y-%m-%d)T\n' -1
# # -> current date printed to terminal
#
# manasdash ~ % howdoi undo commits in git
# $ git commit -m "Something terribly misguided"             # (1)
# $ git reset HEAD~                                          # (2)
# << edit files as necessary >>                              # (3)
# $ git add ...                                              # (4)
# $ git commit -c ORIG_HEAD                                  # (5)
#
# # try executing this
# howdoi howdoi
#
# elements = [1,2,3,0,4,5]
# for element in elements:
# 	if element==0:
# 		print ("I have the power now")
# 		break
# else:
# 	print("breakup ho gaya")
