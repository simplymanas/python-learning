month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
	"""Return True for leap years, False for non-leap years """

	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month) -> object:
	"""Return number rof days in that month in that year.
	:rtype: object
	"""
	if not 1 <= month <= 12:
		return "Invalid month"

	if month == 2 and is_leap(year):
		return 29

	return month_days[month]


print(days_in_month(2020, 2))
