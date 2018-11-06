from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import pymodbus.exceptions as exceptions
import sys

def loopOnAddr(client, idunit, start, end):
    print("id: " + idunit)
    print("address: " + start + "-" + end)
    for addr in range(int(start), int(end)):
        try:
            rr = client.read_input_registers(unit=int(idunit), address=addr, count=2)
            print(rr.registers)
        except Exception as e:
            print(e)
    return

def readValue(client, idunit, addr):
    print("id: " + str(idunit))
    print("address: " + str(addr))
    try:
        rr = client.read_input_registers(unit=int(idunit), address=int(addr), count=2)
        print(rr.registers)
    except Exception as e:
        print(e)
    return


def main(argv): 
    usb = "/dev/ttyUSB0"
    #loop = 1
    #usb = "/dev/modbus" + str(loop)
    client = ModbusClient(method='rtu', port=usb, stopbits=1, bytesize=8, baudrate=9600, timeout=1)
    client.connect()
    
    #readValue(client, argv[0], argv[1])    
    loopOnAddr(client, argv[0], argv[1], argv[2])    




if __name__ == '__main__':
    main(sys.argv[1:])
