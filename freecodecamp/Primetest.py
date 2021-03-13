# check if a number is a prime number or not

input_number = int(input("Enter a number: "))

ctr = 2
while ctr < input_number:
	if input_number % ctr == 0:
			print("not prime");
			break
	ctr+=1

if ctr == input_number:
	print("Prime number")
