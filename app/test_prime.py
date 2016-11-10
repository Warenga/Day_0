from prime import prime_numbers, is_prime

import unittest

class PrimeNumbersTest(unittest.TestCase):

	def test_number_is_int(self):
		self.assertEqual(prime_numbers("70"), "Invalid input")

	def test_negative_number(self):
		self.assertEqual(prime_numbers(-1), "Invalid input")

	def test_number_less_than_two(self):
		self.assertEqual(prime_numbers(1), [])

	def test_validity_ten(self):
		self.assertEqual(prime_numbers(10), [2, 3, 5, 7])

	def test_validity_number_two(self):
		self.assertEqual(prime_numbers(2), [2])

	def test_validity_twenty(self):
		self.assertNotEqual(prime_numbers(3), [])

	def test_validity_big_numbers(self):
		self.assertEqual(prime_numbers(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

	def test_number_if_list(self):
		self.assertEqual(prime_numbers([]), "Invalid input")

	def test_output_is_list(self):
		self.assertEqual(prime_numbers(0), [])

	def test_is_prime(self):
		self.assertIs(is_prime(7), True)

	def test_is_not_prime(self):
		self.assertIsNot(is_prime(9), True)




