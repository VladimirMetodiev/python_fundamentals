def move_the_first_two_from_the_left(data):
    if len(data) <= 2:
        return data
    else:
        return data[2:] + data[:2]

data = input()
print(move_the_first_two_from_the_left(data))
