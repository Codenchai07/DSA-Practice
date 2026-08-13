arr = [1, 2, 3, 4, 5, 6]

def swap_array_alternate(arr):
    left = 0
    right = 1
    
    while right < len(arr):
        arr[left], arr[right] = arr[right], arr[left]
        left += 2
        right += 2
        
        return arr

print(swap_array_alternate(arr))