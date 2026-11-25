def check_for_close_and_far_value(a, b, c):
    if abs(a - b) <= 1 and abs(a - c) >= 2 and abs(b - c) >= 2 or abs(a - c) <= 1 and abs(a - b) >= 2 and abs(c - b) >= 2:
        return True
    else:
        return False

a = int(input())
b = int(input())
c = int(input())

print(check_for_close_and_far_value(a, b, c))





# Given three ints, a b c, return True if one of 
# b or c is "close" (differing from a by at most 1), 
# while the other is "far", differing from both other 
# values by 2 or more. Note: abs(num) computes 
# the absolute value of a number.



# Tests

# 1
# 2
# 10
# True

# 1
# 2
# 3
# False

# 4
# 1
# 3
# True

# 4
# 5
# 3
# False

# 4
# 3
# 5
# False

# -1
# 10
# 0
# True

# 0
# -1
# 10
# True

# 10
# 10
# 8
# True

# 8
# 9
# 7
# False

# 10
# 8
# 9
# False

# 7
# -7
# 11
# False

# 8
# 6
# 9
# True
