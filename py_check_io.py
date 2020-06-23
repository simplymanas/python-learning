# x = 101
#
# # print no of digits in a number
# print(len(str(x)))
#
#
# def end_zeros(num: int) -> int:
#     # your code here
#     # return str(num).count('0')
#     return len(str(num)) - len(str(num).rstrip('0'))
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(end_zeros(0))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert end_zeros(0) == 1
#     assert end_zeros(1) == 0
#     assert end_zeros(10) == 1
#     assert end_zeros(101) == 0
#     assert end_zeros(245) == 0
#     assert end_zeros(100100) == 2
#     print("Coding complete? Click 'Check' to earn cool rewards!")


# def is_even(num: int) -> bool:
#     # your code here
#     return not (num % 2)
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(is_even(2))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert is_even(2) == True
#     assert is_even(5) == False
#     assert is_even(0) == True


def correct_sentence(text: str) -> str:
    text = text[0].upper() + text[1:]

    if (text[len(text)-1]) != '.':
        return text[0:] + '.'
    return text[0:]

    # return text.title().join('.')


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."

    print("Coding complete? Click 'Check' to earn cool rewards!")
