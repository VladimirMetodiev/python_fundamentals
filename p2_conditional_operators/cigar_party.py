def rate_the_party_with_cigars(cigars, is_weekend):
    if (is_weekend == False and cigars >= 40 and cigars <= 60) or \
        (is_weekend == True and cigars >= 40 ):
        return True
    else:
        return False

cigars = int(input())
is_weekend = True if input().lower() == 'weekend ' else False

print(rate_the_party_with_cigars(cigars, is_weekend))





# Когато катериците се събират на парти, те обичат да пушат пури. 
# Партито на катериците се счита за успешно, когато броят на пурите 
# е между 40 и 60 включително. Освен ако не е уикенд, тогава няма 
# горна граница за броя на пурите. Върни True, ако партито с дадените 
# стойности е успешно, в противоположния случай върни False.
