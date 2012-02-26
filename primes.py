def smallestFactor(num):
	'''Find the smallest factor of a number, which is always a prime'''
	# We know the smallest factor is prime because if it was not,
	# it would be the product of two smaller numbers, and those numbers
	# would be factors of the given number.
	f = 2
	while (num % f != 0):
		f += 1
	return f