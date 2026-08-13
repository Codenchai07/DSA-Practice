arr = [1, 2, 3, 4, 5]



def copy_array(arr):
    n = len(arr)
    arr1 = list()
    for i in range(0, n, 1):
        arr1.append(arr[i])

    return arr1


print(arr)
print(copy_array(arr))
