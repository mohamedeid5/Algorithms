numbers = [5, 4, 3, 9, 8, 6, 7, 2, 10, 1]

for i in range(len(numbers)-1):
    
    min_idx = i
    
    for j in range(i+1, len(numbers)):
                
        if numbers[min_idx] > numbers[j]:
            min_idx = j
            
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    
    

