import subprocess
import time
import sys
import RPi.GPIO as io
from omxplayer import OMXPlayer

#movie1 = ("/home/pi/Videos/movie1.mp4")

reed_switch_pin = 26 # board pin 39 , bcm 26
videorunning = False
videopaused = False
io.setmode(io.BCM)
io.setup(reed_switch_pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp

while True:
    pedals = 0
    startdisplay = False
    now = time.time()
    future = now + 15
    while time.time() <= future:
        if not io.input(reed_switch_pin):
            pedals += 1
            print("Number of pedals " + str(pedals))
            time.sleep(0.5)
            # todo: if reed switch continuously on, don't do anything
        if pedals >= 5:
            # setting start display to true if amound of pedals is greater than 5 in 15 seconds
            startdisplay = True
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
   
    
        # start video
        # stop video
        #print("Starting video...")
        #os.system('killall omxplayer.bin')
        #omxc = Popen(['omxplayer', '-b', movie1])
    #else:
        
    # if every 15 second, 5 revolution, then keep it ON otherwise pause it
    # after 5 revolution reset the time
   

    # after 5 minutes of doing nothing kill the system
    
    # shutdown system after 5 minutes, shut down the pi 
    

