import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)

while True:
  print "GPIO Power on"
  GPIO.output(4,GPIO.HIGH)
