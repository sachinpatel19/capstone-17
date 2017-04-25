import subprocess
from sys import argv

subprocess.call(['rm','./pipeline'])
subprocess.call(['chmod', '+x', 'mkfifoscript.sh'])
subprocess.call(['./mkfifoscript.sh'])

target = open("pipeline", 'w')
#subprocess.call(['echo', '-n', '/home/pi/Videos/movie1.mp4', '>', './pipeline'])
target.write("/home/pi/Videos/movie1.mp4")

