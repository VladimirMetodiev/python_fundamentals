def caught_speeding(speed: int, is_birthday: bool) -> int:
    
    if is_birthday == True:
        if speed >= 86:
            return 2
        elif speed >= 66 and speed <= 85:
            return 1
        else:
            return 0
    else:
        if speed >= 81:
            return 2
        elif speed >= 61 and speed <= 80:
            return 1
        else:
            return 0

def get_a_positive_speed(text: str) -> int:
    while True:
        try:
            sp = int(input(text))
            if sp <= 0:
                print('Error: the speed must be greater than zero')
            else:
                return sp
        except ValueError:
            print('Error: please enter a valid speed')

speed = get_a_positive_speed('Speed: ')
is_birthday = True if input().lower() == 'birthday' else False

print(caught_speeding(speed, is_birthday))





# Карате бързо и полицаите ви спират. Напишете код, който да изчисли резултата, 
# кодиран като цяло число (int): 0 == няма глоба, 1 == малка глоба, 2 == голяма глоба. 
# Ако скоростта е 60 или по-малко, резултатът е 0. Ако скоростта е между 61 и 80 включително, 
# резултатът е 1. Ако скоростта е 81 или повече, резултатът е 2. Освен ако не е 
# рождения ви ден. На този ден скоростта ви може да бъде с 5 по-висока във всички случаи.
