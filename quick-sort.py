# main

def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    
    for j in range(low, high):
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            i=i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
        
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    
    
arr = [10, 7, 8, 9, 1, 5]    
n = len(arr)
quickSort(arr, 0, n-1)
for i in range(n):
    print("%d" % arr[i])