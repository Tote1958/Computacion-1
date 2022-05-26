def sum_of_differences(nums):
    nums.sort(reverse=True)
    total = 0
    for i in range(len(nums) - 1):
        total = total + (nums[i] - nums[(i + 1)])
    return total

