arr = [4, 3, 10, 2, 8, 9]

def selectionSortAlgo(arr):
    n = len(arr)
    
    for i in range(n-1):
        mini = i
        for j in range(i+1, n):
            if(arr[j] < arr[mini]):
                arr[j], arr[mini] = arr[mini], arr[j]
                

selectionSortAlgo(arr)
print(arr)
