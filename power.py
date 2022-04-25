def power(x, y):
    if y == 1:
        return x
    
    result = power(x, int(y/2))
    
    if int(y % 2) == 0:
        return result * result
    else:
        return result * result * x
    
print(power(2,5))