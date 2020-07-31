import time

stop_countdown = False

def countdown(seconds):
    while seconds > 0:
        if stop_countdown == False:
            seconds = seconds - 1
            time.sleep(1)
            if (seconds == 0):
                return True
        elif stop_countdown == True:
            return False