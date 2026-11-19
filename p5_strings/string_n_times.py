def string_times(some_str, n):
    result = ''

    for j in range(n):
        result += some_str

    return result

data = input()
n = int(input())

print(string_times(data, n))





# Description

# Given a string and a non-negative int n, return a larger string 
# that is n copies of the original string.
