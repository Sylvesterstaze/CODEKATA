import math

def xSum(n, m) :

	# variable to
	# store result
	res = 0

	# variable to maintain
	# place value
	multiplier = 1

	# variable to maintain
	# each digit sum
	bit_sum = 0

	# Add numbers till each
	# number become zero
	while (n or m) :

		# Add each bits
		bit_sum = ((n % 10) +
				(m % 10))
		
		# Neglect carry
		bit_sum = bit_sum % 10
		
		# Update result
		res = (bit_sum *
			multiplier) + res
		n = math.floor(n / 10)
		m = math.floor(m / 10)
		
		# Update multiplier
		multiplier = multiplier * 10
	
	return res

# Driver code
n,m =input().split()
n=int(n)
m=int(m)
print (xSum(n, m))