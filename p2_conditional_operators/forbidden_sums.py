def sorta_sum(a, b):
    result = a + b
    if result >= 10 and result <= 19:
        return 20
    return result

a = int(input('a = '))
b = int(input('b = '))

print(sorta_sum(a, b))





# Given 2 ints, a and b, return their sum. However, sums in the range [10, 19], 
# are forbidden, so in that case just return 20.
