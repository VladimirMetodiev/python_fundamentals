def sleep_in(weekday, vacation):
    if weekday == False or vacation == True:
        return True
    else:
        return False

w = input().lower()
v = input().lower()

weekday = False
vacation = False

if w == 'monday' or w == 'tuesday' or w == 'wednesday' or w == 'thursday' or w == 'friday':
    weekday = True

if v == 'vacation':
    vacation = True

print(sleep_in(weekday, vacation))





# Параметърът "weekday" е True, ако е делничен ден, а параметърът "vacation" е True, 
# ако сме в отпуск. Спим до късно, ако не е делничен ден или сме в отпуск. 
# Върнете True, ако спим до късно.
