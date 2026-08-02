arr = [5, -8, -2, 9, 1, -4]


def move_positive_numbers_left(arr):
    """This function solve the classic array problem that placed the all positive number at start or left"""
    i = 0
    j = 0

    n = len(arr)

    while i < n:
        if arr[i] > 0:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
            j += 1
        else:
            i += 1


move_positive_numbers_left(arr)
print(arr)
