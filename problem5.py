from primes import smallestFactor

def primeFactorization(num):
	'''Generates the prime factorization of the given number, in order from smallest to largest'''
	if (num < 0 or int(num) != num):
		raise TypeError("Expected a positive integer")
		
	sf = 1
	while sf != num:
		num = num/sf
		sf = smallestFactor(num)
		yield sf

def merge(lhs, rhs):
	'''
	Merges two arrays with repeated elements such that the result array has
	the same occurrence of each value as the greater of the source arrays
	'''
	merged = []
	lhsIndex = 0
	rhsIndex = 0
	while (lhsIndex < len(lhs) or rhsIndex < len(rhs)):
		if lhsIndex < len(lhs) and rhsIndex < len(rhs) and (lhs[lhsIndex] == rhs[rhsIndex]):
			merged.append(lhs[lhsIndex])
			lhsIndex += 1
			rhsIndex += 1
		elif lhsIndex < len(lhs) and (rhsIndex >= len(rhs) or lhs[lhsIndex] < rhs[rhsIndex]):
			merged.append(lhs[lhsIndex])
			lhsIndex += 1
		elif rhsIndex < len(rhs):
			merged.append(rhs[rhsIndex])
			rhsIndex += 1
	return merged

def smallestNumberByDivisibleBy(list):
	'''
	Finds the smallest number divisible by all numbers in the list by
	combining their prime factorizations to get the factorization of the result
	'''
	sharedFactors = []

	for n in list:
		if int(n) != n:
			raise TypeError("Expected all integer entries in the list")
		sharedFactors = merge(sharedFactors, [f for f in primeFactorization(n)])

	num = 1
	for n in sharedFactors:
		num *= n

	return num

if __name__ == "__main__":
	print smallestNumberByDivisibleBy(range(1,21))