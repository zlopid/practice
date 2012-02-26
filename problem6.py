def sumOfSquares(list):
	return sum(map(lambda x: x**2, list))
	
def squareOfSum(list):
	return sum(list)**2
	
if __name__ == "__main__":
	print squareOfSum(range(1,101)) - sumOfSquares(range(1,101))