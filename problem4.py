import math

def isPalindrome(num, digit=0):
	'''Checks whether a given integer number is palindromic (the same forwards and backwards)'''
	numDigits = math.ceil(math.log(num, 10))
	if digit > numDigits/2:
		return True
		
	lastDigit = math.floor(num / 10**digit) % 10
	firstDigit = math.floor(num / 10**(numDigits-1-digit)) % 10
	if firstDigit != lastDigit:
		return False
		
	return isPalindrome(num, digit+1)

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