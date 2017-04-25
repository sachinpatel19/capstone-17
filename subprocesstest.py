import os
import subprocess
from sys import argv

#os.mkfifo("/tmp/pipeline")


#subprocess.call(['chmod', '+x', 'mkfifoscript.sh'])
#subprocess.call(['./mkfifoscript.sh'])
subprocess.call('omxplayer -o hdmi "$*" < /tmp/pipeline &')

print "opening file"
#target = open("/tmp/pipeline", 'w')
subprocess.call('echo -n /home/pi/Videos/movie1.mp4 > /tmp/pipeline')
#print "writing to file"
#target.write("/home/pi/Videos/movie1.mp4")


