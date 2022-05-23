def missing_no(nums):
    n = 0
    if nums[n] < nums[n + 1]:
        for i in range(len(nums)):
            if nums[i] != ((nums[i+1]) - 1):
                return nums[i] + 1
    elif nums[n] > nums[n + 1]:
        for i in range(len(nums)):
            if nums[i] != ((nums[i+1]) + 1):
                return nums[i] - 1
