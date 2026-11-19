text = 'Ships on vigor of the waves are skimming'

# Аналог на `.indexOf(String str)` в Java
print(text.find('S'))            # 0
print(text.find('s'))            # 4
print(text.find('vigor'))        # 9
print(text.find('Valhalla'))     # - 1

print('=' * 30)

# Аналог на `.indexOf(String str, int fromIndex)` в Java
print(text.find('wave', 14))                  # 22
print(text.find('s', text.find('s') + 1))     # 26

print('=' * 30)

# Аналог на `.indexOf(String str, int beginIndex, endIndex)` в Java
print(text.find('o', 5, 18))                  # 6

print('=' * 30)

# Обхождане на всички срещания

current_index = text.find('s')

while current_index != -1:
    print(current_index)
    current_index = text.find('s', current_index + 1)

print('=' * 30)

try:
    print(text.index('S'))            # 0
    print(text.index('s'))            # 4
    print(text.index('vigor'))        # 9
    print(text.index('Valhalla'))     # ValueError
except ValueError:
    print('There is not such substring')

print('=' * 30)

print(text.count('s'))            # 3
print(text.count('vigor'))        # 1
print(text.count('Valhalla'))     # 0

# Методите `str.find('sub')` и `str.index('sub')` търсят индекса на първото срещане на подниза.
# `str.find('sub')` връща -1, ако подниза не е намерен.
# `str.index('sub')` хвърля грешка, ако подниза не е намерен.
# `str.count('sub')` връща броя на срещанията на подниза.
