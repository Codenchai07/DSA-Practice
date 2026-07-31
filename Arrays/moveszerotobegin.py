arr = [1, 2, 3, 0, 3, 0, 2, 3, 0, 3, 4]


def moves_zero_to_begin(arr):
    n = len(arr)
    i = n - 1
    j = n - 1
    
    while i >= 0:
        if arr[i] == 0:
            i -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i -=1
            j -= 1


moves_zero_to_begin(arr)   
print(arr)   