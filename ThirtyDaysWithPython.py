# Day 1
#
# name = input("what is your name : ")
# print(name)
#
# user_name = 'John'
# age = 40
# print(user_name + str(age))
# print(type(str(age)))


## Day 2
## Ternary operator
#
# condition = True
#
# x = 1 if condition else 0
# print(x)

## adding big number


# Add big number with a comma(,) separated output

# you can use _ to separate the position, readability is better as well
#
# a_number = 1_00_000_000
#
# one_more_number = 1_00_000_000_000  # readability is nice
#
# total_of_both_the_number = a_number + one_more_number
#
# print(f'{total_of_both_the_number: ,}')  # prints  100,100,000,000


## managing resource
# context manager
# with open('chatbot.py', 'r') as f:
#     file_contents = f.read()
# words = file_contents.split(' ')
# word_count =  len(words)
# print(word_count)


## numeric function , index, zip
## unpack from zip

# names = ['manas', 'tuku', 'deepak','dave']
# heroes = ['Spiderman', 'shakitman', 'Batman','parkerman']
# universes = ['Marvel','DC','Marvel','DC']
# 
# for index, name in enumerate(names, start=1):
#     print(index, name)
# 
# for name, hero, universe in zip(names, heroes, universes):
#     print(f'{name} is actually {hero} from {universe}')
# 
# for value in zip(names, heroes, universes):
#     print(value)

## unpacking

# a, b, *c, d = (1, 2, 3, 4, 5)
# print(a,b, c ,d)

## getting and setting attirbute in a class
#
# class  Person():
#     pass
#
# person = Person()
#
# # person.first = 'manas'
# # person.last = 'dash'
#
# first_key = 'first'
# first_val = 'corey'
#
# # setattr(person,'first', 'corey')
# setattr(person,first_key, first_val)
#
# person_info = {'first': 'david', 'last': 'moris'}
#
# for key, value in person_info.items():
#     setattr(person,key,value)
#
# for key in person_info.keys():
#     print(getattr(person,key))
#
# # print(getattr(person, first_key))
# # print(person.last)


## log user id and password
# from getpass import getpass
#
# username = input('username: ')
# password = getpass('password: ')
#
# print('Logging In ....')


## get help , run in python console
# import smtpd
# help(smtpd)

#
# from datetime import datetime
# dir(datetime)


## function
# def hello_fun(greeting, name='you'):
# 	return '{}, {} Function.'.format(greeting, name)
#
#
# print(hello_fun('hello', 'manas'))


# DRY : Don't Repeat yourself
#
# def student_info(*args, **kwargs):
# 	print(args)
# 	print(kwargs)
#
# courses = ['Math', 'Arts']
# info = {'name':'John', 'age':'22'}
# # student_info('math', 'arts', name='John', age=22)
# student_info(*courses, **info)
# Union



