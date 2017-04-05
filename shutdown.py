# Import the libraries to use time delays, send os commands and access GPIO pins
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD) # Set pin numbering to board numbering
GPIO.setup(11, GPIO.IN) # Setup pin 7 as an input
while True: # Setup a while loop to wait for a button press
   if(GPIO.input(11)): # Setup an if loop to run a shutdown command when button press sensed
   os.system("sudo shutdown -h now") # Send shutdown command to os
    break
   time.sleep(1) # Allow a sleep time of 1 second to reduce CPU usage
