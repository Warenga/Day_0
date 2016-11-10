import unittest

from . import prime_numbers.prime_numbers

class PrimeNumbersTest(unittest.Testcase):

	def test_validity(self):
		self.assertEqual(prime_numbers(10), "Not a prime number")

