def count_nines(nums):
    nums_size = len(nums)
    length = 4 if nums_size >= 4 else nums_size
    has_nine = False

    for j in range(length):
        if nums[j] == 9:
            has_nine = True
            break

    return has_nine

try:
    raw_data = input().split(',')

    if not raw_data or raw_data == ['']:
        raise ValueError('empty input')
    
    nums = [int(k) for k in raw_data]
    print(count_nines(nums))
except ValueError as e:
    error_msg = str(e)

    if 'empty input' in error_msg:
        print('Error: no value entered')
    elif 'invalid literal' in error_msg:
        print('Error: the value is not a valid integer')
    else:
       print(f'Unexpected error {e}')





# БЕЛЕЖКИ ПО ЗАДАЧАТА:

# Ако искам да използвам контекста към грешката:
# `except ValueError as e:` - достъпвам обекта на грешката
# `raise ValueError('empty input')` - предизвиквам грешка с текстово съобщение, което става част от обекта на грешката - `error_msg = str(e)`
# Използвам if-else проверки
