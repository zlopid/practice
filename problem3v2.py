def smallestFactor(num):
	'''Find the smallest factor of a number, which is always a prime'''
	# We know the smallest factor is prime because if it was not,
	# it would be the product of two smaller numbers, and those numbers
	# would be factors of the given number.
	f = 2
	while (num % f != 0):
		f += 1
	return f

def largestPrimeFactor(num):
	'''Find the largest prime factor of a number by recursively removing all smaller factors'''
	sf = smallestFactor(num)
	
	# Base case: num is prime, and has no smaller factors 
	if (sf == num):
		return num
		
	# Induction case: num is composite, = sf * c
	# and the largest factor of num is the largest factor of c
	return largestPrimeFactor(num/sf)

if __name__ == "__main__":
	print largestPrimeFactor(600851475143)