def fix_teen(n):
    if n == 15 or n == 16:
        return n
    else:
        return 0

def no_teen_sum(a, b, c):
    if a >= 13 and a <= 19:
        a = fix_teen(a)
    if b >= 13 and b <= 19:
        b = fix_teen(b)
    if c >= 13 and c <= 19:
        c = fix_teen(c)
    return a + b + c

try:
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))

    print(no_teen_sum(a, b, c))
except ValueError:
    print('invalid integer')





# Given 3 int values, a b c, return their sum. However, if any of 
# the values is a teen -- in the range [13, 19] then that value 
# counts as 0, except 15 and 16 do not count as a teens. Write 
# a separate helper "def fix_teen(n):" that takes in an int value 
# and returns that value fixed for the teen rule. In this way, 
# you avoid repeating the teen code 3 times (i.e. "decomposition"). 
# Define the helper below and at the same indent level as the main 
# no_teen_sum().
