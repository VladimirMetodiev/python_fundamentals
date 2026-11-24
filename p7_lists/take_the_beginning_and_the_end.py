def make_a_new_list(nums):
    return [nums[0] , nums[len(nums) - 1]]

nums = [int(j) for j in input().split(',')]
print(make_a_new_list(nums))
