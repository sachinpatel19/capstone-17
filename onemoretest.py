import subprocess
import time

myprocess = subprocess.Popen(['omxplayer','-b','/home/pi/Videos/movie1.mp4'],stdin=subprocess.PIPE)
time.sleep(10)
myprocess.stdin.write('p')
time.sleep(5)
myprocess.stdin.write('p')
time.sleep(10)
myprocess.stdin.write('q')
