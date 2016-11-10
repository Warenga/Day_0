import time

def is_prime(num):
	if num > 1:
		for i in range(2, num):
			if num % i == 0:
				return False
		return True
	else:
		return False

def prime_numbers(num):
	start = time.time()

	prime = []

	if not isinstance(num, int):
		return "Only integers allowed"
	elif num < 0:
		return "Only Positive numbers allowed"
	elif num == 2:
		prime.append(2)
		return prime
	else:
		for i in range(2, num):
			if is_prime(i):
				prime.append(i)
		return prime

prime_numbers(10)





