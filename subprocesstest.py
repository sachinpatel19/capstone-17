import os
import subprocess
from sys import argv

os.mkfifo("pipeline")

subprocess.call(['rm','./pipeline'])
subprocess.call(['chmod', '+x', 'mkfifoscript.sh'])
#subprocess.call(['./mkfifoscript.sh'])
subprocess.call(['omxplayer', '-o', 'hdmi', '"$*"', '<' './pipeline', '&'])

print "opening file"
target = open("pipeline", 'w')
#subprocess.call(['echo', '-n', '/home/pi/Videos/movie1.mp4', '>', './pipeline'])
print "writing to file"
target.write("/home/pi/Videos/movie1.mp4")


