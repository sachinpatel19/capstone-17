# Import the libraries to use time delays, send os commands and access GPIO pins
import RPi.GPIO as GPIO
import time
import os
#GPIO.cleanup()
power_on_pin=14 #board pin = 7
shutdown_switch_pin=17 #board pin = 11
#This is to keep the raspberry pi on 
GPIO.setmode(GPIO.BCM)
#print("setting gpio pin to high\n")
GPIO.setup(power_on_pin,GPIO.OUT)
GPIO.output(power_on_pin,GPIO.HIGH)

#print("setting gpio pin to input\n")
GPIO.setup(shutdown_switch_pin, GPIO.IN)
#time.sleep(1)
while True: # Setup a while loop to wait for a button press
   if GPIO.input(shutdown_switch_pin): # Setup an if loop to run a shutdown command when button press sensed
      print("pressed")
      GPIO.cleanup()
      os.system("sudo shutdown -h now") # Send shutdown command to os
   time.sleep(1) # Allow a sleep time of 1 second to reduce CPU usage
