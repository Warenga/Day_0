from prime import prime_numbers

import unittest

class PrimeNumbersTest(unittest.TestCase):

	def test_if_number_is_int(self):
		self.assertEqual(prime_numbers("70"), "Only integers allowed")

	def test_negative_number(self):
		self.assertEqual(prime_numbers(-1), "Only Positive numbers allowed")

	def test_number_less_than_two(self):
		self.assertEqual(prime_numbers(1), [])

	def test_validity(self):
		self.assertEqual(prime_numbers(10), [2, 3, 5, 7])