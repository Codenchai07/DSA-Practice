arr = [1, 2, 3, -1, -2, -3]
arr1 = [1, 2, 3, -1, -2, -3, 4, 5]


def alternate_positive_negative_numbers(arr):
    """
    Rearranges the array into alternating positive and negative numbers while
    preserving the relative order of both positive and negative elements.

    This solution assumes the number of positive and negative elements is equal.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(arr)
    num = [0] * (n)

    pos_idx = 0
    neg_idx = 1

    for item in arr:
        if item > 0:
            num[pos_idx] = item
            pos_idx += 2
        else:
            num[neg_idx] = item
            neg_idx += 2

    return num


def alternate_pos_neg_numbers(arr1):
    """
    Rearranges the array into alternating positive and negative numbers using
    in-place swapping.

    This method works for both equal and unequal numbers of positive and negative
    elements. It does not preserve the relative order of the elements.

    Time Complexity:
    - Worst Case: O(n²)
    - Extra Space: O(1)
    """

    n = len(arr1)
    i = 0
    while i < n:
        # for positive number and index
        if i % 2 == 0:
            if arr1[i] > 0:
                i += 1
            else:
                j = i + 1
                while j < n and arr1[j] < 0:
                    j += 1

                if j == n:
                    break
                arr1[i], arr1[j] = arr1[j], arr1[i]
                i += 1
        # for negative number and index
        else:
            if arr1[i] < 0:
                i += 1
            else:
                j = i + 1
                while j < n and arr1[j] > 0:
                    j += 1
                if j == n:
                    break
                arr1[i], arr1[j] = arr1[j], arr1[i]
                i += 1
    return arr1


print(alternate_positive_negative_numbers(arr))
print(alternate_pos_neg_numbers(arr1))
