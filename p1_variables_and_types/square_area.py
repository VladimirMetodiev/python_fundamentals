a = -1.0

while True:
    try:
        a = float(input('Enter a length of side a: '))
        if a <= 0:
            print('Error: the number must be greater than zero')
        else:
            break
    except ValueError:
        print('Error: please enter a valid number')

area = a * a
print(f'Square area: {area:.2f}')
