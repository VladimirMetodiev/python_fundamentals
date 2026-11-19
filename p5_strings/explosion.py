def string_explosion(some_str):
    index = len(some_str) + 1
    result = ''

    for j in range(1, index):
        result += some_str[0:j]

    return result

some_str = input()
print(string_explosion(some_str))





# Given a non-empty string like "Code" return a string like "CCoCodCode".
