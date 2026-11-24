def same_first_last(nums):
    if len(nums) == 0:
        return False

    return True if nums[0] == nums[len(nums) - 1] else False

data = input()

try:
    if len(data) == 0:
        print(same_first_last([]))
    else:
        nums = [int(j) for j in data.split(',')]
        print(same_first_last(nums))
except ValueError:
    print('Wrong input!')





# Given an array of ints, return True if the array is length 1 or more, 
# and the first element and the last element are equal.



# Tests

# 
# False

# 7
# True

# 2,4,6
# False

# 7,7
# True

# 7,9,7
# True

# 15,8,20,15
# True

# 1,2,3,4,5,1
# True

# 1,2,3,4,5,11
# False
