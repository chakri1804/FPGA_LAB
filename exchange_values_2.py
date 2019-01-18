import numpy as np
import serial
import time

x = np.genfromtxt('input_100_1e5.csv', delimiter = ',')
print x
y = []
ser = serial.Serial('/dev/ttyACM0',9600)

time.sleep(5)

fpo = open('val_out.txt', 'w')

for i in x[0:9998]:
	ser.write(str(i))
	ser.write(" ")
	print i
	line =ser.readline()
	fpo.write(line)
	# fpo.write('\n')
	# y_f = read_output()
	# print y_f
	# y.append(float(y_f))
	#time.sleep(1)

# np.savetxt("output_100_1e5.csv", y, newline= ",", fmt = '%f')
