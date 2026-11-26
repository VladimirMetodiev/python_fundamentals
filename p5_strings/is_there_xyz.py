def find_xyz(some_str):
    length_without_three = len(some_str) - 3
    index = some_str.find('xyz')

    while index <= length_without_three:
        if index != -1:
            if (index > 0 and some_str[(index - 1):index] != '.') or index == 0:
                return True
            else:
                index = some_str.find('xyz', index + 1)
        else:
            return False

    return False

some_str = input().lower()
print(find_xyz(some_str))





# Description

# Return True if the given string contains an appearance 
# of "xyz" where the xyz is not directly preceeded by 
# a period (.). So "xxyz" counts but "x.xyz" does not.
