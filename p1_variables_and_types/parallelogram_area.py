import math

def get_a_positive_number(text: str) -> float:
    while True:
        try:
            value = float(input(text))
            if value <= 0:
                print('Error: the number must be greater than zero')
            else:
                return value
        except ValueError:
            print('Error: please enter a valid number')

def get_a_valid_angle(text: str) -> float:
    while True:
        try:
            value = float(input(text))
            if value >= 180:
                print('Error: the angle of a parallelogram must be less than 180 degrees')
            else:
                return value
        except ValueError:
            print('Error: please enter a valid number')

def calculate_parallelogram_area(a: float, b: float, angle_degrees: float) -> float:
    angle_radians = math.radians(angle_degrees)
    area = a * b * math.sin(angle_radians)
    return area

a = get_a_positive_number('Length of side a: ')
b = get_a_positive_number('Length of side b: ')
angle_degrees = get_a_valid_angle('Enter an angle in degrees: ')

area = calculate_parallelogram_area(a, b, angle_degrees)
print(f'Parallelogram area: {area:.2f}')



# БЕЛЕЖКИ ПО ЗАДАЧАТА

# Функцията `math.sin()` приема като аргумент радиани, а не градуси.
# Градусите мога да преобразувам в радиани чрез функцията `math.radians()`, 
# или чрез формулата `radians = degrees * (PI / 180)`.

# Формулата за лице на успоредник е `S = a * b * sin angle`
