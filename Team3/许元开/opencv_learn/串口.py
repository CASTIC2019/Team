import serial
import serial.tools.list_ports
ser=serial.Serial(port='COM6')
ser.write('A'.encode())






