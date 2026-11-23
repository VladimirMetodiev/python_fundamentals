def in1to10(n, outside_mode):
    if not outside_mode:
        if n >= 1 and n <= 10:
            return True
        else:
            return False
    else:
        if n <= 1 or n >= 10:
            return True
        else:
            return False

n = int(input('n = '))
data = input().lower()
outside_mode = True if data == 'out' else False

print(in1to10(n, outside_mode))





# Given a number n, return True if n is in the range [1, 10], inclusive. 
# Unless outside_mode is True, in which case return True if the number 
# is less or equal to 1, or greater or equal to 10.
