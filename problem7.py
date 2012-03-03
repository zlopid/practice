from primes import all_primes

def nth_prime(num):
	if (num < 1 or int(num) != num):
		raise TypeError("Expected a positive real number")
	
	get_prime = all_primes()
	for i in range(num-1):
		get_prime.next()
	return get_prime.next()

if __name__ == "__main__":
	print nth_prime(10001)