def has_2_or_3(nums):
    return True if nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3 else False

nums = [int(j) for j in input().split(',')]
print(has_2_or_3(nums))
