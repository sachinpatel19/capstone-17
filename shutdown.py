# Import the libraries to use time delays, send os commands and access GPIO pins
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setmode(GPIO.BOARD) # Set pin numbering to board numbering
#GPIO.setup(10, GPIO.IN) # Setup pin 7 as an input

while True: # Setup a while loop to wait for a button press
   if(GPIO.input(10)): # Setup an if loop to run a shutdown command when button press sensed
      print("shutdown will initiate in 3..2..1..")
      time.sleep(3)
      #os.system("sudo shutdown -h now") # Send shutdown command to os
      break
   time.sleep(1) # Allow a sleep time of 1 second to reduce CPU usage
