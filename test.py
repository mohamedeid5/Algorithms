def quickSort(arr):
    # Write your code here
    pivot = arr[0]
    eq, left, right = [], [], []
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
    print(left)
    print(right)
            
            
arr = [2, 1, 4, 9, 3, 1, 6, 5, 7, 8, 10]    
quickSort(arr)
print(arr)