arr = [12, 35, 1, 10, 34, 1]

def secondlarg(arr):
    largest = -1
    secLarg = -1
    
    for num in arr:
        if num > largest:
            secLarg = largest
            largest = num
            
        elif num > secLarg and num != largest:
            secLarg = num
        
    return secLarg


print(secondlarg(arr))