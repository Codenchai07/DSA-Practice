arr = [4, 9, 12, 17, 25]
target = 12

def binary(arr, target):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if(arr[mid] == target):
            print("found at ",arr[mid])
            return
        elif(arr[mid] > target):
            end = mid - 1
        else:
            start = mid + 1
    print("Not found")

binary(arr,target)