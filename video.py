import sys
import os
from subprocess import Popen

movie1 = ("/home/pi/Videos/movie1.mp4")



while True:
    os.system('killall omxplayer.bin')
    omxc = Popen(['omxplayer', '-b', movie1])
    while time.time() >= future:
        sys.exit(0)

