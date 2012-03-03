def mark_multiples(n, value, array):
	'''Set multiples of n to the given value in array'''
	i = 2;
	while n*i < len(array):
		array[n*i] = value
		i += 1

def primes_below(max):
	'''Generate all primes below the given maximum value'''
	# This uses the sieve of eratosthenes to find all the primes
	# See http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
	is_prime = [True]*max
	i = 2;
	while i < max:
		if is_prime[i]:
			yield i
			mark_multiples(i, False, is_prime)
		i += 1

if __name__ == "__main__":
	print sum(primes_below(2000000))