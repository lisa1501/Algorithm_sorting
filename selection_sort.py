def selection_sort(array):
    i = 0
    while i < len(array) - 1:
        min_index = i
        j = i + 1
        while j < len(array):
            if array[j] < array[min_index]:
                min_index = j
            j += 1
        if min_index != i:
            temp = array[min_index]
            array[min_index] = array[i]
            array[i] = temp
        i += 1
    return array

array = [99, 45, 35, 40, 16, 50, 11, 7, 90]
# step1:
# len(array)=9
# i=0
# while i < 8
# min_index = 0
# j = 0+1 = 1
# while j < 9
# if 45 < 99
# min_index = 1
# min_index != i
# temp = array[1]=45
# array[1] = 99
# array[0] = 45
# [45, 99, 35, 40, 16, 50, 11, 7, 90]



