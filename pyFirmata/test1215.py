#conding: utf-8

import serial
import time

ser = serial.Serial('/dev/ttyACM0',9600)
ser1 = serial.Serial('/dev/ttyACM1',9600)
while(1):
	time.sleep(2)
	ser1.write('a')
	ser.write('a')
	time.sleep(2)
	ser1.write('0')
	ser.write('0')
ser.close()

