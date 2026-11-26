import string

def count_code(some_str):
    return sum(some_str.count('co' + letter + 'e') for letter in string.ascii_lowercase)

some_str = input().lower()
print(count_code(some_str))





# Return the number of times that the string "code" appears 
# anywhere in the given string, except we'll accept any letter 
# for the "d", so "cope" and "cooe" count.





# Моето първо решение - 100/100

# def count_code(some_str):
#     temporary = [chr(ch) for ch in range(97, 123)]
#     counter = 0

#     for letter in temporary:
#         current = 'co' + letter + 'e'
#         counter += some_str.count(current)

#     return counter

# some_str = input().lower()
# print(count_code(some_str))
