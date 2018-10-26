from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import pymodbus.exceptions as exceptions
import math

usb = "/dev/ttyUSB0"

try:
    client = ModbusClient(method='rtu', port=usb, stopbits=1, bytesize=8, baudrate=9650, timeout=1)
    client.connect()
except Exception as e:
    print(e)



rr = client.read_input_registers(address=514, count=2, unit=1)
print(rr)

#escale = client.read_input_registers(address=513, count=1, unit=1).registers[0]

#high = rr.registers[0]
#low = rr.registers[1]
#raw_value = high*65536 + low
#value = raw_value * math.pow(10, escale-6)
#print(value)
