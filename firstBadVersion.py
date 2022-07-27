
def searchInsert(nums: list, target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = (high + low) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            high = mid
        else:
            low = mid + 1
    return low


print(searchInsert([1, 3, 5, 6], 4))