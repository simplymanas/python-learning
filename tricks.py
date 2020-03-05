# Print even number within a range of 20

evens = [x for x in range(20) if x % 2 == 0]
print(evens)

# lambda functions

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def square(n):
    return n ** n


squares = list(map(lambda x: x ** 2, numbers))
print(squares)
