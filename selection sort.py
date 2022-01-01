numbers = [1, 6, 3, 0, 11, 9, 8]

for i in range(len(numbers)-1):
    
    min_idx = i
    for j in range(i+1, len(numbers)):
        if numbers[min_idx] > numbers[j]:
            min_idx = j
            
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]


print(numbers)