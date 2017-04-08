import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(8,GPIO.OUT)

while True:
  print "GPIO Power on"
  GPIO.output(8,GPIO.HIGH)
