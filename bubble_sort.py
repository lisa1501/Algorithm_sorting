def bubble_sort(array):
    i = 0
    # Begin the outer loop
    while i < len(array) - 1:
        j = 0
        # Begin the inner loop
        while j < (len(array) - i - 1):
            # Compare two adjacent items
            if array[j] > array[j+1]:
                # Swap
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
            j += 1
        i += 1
    return array

# array=[99, 45, 35, 40, 16, 50, 11, 7, 90]
# step1:
# i=0:
# j=0
# while j<8
# if 99>45
# temp = 99
# array[0]=45
# array[1]=99
# [45, 99, 35, 40, 16, 50, 11, 7, 90]
# j=1
# while j<8
# if 99>35
# temp = 99
# array[1]=35
# array[2]=99
# [45, 35, 99, 40, 16, 50, 11, 7, 90]
# j=2
# while j<8
# if 99>40
# temp = 99
# array[2]=34
# array[3]=99
# [45, 35, 40, 99, 16, 50, 11, 7, 90]
# .
# .
# .
# [45, 35, 40, 16, 50, 11, 7,99, 90] 
# j=7
# while j<8
# if 99>90
# temp = 99
# array[7]=90
# array[8]=99
# [45, 35, 40, 16, 50, 11, 7,90, 99]
# j+1=8 while j<8 false
# i=1
# j=0
# while j < 7
# if 45 > 35
# temp = 45
# array[0]=35
# array[1]=45
# [35, 45, 40, 16, 50, 11, 7,90, 99]

