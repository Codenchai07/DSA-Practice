arr = [4, 3, 10, 2, 8, 9]

def insertionSortAlgo(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key


print("before sorted: ", arr)
insertionSortAlgo(arr)
print("after sorted: ", arr)
    
    
