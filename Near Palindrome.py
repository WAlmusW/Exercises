def isNearPalindrome(string):
	N, R = str(string), str(string)[::-1]
	Count = 0
	
	for X in range(len(N)):
		if N[X] == R[X]:
			Count += 1
			
	if Count+2 == len(N):
		return 1
	else:
		return 0
