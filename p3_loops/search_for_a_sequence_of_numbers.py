def search_for_a_sequence(nums):
    for j in range(len(nums) - 2):
        if nums[j] == 1 and nums[j + 1] == 2 and nums[j + 2] == 3:
            return True

    return False

try:
    raw_data = input().split(',')

    if not raw_data or raw_data == ['']:
        raise ValueError('empty input')
    
    nums = [int(k) for k in raw_data]
    print(search_for_a_sequence(nums))
except ValueError as e:
    error_msg = str(e)

    if 'empty input' in error_msg:
        print('Error: no value entered')
    elif 'invalid literal' in error_msg:
        print('Error: the value is not a valid integer')
    else:
       print(f'Unexpected error {e}')





# Description

# Given an array of ints, return true if the sequence of numbers 1, 2, 3 appears in the array somewhere.





# Моето първо решение - 100/100

# def search_for_a_sequence(nums):
#     length = len(nums)
#     is_it_a_sequence = False

#     for j in range(length - 2):
#         if nums[j] == 1:
#             counter, index = 1, j + 1

#             while index < length and counter <= 3:
#                 if nums[index] - nums[index - 1] == 1:
#                     counter += 1
#                     index += 1
#                 else:
#                     break

#             if counter == 3:
#                 is_it_a_sequence = True
#                 break

#     if is_it_a_sequence == True:
#         return True
#     else:
#         return False

# try:
#     raw_data = input().split(',')

#     if not raw_data or raw_data == ['']:
#         raise ValueError('empty input')
    
#     nums = [int(k) for k in raw_data]
#     print(search_for_a_sequence(nums))
# except ValueError as e:
#     error_msg = str(e)

#     if 'empty input' in error_msg:
#         print('Error: no value entered')
#     elif 'invalid literal' in error_msg:
#         print('Error: the value is not a valid integer')
#     else:
#        print(f'Unexpected error {e}')




# Решение, което видях и ми хареса - 100/100

# def search_for_a_sequence(nums):
#     return [1, 2, 3] in [nums[j:j+3] for j in range(len(nums) - 2)]

# try:
#     raw_data = input().split(',')

#     if not raw_data or raw_data == ['']:
#         raise ValueError('empty input')
    
#     nums = [int(k) for k in raw_data]
#     print(search_for_a_sequence(nums))
# except ValueError as e:
#     error_msg = str(e)

#     if 'empty input' in error_msg:
#         print('Error: no value entered')
#     elif 'invalid literal' in error_msg:
#         print('Error: the value is not a valid integer')
#     else:
#        print(f'Unexpected error {e}')
