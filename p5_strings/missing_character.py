def missing_char(some_str, n):
    current = [j for j in some_str]
    result = ''

    for j in range(0, len(current)):
        if j != n:
            result += current[j]

    return result

some_string = input("Enter some text: ")
index = int(input('Enter a valid index: '))

print(missing_char(some_string, index))





# Description

# Given a non-empty string and an int n, return a new string 
# where the char at index n has been removed. The value of n 
# will be a valid index of a char in the original string.



# Enter some text: aabccc
# Enter a valid index: 2
# aaccc

# Enter some text: lana
# Enter a valid index: 0
# ana
