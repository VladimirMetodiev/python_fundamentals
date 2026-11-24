def get_middle(a, b):
    return [a[1], b[1]]

a = [int(j) for j in input().split(',')]
b = [int(k) for k in input().split(',')]

print(get_middle(a, b))
