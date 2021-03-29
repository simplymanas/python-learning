import unittest
from fizzbuzz import checkio

class TestFizzBuzz(unittest.TestCase):
	def test_fizz(self):
		for i in [3, 6, 9, 18]:
			print('testing', i)
			assert checkio(i) == 'Fizz'
	def test_buzz(self):
		for i in [5, 10, 50]:
			print('testing', i)
			assert checkio(i) == 'Buzz'

	def test_fizzbuzz(self):
		for i in [15, 30, 75]:
			print('testing', i)
			assert checkio(i) == 'FizzBuzz'

if __name__ == '__main__':
	unittest.main()
