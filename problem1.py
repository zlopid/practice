def validMultiples(max):
	'''
	Returns positive numbers that are multiples of 3 or 5, up to max
	'''
	n = 0
	while n < max:
		if (n % 3 == 0) or (n % 5 == 0):
			yield n
		n += 1
		
if __name__ == "__main__":
	print sum(validMultiples(1000))