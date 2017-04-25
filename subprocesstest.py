import subprocess

subprocess.call(['./mkfifoscript.sh'])
subprocess.call('echo -n /home/pi/Videos/movie1.mp4 > ./pipeline')


