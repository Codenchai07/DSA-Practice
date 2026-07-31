arr = [1, 2, 3, 0, 3, 0, 2, 3, 0, 3, 4]


def moves_zero_to_end(arr):
    i = 0
    j = 0
    n = len(arr)
    
    while i < n:
        if arr[i] == 0:
            i += 1
        else:
            arr[i], arr[j] =arr[j], arr[i]
            i += 1
            j += 1


moves_zero_to_end(arr)      