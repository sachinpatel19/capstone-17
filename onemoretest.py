import subprocess
myprocess = subprocess.Popen(['omxplayer','-b','/home/pi/Video/movie1.mp4'],stdin=subprocess.PIPE)
sleep(10)
myprocess.stdin.write('q')
