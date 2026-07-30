arr = [7, 1, 5, 3, 6, 4]

#output = [7, 6, 3, 5, 1, 4]

def revSubArray(arr):
    left = 1
    right = 4
    
    while left <= right :
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
        
    return arr


print(revSubArray(arr))