from app import prime

import unittest

class PrimeNumbersTest(unittest.Testcase):

	# def test_validity(self):
	# 	self.assertEqual(prime.prime_numbers(10), [2, 3, 5, 7])

	def test_if_number_is_int(self):
		self.assertEqual(prime_numbers("70"), "Only integers allowed")