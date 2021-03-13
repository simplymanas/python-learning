# weight

weight = float(input("enter your weight : "))
unit = input("(K)g or (L)bs :")

if unit.upper() == "K":
	print(f"Weight in Lbs:{weight * 2.20}" )
elif unit.upper() == "L":
	print(f"Weight in Lbs: {weight /2.20}")
else:
	print("Wrong entry")

