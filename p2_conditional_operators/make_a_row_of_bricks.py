def make_bricks(small, big, goal):
    if big * 5 == goal:
        return True
    elif big * 5 > goal:
        remainder = goal % 5
        if small >= remainder:
            return True
        else:
            return False
    else:
        remainder = goal - (5 * big)
        if small >= remainder:
            return True
        else:
            return False

small = int(input())
big = int(input())
goal = int(input())
print(make_bricks(small, big, goal))





# We want to make a row of bricks that is goal inches long. 
# We have a number of small bricks (1 inch each) and big 
# bricks (5 inches each). Return True if it is possible to 
# make the goal by choosing from the given bricks. This is 
# a little harder than it looks and can be done without any loops.



# Tests

# 9
# 0
# 10
# False

# 0
# 2
# 12
# False

# 3
# 1
# 8
# True

# 3
# 1
# 9
# False

# 3
# 2
# 8
# True

# 3
# 2
# 10
# True

# 7
# 1
# 12
# True

# 5
# 0
# 5
# True

# 1
# 5
# 12
# False

# 40
# 2
# 49
# True

# 22
# 2
# 33
# False
