def monkey_trouble(a_smile, b_smile):
    if (a_smile == True and b_smile == True) or (a_smile == False and b_smile == False):
        return True
    else:
        return False

a = input().lower()
a_smile = True if a == 'smile' else False
b = input()
b_smile = True if b == 'smile' else False

print(monkey_trouble(a_smile, b_smile))





# Условие

# Имаме две маймуни, a и b, а параметрите a_smile и b_smile 
# показват дали съответната маймуна се усмихва. Имаме проблем, 
# ако и двете се усмихват или ако никоя от тях не се усмихва. 
# Върнете True, ако имаме проблем.
