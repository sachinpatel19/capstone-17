import subprocess
from sys import argv

subprocess.call(['rm','./pipeline'])
subprocess.call(['chmod', '+x', 'mkfifoscript.sh'])


print "opening file"
target = open("pipeline", 'w')
#subprocess.call(['echo', '-n', '/home/pi/Videos/movie1.mp4', '>', './pipeline'])
print "writing to file"
target.write("/home/pi/Videos/movie1.mp4")
target.write("\n")
subprocess.call(['./mkfifoscript.sh'])
