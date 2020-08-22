# manipulate functionality of a function,
# a test method just by adding @decorator_name
# python Decorator


import datetime
import sys


def log_decorator(func):
	def log():
		print(f"Log started for {func}   at  : {datetime.datetime.now()}")
		func()
		print(f"Logging over for  at  : {datetime.datetime.now()}")
	return log()


@log_decorator
def test_decorator_simple():
	print(f"Time in test : {datetime.datetime.now()}")

@log_decorator()
def is_leap(year):
	"""Return True for leap years, False for non-leap years """
	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# test_decorator_simple
# print(is_leap(2021))
