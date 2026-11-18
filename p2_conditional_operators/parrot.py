def parrot_trouble(talking, hour):
    if talking == True and (hour < 7 or hour > 20):
        return True
    else:
        return False

t = input()
hour = int(input())
talking = True if t == 'talking' else False

print(parrot_trouble(talking, hour))





# Имаме папагал, който говори силно. Параметърът "hour" представлява текущия час 
# в диапазона от 0 до 23. Имаме проблем, ако папагалът говори, а часът е преди 7 
# или след 20. Върнете True, ако имаме проблем.
