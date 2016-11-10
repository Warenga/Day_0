def is_prime(num):
	if num == 2:
		return True
	if num > 1:
		for i in range(2, num):
			if num % i == 0:
				return False
		return True
	else:
		return False

def prime_numbers(num):

	result = []
	not_prime = []

	if not isinstance(num, int):
		return "Only integers allowed"
	if num < 0:
		return "Only Positive numbers allowed"
	else:
		for i in range(2, num):
			if is_prime(i):
				result.append(i)
			else:
				not_prime.append(i)
		return result

print prime_numbers(10)





