import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import soundfile as sf

f0 = 100
f1 = 500
fs  = 5000

x = np.linspace(-1,1, 1e4)

y = np.cos(2*np.pi*f0*x) + np.cos(2*np.pi*f1*x)
np.savetxt("input_100_1e5.csv", y, newline= ",", fmt = '%f')
sf.write('input_100_1e5.wav', y, fs)
