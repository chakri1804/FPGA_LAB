import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# t = np.linspace(0.0,2.0,20000)
# input_signal = np.sin(np.pi*100*t) + np.sin(np.pi*300*t)

cutoff = 50
sampl_fs = 1e4
order = 4

wn = 2*cutoff/sampl_fs

b, a = signal.butter(order, wn, 'low')

print(a,b)
# output = signal.filtfilt(b, a, input_signal)
#
# plt.subplot(2,1,1)
# plt.plot(t, input_signal)
# plt.grid()
# plt.subplot(2,1,2)
# plt.plot(t, output)
# plt.grid()
# plt.show()
