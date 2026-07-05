nums = [1, 1, 2, 3, 6, 2, 3]


def singleNumberAlgo(nums):
    ans = 0

    for i in nums:
        ans ^= i

    return ans


print(singleNumberAlgo(nums))
