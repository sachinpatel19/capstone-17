import sys
import os
from subprocess import Popen
import time

movie1 = ("/home/pi/Videos/movie1.mp4")
now = time.time()
future = now + 10

while True:
    os.system('killall omxplayer.bin')
    omxc = Popen(['omxplayer', '-b', movie1])
    while True:
        if time.time() >= future:
            os.system('killall omxplayer.bin')
            break
    break
    print("blah")
sys.exit(0)
