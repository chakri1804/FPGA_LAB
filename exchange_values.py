import serial
import time
import numpy as np
import matplotlib.pyplot as plt

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0)

fpo = open('val_out.txt', 'w')
fpi = open('val_in.txt', 'w')

t = np.linspace(0,1,1e4)
x = np.cos(2*np.pi*50*t) + np.cos(2*np.pi*150*t)
iter=0

meh = []
while(1):
    var = x[iter%10000]
    iter+=1
    ser.write(str(int(var*10000)))
    # time.sleep(1)
    # line =ser.readline()
    # time.sleep(0.1)
    # print(line)
    # # meh.append(float(line))
    print "sent: "+str(int(var*10000))
    # fpo.write(line)
    # fpo.write('\n')
    # fpi.write(str(int(var*10000)))
    # fpi.write('\n')
# plt.plot(t, meh)
