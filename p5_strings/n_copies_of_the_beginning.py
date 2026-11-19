def front_times(some_str, n):
    beginning = ''
    result = ''

    if len(some_str) >= 3:
        beginning = some_str[0:3]
    else:
        beginning = some_str

    for j in range(n):
        result += beginning

    return result

some_str = input()
n = int(input())

print(front_times(some_str, n))





# Даден е низ и неотрицателно цяло число n. Ще приемем, че началната част на низът 
# се състои от първите 3 символа, или ако дължината на низа е по-малка от 3, от това 
# от което е съставен низа. Върнете n копия на началната част.
