# There are 1000 people standing in a row. They are numbered as 1,2,...,1000.
# There is a unique demon who eats only the persons which are standing on odd positions.
# It means that after his first round the person numbered 2 will come at position 1 and the one
# at 4 will come at 2 and so on. So what is the assigned number of the person which is left at last ?

import array
#def theOddManOut(limit):

limit = 100
numarr = array.array('i')
num = 1
while num < limit-1:
    numarr.append (num )
    num = num + 1

print(numarr)
