def squirrel_play(temp, is_summer):
    if is_summer == False and temp >= 60 and temp <= 90 or \
        is_summer == True and temp >= 60 and temp <= 100:
        return True
    else:
        return False

temperature = int(input())
is_summer = True if input().lower() == 'summer' else False

print(squirrel_play(temperature, is_summer))





# Катериците в Пало Алто прекарват по-голямата част от деня си в игри. 
# Те си играят, ако температурата е между 60 и 90 (включително). Освен 
# ако не е лято. Тогава горната граница е 100 вместо 90. Дадени са цяло 
# число `temperature` и булева променлива `is_summer`. Върнете True ако 
# катериците си играят и False в противоположния случай.
