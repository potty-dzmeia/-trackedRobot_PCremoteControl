__author__ = 'potty'


import serial
from baud_rates import BaudRates

ser = serial.Serial('/dev/ttyUSB0', baudrate=BaudRates.B_115200, xonxoff=False, rtscts=False, dsrdtr=False)
ser.flushInput()
ser.flushOutput()

while True:
    bytesToRead = ser.inWaiting()
    bytes = ser.read(bytesToRead)
    if bytesToRead>0:
        print(bytes)
