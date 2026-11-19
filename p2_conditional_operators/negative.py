def pos_neg(a, b, negative):
    if negative == True:
        if a < 0 and b < 0:
            return True
        else:
            return False
    else:
        if (a < 0 and b > 0) or (a > 0 and b < 0):
            return True
        else:
            return False

a = int(input('a = '))
b = int(input('b = '))

current = input()
negative = True if current == 'negative' else False

print(pos_neg(a, b, negative))





# При две целочислени стойности се връща True, ако едната 
# е отрицателна, а другата е положителна. Освен ако параметъра 
# "negative" е True. В такъв случай се връща True, само ако и 
# двете стойности са отрицателни.
