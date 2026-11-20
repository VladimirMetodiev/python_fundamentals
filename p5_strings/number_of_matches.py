def string_match(a, b):
    counter = 0
    length_a = len(a)
    length_b = len(b)
    length = length_a if length_a >= length_b else length_b

    for j in range(length - 1):
        if a[j:j+2] == b[j:j+2]:
            counter += 1

    return counter

a = input()
b = input()

print(string_match(a, b))





# Given 2 strings, a and b, return the number of the positions 
# where they contain the same length 2 substring.
