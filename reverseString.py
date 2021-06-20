def reverse(string):
	if len(string) < 1: return string
	return reverse(string[1:]) + string[0]

print(reverse("hello"))