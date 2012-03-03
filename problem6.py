def square_of_sum(list):
	return sum(list)**2

def sum_of_squares(list):
	return sum(map(lambda x: x**2, list))

if __name__ == "__main__":
	print square_of_sum(range(1,101)) - sum_of_squares(range(1,101))