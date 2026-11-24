def replace_elements(nums):
    first = nums[0]
    last = nums[len(nums) - 1]
    target = first if first >= last else last

    for j in range(1, len(nums) - 1):
        nums[j] = target

    return nums

try:
    nums = [int(j) for j in input().split(',')]
    print(replace_elements(nums))
except ValueError:
    print('Invalid input')
