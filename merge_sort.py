	if len(array) == 1:
		return array
	middleIdx = len(array)//2
	leftHalf = array[:middleIdx]
	rightHalf = array[middleIdx:]
	return mergeSortedArrays(mergeSort(lefHalf),mergeSort(rightHalf))

def mergeSorteArrays(leftHalf,rightHalf):
	sortedArray = [None] * (len(leftHalf) + len(rightHalf):
    k = i = j = 0
	while i < len(leftHalf) and j < len(rigthHalf):
		if leftHalf[i] <= rightHalf[j]:
			sortedArray[k] = leftHalf[i]
			i += 1
		else:
			sortedArray[k] = leftHalf[j]
			j+= 1
		k += 1