def get_the_beginning(some_str):
    beginning = ''

    if len(some_str) >= 3:
        beginning = some_str[0:3]
    else:
        beginning = some_str

    return beginning + beginning + beginning

data = input()
print(get_the_beginning(data))





# Даден е низ. Приема се, че "началната част" са първите 3 символа от низа. 
# Ако дължината на низа е по-малка от 3, началната част е това, от което се 
# състои низа. Върнете нов низ, състоящ се от 3 копия на началната част.



# Тестове

# Anna
# AnnAnnAnn

# Java
# JavJavJav

# :)
# :):):)
