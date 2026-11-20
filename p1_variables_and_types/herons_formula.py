import math

def get_positive_input(text: str) -> float:
    while True:
        try:
            value = float(input(text))
            if value <= 0:
                print('Error: the number must be greater than zero')
            else:
                return value
        except ValueError:
            print('Error: please enter a valid number')

def calculate_the_area_of_a_triangle(a: float, b: float, c: float) -> float:
    p = (a + b + c) / 2.0
    area = p * (p - a) * (p - b) * (p - c)
    if area <= 0:
        raise ValueError("The values don't form a valid triangle")
    return math.sqrt(area)

a = get_positive_input('a = ')
b = get_positive_input('b = ')
c = get_positive_input('c = ')

try:
    print('The area of the triangle is: %.2f' % (calculate_the_area_of_a_triangle(a, b, c)))
except ValueError as e:
    print(e)



# Tests

# 4
# 13
# 15
# 24.00

# 8
# 6.2
# 5.7
# 17.58
