import math

def factors(num):
	'''Generates all factors of a given number in increasing order'''
	
	# for every factor n, there is an opposite factor num/n
	# store them as we go so we can yield factors in order
	oppositeFactors = []
	
	# because this tracks opposite factors, it only needs to
	# iterate until the mid-point, sqrt(num)
	for n in range(2, int(math.sqrt(num))):
		if (num % n == 0):
			yield n
			oppositeFactors.append(num/n)
			
	while len(oppositeFactors) > 0:
		yield oppositeFactors.pop()


def primeFactors(num):
	'''Returns a list of the prime factors of the given num'''
	remainingFactors = [f for f in factors(num)]
	getPrimes = allPrimes()
	p = getPrimes.next()
	
	# Eliminate factors that are divisible by primes until all factors are known to be prime
	
	# When p > sqrt(max(remainingFactors)), then
	#   all remaining factors are not divisible by any primes less than p
	# 	if any factor was divisible by a prime greater than or equal to p,
	#		then the factor would also be divisible by factor/p
	#		and factor/p must be < sqrt(factor)
	#		but that's impossible because we've already tested all primes < sqrt(factor)
	#	therefore, no factor is divisible by a prime greater than or equal to p
	#	therefore, all remaining factors are prime
	while len(remainingFactors) > 0 and p < math.sqrt(max(remainingFactors)):
		remainingFactors= filter(lambda f: f % p != 0 or f == p, remainingFactors)
		p = getPrimes.next()
	return remainingFactors
	
if __name__ == "__main__":
	print max(primeFactors(600851475143))