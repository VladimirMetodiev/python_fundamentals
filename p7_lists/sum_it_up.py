def sum_up(nums):
    total = 0
    for j in nums:
        total += j
    return total

try:
    nums = [int(j) for j in input().split(',')]
    print(sum_up(nums))
except ValueError:
    print('Wrong input!')
