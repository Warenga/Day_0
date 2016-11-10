from prime import prime_numbers

import unittest

class PrimeNumbersTest(unittest.TestCase):

	def test_if_number_is_int(self):
		self.assertEqual(prime_numbers("70"), "Only integers allowed")

	def test_negative_number(self):
		self.assertEqual(prime_numbers(-1), "Only Positive numbers allowed")

	def test_number_less_than_two(self):
		self.assertEqual(prime_numbers(1), [])

	def test_validity_one(self):
		self.assertEqual(prime_numbers(10), [2, 3, 5, 7])

	def test_validity_two(self):
		self.assertEqual(prime_numbers(20), [2, 3, 5, 7, 11, 13, 17, 19] )

	def test_validity_number_two(self):
		self.assertEqual(prime_numbers(2), [2])

	def test_validity_of_big_numbers(self):
		self.assertEqual(prime_numbers(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

	def test_number_if_list(self):
		self.assertEqual(prime_numbers([]), "Only integers allowed")




