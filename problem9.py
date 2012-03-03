from more_math import product

def pythagorean_triplet_with_sum(triplet_sum):
	'''Returns a pythagorean triplet where a^2 + b^2 = c^2 and a+b+c = triplet_sum'''
	min_a = 3
	min_b = 4
	min_c = 5
	for a in range(min_a, triplet_sum - min_b - min_c + 1):
		for b in range(min_b, triplet_sum - min_a - min_c + 1):
			c = triplet_sum - a - b
			if a**2 + b**2 == c**2:
				return (a, b, c)
				
if __name__ == "__main__":
	print product(pythagorean_triplet_with_sum(1000))