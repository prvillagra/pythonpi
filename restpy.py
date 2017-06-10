import threading
import RPi.GPIO as GPIO
import time
import time
import requests
from datetime import datetime

PIN = 4

class GPIOThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
                                    
            if GPIO.input(PIN) == True:                
                print("Panico pressionado!")
                panb = requests.get('http://pythonsecure.azurewebsites.net/api/SendHelp/1')
                if resp.status_code != 200:
                    # This means something went wrong.
                    raise ApiError('GET /SendHelp/ {}'.format(resp.status_code))
            else:
                print("Panico normalizado!")
                resp = requests.get('http://pythonsecure.azurewebsites.net/api/Normalize/1')
                if resp.status_code != 200:
                    # This means something went wrong.
                    raise ApiError('GET /Normalize/ {}'.format(resp.status_code))
                
            time.sleep(1)

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(PIN, GPIO.FALLING)
        
    gp_thread = GPIOThread()
    gp_thread.start()

    i = 0
    while True:
        
        print("Status do pino: ", PIN, GPIO.input(PIN))
        time.sleep(2)
        
if __name__ == "__main__":
    main()
    
##
##

##
##print(resp.json())

##
##for todo_item in resp.json():
##    print('Loja: '.todo_item['store_name']))
##
