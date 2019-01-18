import numpy as np
import librosa as lb
import serial
import time

# x = np.genfromtxt('input_100_1e5.csv', delimiter = ',')
x, sr = lb.load("Sound_Noise.wav")
print x
y = []
ser = serial.Serial('/dev/ttyUSB0',115200)

time.sleep(5)

fpo = open('val_out_sound.txt', 'w')
count = 0
for i in x:
	ser.write(str(i))
	ser.write(" ")
	print count
	count += 1
	line =ser.readline()
	# print(line)
	# y.append(float(line))
	fpo.write(line)
	# fpo.write('\n')
	# y_f = read_output()
	# print y_f
	# y.append(float(y_f))
	#time.sleep(1)

# np.savetxt("output_100_1e5.csv", y, newline= ",", fmt = '%f')
