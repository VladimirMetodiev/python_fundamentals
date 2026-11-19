def take_a_bite(some_str):
    temporary = [j for j in some_str]
    result = ''

    for j in range(0, len(temporary)):
        if j % 2 == 0:
            result += temporary[j]

    return result

data = input()
print(take_a_bite(data))



# Heeololeo
# Hello

# Valdaadriomaiir
# Vladimir

# Hi
# H

# HiHiHi
# HHH
