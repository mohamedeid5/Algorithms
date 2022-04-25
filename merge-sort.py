def mergeSort(arr):
    
    if len(arr) > 1:
        
        # Finding the mid of the array
        mid = int(len(arr) / 2)
        
        # Dividing the array elements
        l = arr[:mid]
        
        # into 2 halves
        r = arr[mid:]
        
        # Sorting the first half
        mergeSort(l)
        
        # Sorting the second half
        mergeSort(r)
        
        i = j = k = 0
        
        # Copy data to temp arrays L[] and R[]
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
        
        # Checking if any element was left
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
  
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

    return arr
    

print(mergeSort([5, 4, 2, 1, 9, 6, 7, 8, 3]))