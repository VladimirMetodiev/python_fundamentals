def ring(day, vacation):
    if not vacation:
        if day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
            return '7:00'
        else:
            return '10:00'
    else:
        if day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
            return '10:00'
        else:
            return 'off'

def get_a_number_from_0_to_6(text):
    while True:
        try:
            value = int(input(text))
            if value < 0 or value > 6:
                print('Error: The number must be between 0 and 6 inclusive')
            else:
                return value
        except ValueError:
            print('Error: please enter a valid number')


day = get_a_number_from_0_to_6('Day = ')
data = input().lower()
vacation = True if data == 'vacation' else False

print(ring(day, vacation))






# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, 3=Wed, 4=Thu, 5=Fri, 6=Sat, 
# and a boolean indicating if we are on vacation, return a string of the form "7:00" 
# indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" 
# and on the weekend it should be "10:00". Unless we are on vacation - then on weekdays 
# it should be "10:00" and weekends it should be "off".
