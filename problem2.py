def fibonacci(max_value):
	'''
	Generates values from the fibonacci sequence up to max_value
	
	See http://en.wikipedia.org/wiki/Fibonacci_number
	'''
	n_2 = 0
	n_1 = 1
	n = n_1 + n_2
	yield n
	while n <= max_value:
		yield n
		n_2 = n_1
		n_1 = n
		n = n_1 + n_2

def is_even(x):
	return not x % 2;

if __name__ == "__main__":
	print sum(filter(is_even, fibonacci(4000000)))