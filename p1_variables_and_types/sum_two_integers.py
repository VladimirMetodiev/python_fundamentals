def sum_double(a, b):
    total = a + b

    if a != b:
        return total
    else:
        return total * 2

a = int(input('a = '))
b = int(input('b = '))

print(sum_double(a, b))





# Дадени са две цели числа (тип int) върни тяхната сума, освен в случаите, 
# когато двете числа са еднакви. В такива случаи върни удвоената им сума.
