def near_hundred(n):
    diff100 = abs(100 - n)
    diff200 = abs(200 - n)

    if diff100 <= 10 or (diff100 > 100 and diff100 <= 110) or diff200 <= 10 or (diff200 > 200 and diff200 <= 210):
        return True
    else:
        return False

n = int(input())
print(near_hundred(n))





# Description

# Given an int n, return True if it is within 10 of 100 or 200.



# Tests

# 0
# False

# 95
# True

# 90
# True

# 15
# False

# 89
# False

# 110
# True

# 111
# False

# -1
# True

# 190
# True

# 209
# True

# 210
# True

# 211
# False

# -101
# False

# -209
# False
