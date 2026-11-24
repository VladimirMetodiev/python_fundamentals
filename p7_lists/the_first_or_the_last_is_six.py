def first_last6(nums):
    return True if nums[0] == 6 or nums[len(nums) - 1] == 6 else False

nums = [int(j) for j in input().split(',')]
print(first_last6(nums))





# Given an array of ints, return True if 6 appears as 
# either the first or last element in the array. 
# The array will be length 1 or more.
