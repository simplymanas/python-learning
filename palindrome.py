
# verify if a string is palindrome or not
# avoid using built in function

input_string = input ("Enter the string : ")

if input_string[::-1].lower() == input_string.lower():
	print ("Oh My God!!! that's a palindrome 👏")
else:
	print ("Try again ")




