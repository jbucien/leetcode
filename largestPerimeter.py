def largestPerimeter(nums: list) -> int:
    """
    Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0."""
    # Triangle rule: sum of two shorter sides must be larger than the longest side
    nums.sort(reverse=True)

    # loop through nums until process last 3 integers
    max_index = (len(nums) - 1) - 2
    i = 0
    while i <= max_index:
        # see if meets triangle rule
        if nums[i+1] + nums[i+2] > nums[i]:
            break
        else:
            i += 1
    if i > max_index:
        return 0
    else:
        return nums[i] + nums[i+1] + nums[i+2]




