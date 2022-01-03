arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(0, len(arr)):
    isSwapped = False
    for j in range(0, len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            isSwapped = True
        # IF no two elements were swapped
        # by inner loop, then break    
        if isSwapped == False:
            break