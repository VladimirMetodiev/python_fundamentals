def front_back(some_str):
    if len(some_str) <= 1:
        return some_str
    
    current = [j for j in some_str]
    temporary = current[0]
    last_index = len(current) - 1
    current[0] = current[last_index]
    current[last_index] = temporary

    return ''.join(current)

text = input()
print(front_back(text))



# Description

# Given a string, return a new string where the first and last chars have been exchanged.
