def check_for_identical_elements(a, b):
    return True if a[0] == b[0] or a[len(a) - 1] == b[len(b) - 1] else False

try:
    a = [int(j) for j in input().split(',')]
    b = [int(k) for k in input().split(',')]
    print(check_for_identical_elements(a, b))
except ValueError:
    print('Wrong input!')





# Given 2 arrays of ints, a and b, return True if they have 
# the same first element or they have the same last element. 
# Both arrays will be length 1 or more.
