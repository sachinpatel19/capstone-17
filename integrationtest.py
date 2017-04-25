import subprocess
import time
import sys
import RPi.GPIO as io
from omxplayer import OMXPlayer
import os

reed_switch_pin = 26 # board pin 39 , bcm 26
videorunning = False
videopaused = False
io.setmode(io.BCM)
io.setup(reed_switch_pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp

while True:
    pedals = 0
    startdisplay = False
    now = time.time()
    future = now + 30
    shutdowntime = now + 100
    if time.time() >= shutdowntime:
        io.cleanup()
        os.system("sudo shutdown -h now")
    while time.time() <= future:
        if not io.input(reed_switch_pin):
            pedals += 1
            print("Number of pedals " + str(pedals))
            time.sleep(0.5)
            while True:
                if io.input(reed_switch_pin):
                    break
            # todo: if reed switch continuously on, don't do anything
        if pedals >= 5:
            # setting start display to true if amound of pedals is greater than 5 in 15 seconds
            startdisplay = True
            shutdowntime = now + 100
            break
            
    if startdisplay:
        if not videorunning:
            myprocess = subprocess.Popen(['omxplayer','-b','/home/pi/Videos/movie1.mp4'],stdin=subprocess.PIPE)
            videorunning = True
        if videopaused:
            myprocess.stdin.write('p')
            videopaused = False
    elif videorunning and not videopaused:
        myprocess.stdin.write('p')
        videopaused = True
    time.sleep(0.5)
    

    
    # shutdown system after 5 minutes, shut down the pi 
    

