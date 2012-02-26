def allPrimes():
	'''Generate endless new primes. Warning: this will be slow for larger numbers'''
	primes = []
	n = 2
	while True:
		for p in primes:
			if (n % p == 0):
				break
		else:
			yield n
			primes.append(n)
		n += 1

def smallestFactor(num):
	'''Find the smallest factor of a number, which is always a prime'''
	# We know the smallest factor is prime because if it was not,
	# it would be the product of two smaller numbers, and those numbers
	# would be factors of the given number.
	f = 2
	while (num % f != 0):
		f += 1
	return f
	
	