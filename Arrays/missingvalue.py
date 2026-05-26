arr = [1,2,3,5]

def missingValue(arr):
    n = len(arr) + 1

    expected_sum = n * (n + 1) // 2

    actual_sum = 0

    for i in arr:
        actual_sum += i
        
    miss_value = expected_sum - actual_sum
    
    return miss_value

print(f"the missing value is {missingValue(arr)}")
    

    
    
