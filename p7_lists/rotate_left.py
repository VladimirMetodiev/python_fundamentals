def rotate_to_the_left(nums):
    length = len(nums)
    first = nums[0]

    for j in range(1, length):
        nums[j - 1] = nums[j]

    nums[length - 1] = first
    
    return nums

try:
    data = input()

    if len(data) == 0:
        raise ValueError('Empty string')
    
    nums = [int(k) for k in data.split(',')]
    print(rotate_to_the_left(nums))
except ValueError as e:
    error_msg = str(e)

    if 'Empty string' in error_msg:
        print(e)
    else:
        print('Invalid input')
