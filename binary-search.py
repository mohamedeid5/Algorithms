arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def find_number(arr, low, high, num):
    
    if high >= low:
        mid = (low + high) // 2
        
        # If element is present at the middle itself
        if arr[mid] == num:
            return mid
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > num:
            return find_number(arr, low, mid - 1, num)
        # Else the element can only be present in right subarray
        else:
            return find_number(arr, mid + 1, high, num)
            
    else:
        return -1


result = find_number(arr, 0, len(arr)-1, 20)

if result != -1:
    print('element is present at index', str(result))
else:
    print('element not found')
    
    

