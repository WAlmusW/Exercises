def toBase26(integer):
	import math
	Character = 'abcdefghijklmnopqrstuvwxyz'
	C26 = ""
	
	while integer >= 26:
		X = integer % 26
		integer = math.floor(integer/26)
		C26 += Character[X]
	
	X = integer
	C26 += Character[X]
		
	return C26[::-1]
