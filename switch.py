import time
import RPi.GPIO as io
io.setmode(io.BCM)

door_pin = 2
x = True
io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp

while True:
    x = not x
    if io.input(door_pin):
        if x:
            print("Reed switch detected 1" )
        else:
            print("Reed switch detected 2" )
    time.sleep(1)
