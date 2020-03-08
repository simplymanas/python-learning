# you have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.
# Input: A string, that consist of digits.
# Output: An Int.
# Example:
# beginning_zeros('100') == 0
# beginning_zeros('001') == 2
# beginning_zeros('100100') == 0
# beginning_zeros('001001') == 2
# beginning_zeros('012345679') == 1
# beginning_zeros('0000') == 4
from functools import reduce


def beginning_zeros(number: str) -> int:
    y = 0

    for x in str(number):
        if int(x) > 0:
            break
        else:
            y += 1
    return y

    #
    # numofzero = lambda x,y : (y:y+1 if x > 0) ,(for y in str(number))
    # return numofzero



#   return reduce(lambda x, y: x * int(y),(y for y in str(number) if int(y) != 0),1)
# result= lambda x,y: y+1 if (int(x)==0) else exit
#
# print(result)
#
# numofzero = list(filter(lambda x: x > 10 and x < 20, listofNum))
# print('Filtered List : ', listofNum)

if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('00100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    # print("Coding complete? Click 'Check' to earn cool rewards!")
