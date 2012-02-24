def fibonacci(maxValue):
	'''
	Generates values from the fibonacci sequence up to maxValue
	
	See http://en.wikipedia.org/wiki/Fibonacci_number
	'''
	n_2 = 0
	n_1 = 1
	n = n_1 + n_2
	yield n
	while n <= maxValue:
		yield n
		n_2 = n_1
		n_1 = n
		n = n_1 + n_2

def isEven(x):
	return not x % 2;

if __name__ == "__main__":
	print sum(filter(isEven, fibonacci(4000000)))