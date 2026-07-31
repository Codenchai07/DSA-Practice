#rotate the array left by one
arr = [1, 2, 3, 4, 5]
print("before rotated by one: ")
for i in arr:
    print(i,end=" ")
print("\nafter rotated by one: ")
def rotateleftbyone(arr):
    n = len(arr) - 1
    
    firstEle = arr[0]
    # print(firstEle)
    
    for i in range(0,n):
        arr[i] = arr[i + 1]
    
    
    arr[n] = firstEle
    
    for i in arr:
        print(i,end=" ")
    
    
rotateleftbyone(arr)