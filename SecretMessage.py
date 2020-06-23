# Ever tried to send a secret message to someone without using the postal service? You could use newspapers to tell your secret. Even if someone finds your message, it's easy to brush them off as paranoid and as a conspiracy theorist. One of the simplest ways to hide a secret message is to use capital letters. Let's find some of these secret messages.
#
# You are given a chunk of text. Gather all capital letters in one word in the order that they appear in the text.
#
# For example: text = "How are you? Eh, ok. Low or Lower? Ohhh.", if we collect all of the capital letters, we get the message "HELLO".
#
# Input: A text as a string (unicode).
#
# Output: The secret message as a string or an empty string.
#
# Example:
# find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO"
# find_message("hello world!") == ""

# How it is used: This is a simple exercise in working with strings: iterate, recognize and concatenate.
#
# Precondition: 0 < len(text) ≤ 1000
# all(ch in string.printable for ch in text)

def find_message(text: str) -> str:
    """Find a secret message"""
    # return ""
    #  return reduce(lambda x: x + x,(x for x in str if  str.isupper(x)==true)
    y = ''
    for x in text:
        if x.isupper(): y = y + x
    return y


if __name__ == '__main__':
    print('Example:')
    print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
