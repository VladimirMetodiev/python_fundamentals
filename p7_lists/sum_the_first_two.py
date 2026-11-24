def sum_two(nums):
    length = len(nums)

    if length == 0:
        return 0
    elif length == 1:
        return nums[0]
    else:
        return nums[0] + nums[1]

try:
    data = input()
    nums = [0]

    if len(data) == 0:
        nums = []
    else:
        nums = [int(j) for j in data.split(',')]
    
    print(sum_two(nums))
except ValueError:
    print('Invalid input')
