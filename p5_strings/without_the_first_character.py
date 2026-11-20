def get_it_without_the_first_one(a, b):
    return a[1:] + b[1:]

a = input()
b = input()

print(get_it_without_the_first_one(a, b))
