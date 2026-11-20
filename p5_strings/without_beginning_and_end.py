def get_without_beginning_and_end(data):
    return data[1:(len(data) - 1)]

data = input()
print(get_without_beginning_and_end(data))





# При даден низ се връща версия без първия и последния символ, т.е. от 
# "Hello" се получава "ell". Дължината на низа ще бъде най-малко 2.
