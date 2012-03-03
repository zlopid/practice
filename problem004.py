import math

def is_palindrome(num, digit=0):
	'''Checks whether a given integer number is palindromic (the same forwards and backwards)'''
	num_digits = math.ceil(math.log(num, 10))
	if digit > num_digits/2:
		return True
		
	last_digit = math.floor(num / 10**digit) % 10
	first_digit = math.floor(num / 10**(num_digits-1-digit)) % 10
	if first_digit != last_digit:
		return False
		
	return is_palindrome(num, digit+1)

def palindromes_from_n_digit_products(num_digits):
	''''Generates palindromes that are the products of two n-digit numbers'''
	min_value = 10**(num_digits-1)
	lhs = 10**num_digits
	while lhs > min_value:
		lhs -= 1
		rhs = lhs
		while rhs > min_value:
			rhs -= 1
			product = lhs*rhs
			if is_palindrome(product):
				yield product

if __name__ == "__main__":
	print max(palindromes_from_n_digit_products(3))