def consecutive(nums, a, b):
    result = False
    for i in range(len(nums) - 1):
        if nums[i] == a and nums[i + 1] == b:
            result = True
        elif nums[i] == b and nums[i + 1] == a:
            result = True
    return result

