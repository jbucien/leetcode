def search(nums: list, target: int) -> int:
    """
    Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
    
    You must write an algorithm with O(log n) runtime complexity.
    """
    lower = 0
    upper = len(nums) - 1
    while (upper - lower) >= 0:
        mid = (lower + upper) // 2 
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            upper = mid - 1
        else: 
            lower = mid + 1
    return -1


# test_list = [20, 25, 30, 32, 37, 42, 47]
# test_int = 21
# print(search(test_list, test_int))
    
    

