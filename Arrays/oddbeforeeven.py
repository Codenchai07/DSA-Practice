arr = [2, 7, 8, 5, 4, 3]


def odd_before_even_numbers(arr):
    n = len(arr)
    
    i = 0
    j = 0
    
    while i < n :
        if arr[i] % 2 != 0:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
            j += 1
        else:
            i += 1
    return arr


print(odd_before_even_numbers(arr))