# Import the libraries to use time delays, send os commands and access GPIO pins
import RPi.GPIO as GPIO
import time
import os

shutdown_switch_pin=17 #board pin = 11
#This is to keep the raspberry pi on 
GPIO.setmode(GPIO.BCM)
GPIO.setup(shutdown_switch_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True: # Setup a while loop to wait for a button press
   if GPIO.input(shutdown_switch_pin): # Setup an if loop to run a shutdown command when button press sensed
      print("BUTTON PRESSED")
      #time.sleep(3)
      break
   time.sleep(1) # Allow a sleep time of 1 second to reduce CPU usage
