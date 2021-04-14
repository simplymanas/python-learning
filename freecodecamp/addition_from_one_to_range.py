# this program caluclate the sum from 1 to a given number


target_number = int(input("Enter a number up to which you wan to calculate the sum from 1: "))
sum_of_numbers = target_number
for n in range(1,target_number):
	sum_of_numbers += n

print(f"The total sum of 1 to {target_number} is {sum_of_numbers}")
