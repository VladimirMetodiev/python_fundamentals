def count_evens(nums):
    counter = 0

    for n in nums:
        if n % 2 == 0:
            counter += 1

    return counter

try:
    numbers = [int(num) for num in input().split(',')]
    print(count_evens(numbers))
except ValueError:
    print('There are not any integers!')
