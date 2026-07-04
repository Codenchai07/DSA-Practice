arr = [4, 3, 10, 2, 8, 9]

def selectionSortAlgo(arr):
    n = len(arr)
    for i in range(n - 1):
        mini = i
        for j in range (i+1, n):
            if(arr[j] < arr[mini]):
                mini = j
            
        arr[i], arr[mini] = arr[mini], arr[i]

print("before sorted: ", arr)
selectionSortAlgo(arr)
print("after sorted: ", arr)