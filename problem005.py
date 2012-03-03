from primes import smallest_factor
from more_math import product

def prime_factorization(num):
	'''Generates the prime factorization of the given number, in order from smallest to largest'''
	if (num < 0 or int(num) != num):
		raise TypeError("Expected a positive integer")
		
	sf = 1
	while sf != num:
		num = num/sf
		sf = smallest_factor(num)
		yield sf

def merge(lhs, rhs):
	'''
	Merges two arrays with repeated elements such that the result array has
	the same occurrence of each value as the greater of the source arrays
	'''
	merged = []
	lhs_index = 0
	rhs_index = 0
	while (lhs_index < len(lhs) or rhs_index < len(rhs)):
		if lhs_index < len(lhs) and rhs_index < len(rhs) and (lhs[lhs_index] == rhs[rhs_index]):
			merged.append(lhs[lhs_index])
			lhs_index += 1
			rhs_index += 1
		elif lhs_index < len(lhs) and (rhs_index >= len(rhs) or lhs[lhs_index] < rhs[rhs_index]):
			merged.append(lhs[lhs_index])
			lhs_index += 1
		elif rhs_index < len(rhs):
			merged.append(rhs[rhs_index])
			rhs_index += 1
	return merged

def least_common_multiple(list):
	'''
	Finds the smallest number divisible by all numbers in the list by
	combining their prime factorizations to get the factorization of the result
	'''
	shared_factors = []

	for n in list:
		if int(n) != n:
			raise TypeError("Expected all integer entries in the list")
		shared_factors = merge(shared_factors, [f for f in prime_factorization(n)])

	return product(shared_factors)

if __name__ == "__main__":
	print least_common_multiple(range(1,21))