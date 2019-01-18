import serial
import numpy as np
import time
port = '/dev/ttyACM0'

t = np.linspace(0,1,200)
x = np.cos(2*np.pi*10*t) + np.cos(2*np.pi*20*t)
aard = serial.Serial(port,2000000)
for i in range(0,len(x)):
	aard.write()
	time.sleep(0.5)
