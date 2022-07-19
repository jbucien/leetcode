def arraySign(nums: list) -> int:
    """
    Takes a list of integers. Based on the product of all integers in nums, returns:
        1 if the product is positive.
        -1 if the product negative.
        0 if the product is equal to 0
    """
    nums.sort()
    neg = 0

    for i in range(len(nums)):
        if nums[i] >= 0:
            break
        neg += 1
    if nums[i] == 0:
        return 0
    else:
        if neg & 1:
            return -1
        else:
            return 1

print(arraySign([-1,-2,-3,-4,3,2,1]))
