def not_string(some_str):
    if some_str.startswith('not'):
        return some_str
    else:
        return 'not ' + some_str

some_str = input().lower()
print(not_string(some_str))





# Условие

# Даден е низ. Върнете нов низ, в началото на който е добавено "not ". 
# Ако обаче низът вече започва с "not", върнете низа без промени.
