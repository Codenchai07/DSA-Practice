arr = [4, 3, 10, 2, 8, 9]


def bubbleSortAlgo(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break   
        
bubbleSortAlgo(arr)
print("bubble sort")
print(arr)
   
        