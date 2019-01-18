import numpy as np
import matplotlib.pyplot as plt


foo = open('val_out.txt', 'r')
foi = open('val_in.txt', 'r')

input = foi.readlines()
output = foo.readlines()
t = np.arange(0,0.2,200)
# print(output)
inin = []
for i in range(len(input)):
    temp = input[i].split('\n')
    inin.append(float(temp[0]))

outout = []
for i in range(len(output)):
    temp = output[i].split('\r')
    if temp[0] != '\n':
        outout.append(float(temp[0]))
        # print(temp[0])

# print(len(inin))
# print(len(outout))
ti = np.linspace(0,0.2, len(inin))
to = np.linspace(0,0.2, len(outout))
inin = np.array(inin)
outout = np.array(outout)
print(inin.shape, ti.shape)
plt.plot(ti, inin/10000.0)
plt.plot(to, outout/10000.0)
plt.show()
