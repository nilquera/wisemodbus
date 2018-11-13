## wisemodbus
Scripts to test modbus meters in various protocols.

---

# Optical Pulse Reader
1. Red-3.3V Black-GND Blue-deserved Pin (the program is configured to use 17 by default)
2. Attach the pulse reader exactly above the pulse LED and check it detects pulses. It should generate it's own LED flash everytime it gets a pulse from behind.
3. Inside the RPi, modify opticalPulse.py's variable 'cyclelength' to your convenience. If, for example, the meter generates 1000 flashes for every KWh, then the value must be 1000.
4. Stablish connection with the RPi and execute "python3 ~/home/wisemodbus/opticalPulse.py". Values can be read either on screen or inside ~/home/wisemodbus/pulses/
