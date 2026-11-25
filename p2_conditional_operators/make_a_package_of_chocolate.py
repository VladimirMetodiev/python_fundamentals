def make_chocolate(small, big, goal):
    if big * 5 == goal:
        return 0
    elif big * 5 > goal:
        remainder = goal % 5
        if small >= remainder:
            return remainder
        else:
            return -1
    else:
        remainder = goal - (5 * big)
        if small >= remainder:
            return remainder
        else:
            return -1

small = int(input())
big = int(input())
goal = int(input())
print(make_chocolate(small, big, goal))





# We want make a package of goal kilos of chocolate. We have 
# small bars (1 kilo each) and big bars (5 kilos each). Return 
# the number of small bars to use, assuming we always use big bars 
# before small bars. Return -1 if it can't be done.
