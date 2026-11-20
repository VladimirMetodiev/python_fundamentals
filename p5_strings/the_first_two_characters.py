def get_the_first_two(data):
    if len(data) <= 2:
        return data
    else:
        return data[:2]

data = input()
print(get_the_first_two(data))
