import subprocess
import time

myprocess = subprocess.Popen(['omxplayer','-b','/home/pi/Video/movie1.mp4'],stdin=subprocess.PIPE)
time.sleep(10)
myprocess.stdin.write('q')
