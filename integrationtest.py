import subprocess
import time
import sys
import RPi.GPIO as io
from omxplayer import OMXPlayer
import os

reed_switch_pin = 26 # board pin 39 , bcm 26
power_on_pin=14 #board pin = 8
shutdown_switch_pin=17 #board pin = 11

videorunning = False
videopaused = False
io.setmode(io.BCM)
io.setup(reed_switch_pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp
io.setup(power_on_pin,io.OUT)
io.output(power_on_pin,io.HIGH)
io.setup(shutdown_switch_pin, io.IN)

# set shutdown time to five minutes from now
shutdownnow = time.time()
shutdowntime = shutdownnow + 300


# do this continuously till shutdown
while True:
    # initialize variables
    pedals = 0
    prev_input = False
    startdisplay = False
    
    # set the variable now to be used for checking pedals
    now = time.time()
    future = now + 10

       # if now time is less than or equal to future
    while time.time() <= future:
        if io.input(shutdown_switch_pin): # Setup an if loop to run a shutdown command when button press sensed
            print("pressed")
            io.cleanup()
            os.system("sudo shutdown -h now") # Send shutdown command to os
        # increment pedals for each input to reed switch
        input = not io.input(reed_switch_pin)
        if (input):
            pedals += 1
            print("Number of pedals " + str(pedals))
            time.sleep(0.5)
            contpausetime = time.time() + 10
            while time.time() < contpausetime:
               # this is repeated code but idc
               if io.input(shutdown_switch_pin): # Setup an if loop to run a shutdown command when button press sensed
                  print("pressed")
                  io.cleanup()
                  os.system("sudo shutdown -h now") # Send shutdown command to os
               # if shutdown time greater than or equal to now, cleanup and shutdown
               if time.time() >= shutdowntime:
                  io.cleanup()
                  os.system("sudo shutdown -h now")   
               if io.input(reed_switch_pin):
                  break;
         # need to add code to see if there is continous signal to reed switch, 
         #then pause the video if there is continuous signla to reed switch
         #pausetime = time.time()+5
         #while not io.input and time.time() <= pausetime:
            
        # if detected enough pedals
        if pedals >= 5:
            # setting start display to true if amount of pedals is greater than 5 in 15 seconds
            startdisplay = True
            # resetting the shutdown time to 300 seconds from now
            shutdowntime = now + 300
            break
        # if shutdown time greater than or equal to now, cleanup and shutdown
        if time.time() >= shutdowntime:
            io.cleanup()
            os.system("sudo shutdown -h now")
    # if start display flag is set     
    if startdisplay:
      # if video is not running, kick off an new omxplayer instance
      if not videorunning:
         myprocess = subprocess.Popen(['omxplayer','--loop','/media/pi/BRIDGEWELL1/movie1.mp4'],stdin=subprocess.PIPE)
         videorunning = True
      # if video is only paused, play it back again
      if videopaused:
         myprocess.stdin.write('p')
         videopaused = False
    # if video was kicked off once, and it's not paused, and if startdisplay is set to false, pause the video
    elif videorunning and not videopaused:
      myprocess.stdin.write('p')
      videopaused = True
    # sleep to let the cpu rest
    time.sleep(0.5)
