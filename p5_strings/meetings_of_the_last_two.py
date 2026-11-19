def count_the_last_two(some_str):
    length = len(some_str)
    target = some_str[(length - 2):length]
    counter = 0
    
    for j in range(length - 2):
        if some_str[j:(j + 2)] == target:
            counter += 1

    return counter

some_str = input()
print(count_the_last_two(some_str))
