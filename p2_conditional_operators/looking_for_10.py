def makes10(a, b):
    total = a + b

    if a == 10 or b == 10 or total == 10:
        return True
    else:
        return False

a = int(input('a = '))
b = int(input('b = '))

print(makes10(a, b))





# Description

# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
