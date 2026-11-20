def extra_end(data):
    length = len(data)
    return data[length - 2:length] * 3

data = input()
print(extra_end(data))





# Даден е низ. Върнете нов низ, съставен от 3 копия на последните 2 символа 
# от оригиналния низ. Дължината на първият низ ще бъде най-малко 2.
