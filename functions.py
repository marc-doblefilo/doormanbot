import time

stop_countdown = False

def countdown(number):
    while number > 0:
        if stop_countdown == False:
            number = number - 1
            time.sleep(1)
            if (number == 0):
                return True
        elif stop_countdown == True:
            return False