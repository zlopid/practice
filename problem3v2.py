from primes import smallest_factor

def largest_prime_factor(num):
	'''Find the largest prime factor of a number by recursively removing all smaller factors'''
	sf = smallest_factor(num)
	
	# Base case: num is prime, and has no smaller factors 
	if (sf == num):
		return num
		
	# Induction case: num is composite, = sf * c
	# and the largest factor of num is the largest factor of c
	return largest_prime_factor(num/sf)

if __name__ == "__main__":
	print largest_prime_factor(600851475143)