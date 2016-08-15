__author__ = 'potty'

import serial
from baud_rates import BaudRates
import time



def get_as_hex_string(data):
    if type(data) == str:
        return ' '.join('0x%02x' % ord(b) for b in data)
    elif type(data) == list:
        return ' '.join('0x%02x' % b for b in data)

ser = serial.Serial('/dev/ttyUSB0', baudrate=BaudRates.B_115200, xonxoff=False, rtscts=False, dsrdtr=False)
ser.flushInput()
ser.flushOutput()

while True:
    bytesToRead = ser.inWaiting()
    bytes = ser.read(bytesToRead)
    if bytesToRead>0:
        print bytes