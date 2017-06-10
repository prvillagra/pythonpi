import RPi.GPIO as GPIO
import sys

status = sys.argv[1]

PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN, GPIO.OUT, initial=GPIO.LOW)

if status == "1":
    print("Ligando: ", status)
    GPIO.output(PIN, GPIO.HIGH)    
else:
    GPIO.output(PIN, GPIO.LOW)
    print("Desligando: ", status)
