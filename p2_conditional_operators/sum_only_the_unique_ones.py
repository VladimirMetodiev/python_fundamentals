def lone_sum(a, b, c):
    result = 0
    if a != b and a != c:
        result += a
    if b != a and b != c:
        result += b
    if c != a and c != b:
        result += c
    return result

a = int(input())
b = int(input())
c = int(input())

print(lone_sum(a, b, c))





# Given 3 int values, a b c, return their sum. However, if one of the values 
# is the same as another of the values, it does not count towards the sum.



# Tests

# 5
# 5
# 5
# 0

# 14
# 5
# 78
# 97

# 1
# 2
# 1
# 2

# 1
# 1
# 2
# 2

# 2
# 1
# 1
# 2
