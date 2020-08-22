# Multiple Comparisons
# the way vs. the better way
# simplify chained comparison
# Manas Dash
# Raksha Bhandhan day of 2020


time_of_the_day = 6
day_of_the_week = 'mon'

# this way
if time_of_the_day < 12 and time_of_the_day > 6:
	print('Good morning')

# a better way
if 6 < time_of_the_day < 12:
	print('Good morning')


# this way
if day_of_the_week == "Mon" or day_of_the_week == "Wed" or day_of_the_week == "Fri" or day_of_the_week == "Sun":
	print('its just a week day')

# a better way
if day_of_the_week in "Mon Wed Fri Sun".split():  # you can also specify a tuple ("Mon", "Wed", "Fri", "Sun")
	print('its just a week day')

# this way
if time_of_the_day < 17 and time_of_the_day > 10 and day_of_the_week == 'mon':
	print('its a working day')

# a better way
if all(time_of_the_day < 17, time_of_the_day > 10, day_of_the_week == 'mon'):
	print('its a working day')

# similar way use 'any' for logical operator 'or'

# The way is on the way