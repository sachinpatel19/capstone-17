import time
import RPi.GPIO as io
io.setmode(io.BCM)

door_pin = 2

io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp

while True:
    if io.input(door_pin):
        print("Reed switch detected")
    time.sleep(1)
