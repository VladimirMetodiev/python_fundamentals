def get_lucky_sum(a, b, c):
    result = 0
    if a == 13:
        return result
    else:
        result += a
        if b == 13:
            return result
        else:
            result += b
            if c == 13:
                return result
            else:
                return result + c

try:
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))

    print(get_lucky_sum(a, b, c))
except ValueError:
    print('invalid integer')
