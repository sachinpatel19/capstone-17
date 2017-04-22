import time
import sys
import RPi.GPIO as io

io.setmode(io.BCM)

reed_switch_pin = 26
startdisplay = False

io.setup(reed_switch_pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp

while True:
    pedals = 0
    now = time.time()
    future = now + 10
    while time.time() <= future:
        if not io.input(reed_switch_pin):
            pedals += 1
            print("Number of pedals " + str(pedals))
            time.sleep(0.5)
        if pedals >= 5:
            startdisplay = True
            break
    if startdisplay:
        print("Starting video...")
        sys.exit(0)

