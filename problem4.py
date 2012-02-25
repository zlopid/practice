import math

def isPalindrome(num):
	'''Checks whether a given integer number is palindromic (the same forwards and backwards)'''
	if int(num) != num:
		raise TypeError("integer argument expected, got float")
		
	digits = []
	while num > 0:
		digits.append(num % 10)
		num = math.floor(num/10)
	
	numDigits = len(digits)
	for index in range(int(numDigits/2)):
		if digits[index] != digits[numDigits-1-index]:
			return False
	return True
	
def palindromesFromNDigitProducts(numDigits):
	minValue = 10**(numDigits-1)
	lhs = 10**numDigits
	while lhs > minValue:
		lhs -= 1
		rhs = lhs
		while rhs > minValue:
			rhs -= 1
			product = lhs*rhs
			if isPalindrome(product):
				yield product
		
if __name__ == "__main__":
	print max(palindromesFromNDigitProducts(3))