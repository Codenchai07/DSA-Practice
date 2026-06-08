arr = [3, -1, -5, 7, 2]


def positiveNnegative(arr):
    pos_count = 0
    neg_count = 0
    for el in arr:
        if(el >= 0):
            pos_count += 1
        else:
            neg_count += 1
    
    print("Positive ",pos_count)
    print("Negative",neg_count)
    
positiveNnegative(arr)

