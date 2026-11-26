def get_cat_and_dog(some_str):
    return True if some_str.count('cat') == some_str.count('dog') else False

some_str = input().lower()
print(get_cat_and_dog(some_str))
