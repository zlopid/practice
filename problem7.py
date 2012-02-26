from primes import allPrimes

def nthPrime(num):
	if (num < 1 or int(num) != num):
		raise TypeError("Expected a positive real number")
	
	getPrime = allPrimes()
	for i in range(num-1):
		getPrime.next()
	return getPrime.next()

if __name__ == "__main__":
	print nthPrime(10001)
		