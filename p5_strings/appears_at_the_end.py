def end_other(a, b):
    a = a.lower()
    b = b.lower()
    length_a = len(a)
    length_b = len(b)

    if length_a >= length_b:
        end_a = a[(length_a - length_b):]
        return True if end_a == b else False
    else:
        end_b = b[(length_b - length_a):]
        return True if end_b == a else False

a = input()
b = input()

print(end_other(a, b))






# Дадени са два низа. Върнете True, ако някой от низовете се появява 
# в края на другия низ. Разликите между главни и малки букви трябва 
# да бъдат пренебрегнати (с други думи, изчислението не трябва да 
# бъде "чувствително към регистъра").
