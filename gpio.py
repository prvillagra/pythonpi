import threading
import RPi.GPIO as GPIO
import time
import time
from datetime import datetime
#import picamera

i=0
j=0
#camera= picamera.PiCamera()
#camera.resolution = (640, 480)
PIN = 4

class GPIOThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)              

    def run(self):
        while True:
            if GPIO.input(PIN) == False: # adjust this statement as per your pin status i.e HIGH/LOW
                global j
                j+=1
                #camera.close()
                print "handling button event"
                print("pressed",str(datetime.now()))
                time.sleep(4)
                #camera.capture( 'clicked%02d.jpg' %j )

def main():

      GPIO.setmode(GPIO.BCM)
      GPIO.setwarnings(False)
      GPIO.setup(PIN,GPIO.IN,pull_up_down=GPIO.PUD_UP)    
      GPIO.add_event_detect(PIN,GPIO.FALLING)

      gpio_thread = GPIOThread()
      gpio_thread.start() 

      while True or i < 20:
          global i
          print "Hello world! {0}".format(i)
          i=i+1
          time.sleep(5)


if __name__=="__main__":
    main()
