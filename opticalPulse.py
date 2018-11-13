import sys
import RPi.GPIO as GPIO
from time import sleep
import os.path
def main():
    pin = 17
    pinpath = "./pulses/" + str(pin)
    kwhpath = "./pulses/kwh_" + str(pin)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    if os.path.exists(pinpath) == False:
        with open(pinpath, 'w+') as f: f.write("0")
    if os.path.exists(kwhpath) == False:
        with open(kwhpath, 'w+') as f: f.write("0")

    with open(pinpath, 'r') as f: pulses = int(f.read())
    with open(kwhpath, 'r') as f: kwh = int(f.read())

    lastState = False
    while True:
        state = GPIO.input(pin)
        if state and not lastState:
            pulses += 1
            print(str(kwh) + " KWh | pulse #" + str(pulses))
            with open(pinpath, 'w') as f: f.write(str(pulses))
        lastState = state
        sleep(0.01)

        if (pulses >= 1000):
            kwh += 1
            with open(kwhpath, 'w+') as f: f.write(str(kwh))
            pulses = 0
            with open(pinpath, 'w+') as f: f.write(str(pulses))

if __name__ == '__main__':
    main()
