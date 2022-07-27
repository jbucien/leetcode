def sortedSquares(nums: list) -> list:
    """
    Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
    """
    # pointer i --> negative numbers 
    # pointer j ---> positive numbers
    if len(nums) == 1:
        return [nums[0]**2]
    else:
        sorted = [0 for n in nums]
        i = 0
        j = len(nums) - 1
        k = len(nums) - 1
        while i <= j:
            if abs(nums[i]) <= nums[j]:
                sorted[k] = nums[j] ** 2
                j -= 1
            else:
                sorted[k] = nums[i] ** 2
                i += 1
            k -= 1
        return sorted


# test1 = [-5, -3, -1, 0, 4, 5]
# test2 = [-9]
# test3 = [4, 5]
# test4 = [-2, -2]
# print(sortedSquares(test4))