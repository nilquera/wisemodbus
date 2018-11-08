import sys
import RPi.GPIO as GPIO
from time import sleep
import os.path
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-p", help="Test in polling mode",
                    dest="polling")
group.add_argument("-i", help="Test in interruption mode",
                    dest="interruption")
group.add_argument("-b", help="Test in polling and interruption mode",
                    dest="both")

def pulseInterruption(channel):
    with open(str(channel), 'r') as f:
        totalCounts = int(f.read())
        totalCounts += 1
        print("int: " + str(totalCounts))
    with open(str(channel), 'w') as f:
        f.write(str(totalCounts))
    return

def setupGPIO(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(int(pin), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    if os.path.exists(pin) == False:
        with open(pin, 'w+') as f: f.write("0")

def main():
    args = parser.parse_args()

    if args.polling is not None: #Polling mode
        pin = args.polling
        setupGPIO(pin)
        lastState = False

        while True:
            state = GPIO.input(int(pin))
            if state == True and lastState == False:
                with open(pin, 'r') as f: count = int(f.read())
                count += 1
                print ("poll "+ str(count))
                with open(pin, 'w') as f: f.write(str(count))
            lastState = state
            sleep(0.01)

    elif args.interruption is not None: #Interruption mode
        pin = args.interruption
        setupGPIO(pin)
        GPIO.add_event_detect(int(pin), GPIO.RISING, callback = pulseInterruption, bouncetime = 150)
        try:
            while True:
                sleep(30)
        except KeyboardInterrupt:
            GPIO.cleanup()

    elif args.both is not None: #Both modes at the same time (useful to compare results)
        pin = args.both
        setupGPIO(pin)
        GPIO.add_event_detect(int(pin), GPIO.RISING, callback = pulseInterruption, bouncetime = 150)

        if os.path.exists(pin + "poll" ) == False:
            with open(pin + "poll", 'w+') as f: f.write("0")

        lastState = False
        while True:
            state = GPIO.input(int(pin))
            if state == True and lastState == False:
                with open(pin + "poll", 'r') as f: count = int(f.read())
                count += 1
                print ("poll " + str(count))
                with open(pin + "poll", 'w') as f: f.write(str(count))
            lastState = state
            sleep(0.01)

if __name__ == '__main__':
    main()
