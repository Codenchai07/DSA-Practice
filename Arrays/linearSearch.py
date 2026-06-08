arr = [4, 9, 2, 7, 5]
target = 2


def linear(arr, target):
    for el in range(len(arr)):
        if (arr[el] == target):
            print("found at index ", el)
            return
    print("Not found")


linear(arr, target)
