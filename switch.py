import time
import RPi.GPIO as io
io.setmode(io.BCM)

reed_switch_pin = 2
startdisplay = False

io.setup(reed_switch_pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp



while True:
    pedals = 0
    now = time.time()
    future = now + 10
    while time.time() <= future:
        if not io.input(reed_switch_pin):
            ++pedals
            print("Reed switch detected")
    if pedals >= 5:
        print("Starting display...")
        return True
