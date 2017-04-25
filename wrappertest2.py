from pyomxplayer import OMXPlayer
omx = OMXPlayer('/home/pi/Videos/movie1.mp4')
sleep(10)
omx.toggle_pause()
sleep(2)
omx.toggle_pause()
