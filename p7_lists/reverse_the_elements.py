def reverse(nums):
    last_index = len(nums) - 1
    for j in range(len(nums) // 2):
        current = nums[j]
        nums[j] = nums[last_index - j]
        nums[last_index - j] = current
    return nums

try:
    nums = [int(j) for j in input().split(',')]
    print(reverse(nums))
except ValueError:
    print('Invalid input')
