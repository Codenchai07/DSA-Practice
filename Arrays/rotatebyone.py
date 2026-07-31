#rotate the array left by one
arr = [1, 2, 3, 4, 5]
print("before rotated by one: ")
for i in arr:
    print(i,end=" ")
print("\nafter rotated by one: ")
def rotate_left_by_one(arr):
    n = len(arr) - 1
    
    first_Element = arr[0]
    
    for i in range(0,n):
        arr[i] = arr[i + 1]
    
    
    arr[n] = first_Element
    
    for i in arr:
        print(i,end=" ")
    
    
rotate_left_by_one(arr)