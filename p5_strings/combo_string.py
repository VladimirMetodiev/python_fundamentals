def get_combo_string(a, b):
    length_a = len(a)
    length_b = len(b)

    outside = a if length_a < length_b else b
    inside = b if length_b > length_a else a

    return '{0}{1}{0}'.format(outside, inside)

a = input()
b = input()

print(get_combo_string(a, b))




# Дадени са 2 низа, a и b. Върнете низ във формата "къс+дълъг+къс", като по-късият низ е отвън, 
# а по-дългият е отвътре. Низовете няма да са с еднаква дължина, но единия може да бъде празен.



# Тест

# BB
# A
# ABBA
