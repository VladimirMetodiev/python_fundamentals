import re

def count_code(some_str: str) -> int:
    pattern = r'co.e'
    return len(re.findall(pattern, some_str))

some_str = input().lower()
print(count_code(some_str))
