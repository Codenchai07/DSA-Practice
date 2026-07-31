arr = [1, 2, 3, 4, 5, 6, 7]
k = 3


def rotate_arr_left_by_kth(arr, k):
    n = len(arr) - 1
    
    reverse_arr(arr, 0, k - 1)
    
    reverse_arr(arr,k, n)
    
    reverse_arr(arr,0,n)
    
    
        
def reverse_arr(arr,start,end):
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
       
       
def display_arr(arr):
    print(arr) 
    
rotate_arr_left_by_kth(arr, k)
display_arr(arr)