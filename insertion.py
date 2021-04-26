def insertion_sort(array):
    i = 1
    while i < len(array):
        to_insert = array[i]
        j = i
        # Search in the sorted portion of the array
        # for the correct position to insert array[i]
        while j > 0 and array[j-1] > to_insert:
            array[j] = array[j-1]
            j -= 1
        array[j] = to_insert
        i += 1
    return array
# array= [99, 45, 35, 40, 16, 50, 11, 7, 90]
# i =1 

# after step_1
# array_1= [45, 99, 35, 40, 16, 50, 11, 7, 90]
#start step_2
# i =2 :
#to_insert = 35
# j=2
# 2 > 0 and array[1]== 99 > 35
#array[2]=99 [45, 99, 99, 40, 16, 50, 11, 7, 90]
#j=1
# 1 >0 and array[1-1]=45 > 35
#array[1] = 45 [45,45,99, 40, 16, 50, 11, 7, 90]
# j=0
# array[0] = 35 [35,45,99, 40, 16, 50, 11, 7, 90]
# i+1 = 3 