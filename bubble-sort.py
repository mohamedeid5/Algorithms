def bubbleSort(arr):
    n = len(arr)
    isSwapped = False
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSwapped = True
        # IF no two elements were swapped
        # by inner loop, then break   
        if isSwapped == False:
            break

arr = [34, 489, 14, 39, 45, 1]

bubbleSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("% d" % arr[i])