import subprocess
subprocess.call(['rm -f pipeline'])
subprocess.call(['chmod +x mkfifoscript.sh'])
subprocess.call(['./mkfifoscript.sh'])
subprocess.call(['echo -n /home/pi/Videos/movie1.mp4 > pipeline'])


