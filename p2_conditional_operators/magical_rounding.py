def round10(num):
    if num % 10 == 0:
        return num
    if num >= 5 and num < 10 or num % 10 >= 5:
        return num + (10 - num % 10)
    else:
        return num - (num % 10)

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

a = int(input())
b = int(input())
c = int(input())

print(round_sum(a, b, c))



# 16
# 17
# 18
# 60

# 12
# 13
# 14
# 30

# 6
# 4
# 4
# 10

# 10
# 20
# 19
# 50





