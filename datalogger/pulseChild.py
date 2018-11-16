import sys
import time
import json
import os.path
from time import sleep
import RPi.GPIO

pullDict = {
    'up': GPIO.PUD_UP,
    'down': GPIO.PUD_DOWN
}

def main():
    counter = sys.argv[1]
    with open('../configFiles/configGeneral.json', 'r') as configFile:
        configJSON = json.load(configFile)
    counterJSON = configJSON['DataSources']['PulseCounter'][int(counter)]

    pin = counterJSON['pin']
    pinpath = 'counters/' + str(pin)
    pull = counterJSON['pull']

    if os.path.exists(pinpath) == False:
        with open(pinpath, 'w+') as f:
            f.write("0")
            count = 0
    else:
        with open(pinpath, 'r') as f:
            count = int(f.read())

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(int(pin), GPIO.IN, pull_up_down=pullDict[pull])

    if pull == 'up': lastState = 1
    elif pull == 'down': lastState = 0

    print('Starting pin ' + str(pin) + '...')
    sleep(1)

    while True:
        state = GPIO.input(int(pin))
        if pull == 'up' and not state and lastState:
            sleep(0.001)
            state = GPIO.input(int(pin))
            if not state:
                count += 1
                print('pulse #' + str(count))
                with open(pinpath, 'w') as f: f.write(str(count))
        elif pull == 'down' and state and not lastState:
            sleep(0.001)
            state = GPIO.input(int(pin))
            if state:
                count += 1
                print('pulse #' + str(count))
                with open(pinpath, 'w') as f: f.write(str(count))
        lastState = state
        sleep(0.01)
            
if __name__ == '__main__':
    main()
