import RPi.GPIO as GPIO
import time
import os

power_on_pin=2 #bcm
#This is to keep the raspberry pi on 
GPIO.setmode(GPIO.BCM)
GPIO.setup(power_on_pin,GPIO.OUT)
GPIO.output(power_on_pin,GPIO.HIGH)
