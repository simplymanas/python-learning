
import operator


def con_check(a):
	try:
		a = int(a)
		return True
	except:
		return False


def arithmetic_arranger(problems, con=False):
	arranged_problems = ""
	dict = {"+": operator.add, "-": operator.sub}
	first = [*range(len(problems))]
	second = [*range(len(problems))]
	sign = [*range(len(problems))]
	x = 0
	for i in problems:
		first[x], sign[x], second[x] = i.split()
		if len(str(first[x])) > 4 or len(str(second[x])) > 4:
			return "Error: Numbers cannot be more than four digits."
		elif x > 4:
			return "Error: Too many problems."
		elif not sign[x] in dict:
			print(sign[x])
			return "Error: Operator must be '+' or '-'."
		elif not con_check(first[x]) or not con_check(second[x]):
			return "Error: Numbers must only contain digits."
		x += 1

	# first line
	for i in range(len(problems)):
		arranged_problems += str(
			" " * (len(str(max(int(first[i]), int(second[i])))) - len(str(first[i])) + 2) + first[i] + "    ")

	arranged_problems += str("\n")
	# second line
	for i in range(len(problems)):
		arranged_problems += str(
			sign[i] + " " * (len(str(max(int(first[i]), int(second[i])))) - len(second[i]) + 1) + second[i] + "    ")
	arranged_problems += str("\n")
	# Third line
	for i in range(len(problems)):
		arranged_problems += str("--" + "-" * (len(str(max(int(first[i]), int(second[i]))))) + "    ")
	arranged_problems += str("\n")

	# print(arranged_problems)
	if con:
		for i in range(len(problems)):
			arranged_problems += str(" " * (len(str(max(int(first[i]), int(second[i])))) - len(
				str(dict[sign[i]](int(first[i]), int(second[i])))) + 2) + str(
				dict[sign[i]](int(first[i]), int(second[i]))) + "    ")

	return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
