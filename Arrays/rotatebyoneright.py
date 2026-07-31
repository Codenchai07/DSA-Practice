arr = [1, 2, 3, 4, 5]

def rotate_arr_right_by_one(arr):
    n = len(arr)
    last_element = arr[n - 1]
    
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
        
    arr[0] = last_element
        
        
def display_arr(arr):
    print(arr)
        
        
rotate_arr_right_by_one(arr)
display_arr(arr)