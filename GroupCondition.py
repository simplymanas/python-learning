
# all, any for group condition check
# Manas Dash
# 22th July 2020
# think of any (or) and all (and) as series of logical or and and operators


healthy_percentage = 100
have_money = 0
no_of_friends = 5

mental_happiness = [
	healthy_percentage > 50,
	have_money > 0,
	no_of_friends >= 1
]

if all(mental_happiness):
	print('happiness inside')

if any(mental_happiness):
	print('happiness outside')

# happiness outside