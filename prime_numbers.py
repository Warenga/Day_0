def prime_numbers(num):

	if num > 1:
		for i in range(2, num):
			if num % i == 0:
				return "Not a prime number"
			else:
				return "A prime number"
	else:
		print "Not a prime number"

print prime_numbers(10)