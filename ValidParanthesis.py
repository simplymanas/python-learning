# Match parenthesis in a given string
# Algorithm
# 1. define a stack s
# 2. Iterate over each character in the string.
# 3. If we encounter an open bracket push it to the stack.
# 4. If we encounter a close bracket, check the top of the stack.
#    a. If the top of the stack is an open bracket of the same type continue
#    b. else false


def validParenthesis(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            if stack:
                top_elem = stack.pop()
            else:
                top_elem = "#"

            if mapping[char] != top_elem:
                return False
        else:
            stack.append(char)

    return not stack


string1 = "(){}[]"

string2 = "({)}"

print(validParenthesis(string1))
print(validParenthesis(string2))




