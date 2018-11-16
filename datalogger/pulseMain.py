"""
This script executes as many concurrent processes as pulse sources are indicated by generalConfig file
"""
import json
import subprocess

def main():
    configFile = open('../configFiles/configGeneral.json', 'r')
    configJSON = json.load(configFile)
    countersArray = configJSON['DataSources']['PulseCounter']
    for i in range(0,len(countersArray)):
        print(i)
        print(countersArray[i]['pin'])
        subprocess.Popen(['python3', './pulseChild.py', str(i)])

if __name__ == '__main__':
    main()
