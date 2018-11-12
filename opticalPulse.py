import sys
import RPi.GPIO as GPIO
from time import sleep
import os.path
def main():
    pin = 17
    pinpath = "./pulses/" + str(pin)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    if os.path.exists(pinpath) == False:
        with open(pinpath, 'w+') as f: f.write("0")

    lastState = False
    while True:
        state = GPIO.input(pin)
        if state and not lastState:
            with open(pinpath, 'r') as f: count = int(f.read())
            count += 1
            print("pulse #" + str(count))
            with open(pinpath, 'w') as f: f.write(str(count))
        lastState = state
        sleep(0.01)

if __name__ == '__main__':
    main()
