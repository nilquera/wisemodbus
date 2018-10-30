from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import pymodbus.exceptions as exceptions
import math

usb = "/dev/ttyUSB0"

try:
    client = ModbusClient(method='rtu', port=usb, stopbits=1, bytesize=8, baudrate=9600, timeout=1)
    client.connect()
    rr = client.read_input_registers(address=514, count=2, unit=1)
    print(rr.registers)
except Exception as e:
    print(e)
