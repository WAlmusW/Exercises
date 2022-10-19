def most_prime(array):
	from statistics import mode
	import math

	array_common = []
	while len(array) > 0:
		array_common.append(int(mode(array)))
		array = [X for X in array if X != (mode(array))]
				
	for num in array_common:
		if num == 1:
			continue

		for I in range(2, math.ceil(math.sqrt(num))):
			if num % I == 0:
				break
		else:
			return num
