def count_nines(nums):
    counter = 0
    for j in nums:
        if j == 9:
            counter += 1
    return counter

nums = [int(k) for k in input().split(',')]
print(count_nines(nums))
