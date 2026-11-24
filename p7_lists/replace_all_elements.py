def replace_all(nums):
    first = nums[0]
    last = nums[len(nums) - 1]
    target = first if first >= last else last

    for j in range(len(nums)):
        nums[j] = target

    return nums

try:
    nums = [int(j) for j in input().split(',')]
    print(replace_all(nums))
except ValueError:
    print('Invalid input')
