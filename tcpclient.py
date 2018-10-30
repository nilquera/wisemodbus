from pymodbus.client.sync import ModbusTcpClient
import pymodbus.exceptions as exceptions
ip = "192.168.143.112"
port = 502
try:
    client = ModbusTcpClient(ip, port)
    client.connect()

    rr = client.read_input_registers(address=0, count=2, unit=1)
    print(rr.registers)
except Exception as e:
    print(e)
