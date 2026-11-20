import math

a = -1.0
angle = 180.0

while True:
    try:
        a = float(input('Enter a length of side a: '))
        if a <= 0:
            print('Error: the number must be greater than zero')
        else:
            break
    except ValueError:
        print('Error: please enter a valid number')

while True:
    try:
        angle = float(input('Enter an angle in degrees: '))
        if angle <= 0 or angle >= 180:
            print('Error: the angle must be between 0 and 180 degrees')
        else:
            break
    except ValueError:
        print('Error: please enter a valid number')

angle_radians = math.radians(angle)
area = a * a * math.sin(angle_radians)

print(f'Rhombus area: {area:.2f}')



# БЕЛЕЖКИ ПО ЗАДАЧАТА

# Функцията `math.sin()` приема като аргумент радиани, а не градуси.
# Градусите мога да преобразувам в радиани чрез функцията `math.radians()`, 

# Формулата за лице на ромб е `S = a * a * sin angle`
