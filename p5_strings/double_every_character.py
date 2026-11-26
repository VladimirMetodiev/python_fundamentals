def double_char(some_str):
    return ''.join(ch * 2 for ch in some_str)

some_str = input('Enter some text: ')
print(double_char(some_str))





# Given a string, return a string where for every char in the original, there are two chars.





# Моето първо решение - 100/100

def double_char(some_str):
    result = ''

    for ch in some_str:
        result += ch + ch

    return result

some_str = input('Enter some text: ')
print(double_char(some_str))
