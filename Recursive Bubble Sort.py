def bubbleSortRec(array):
	Check = 0
	for X in range(len(array)-1):
		if array[X] > array[X+1]:
			array[X], array[X+1] = array[X+1], array[X]
			Check += 1
			
	if Check == 0:
		return array
	else:
		return bubbleSortRec(array)
