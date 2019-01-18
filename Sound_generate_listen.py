import librosa as lb
import numpy as np

t = np.linspace(-10, 10, 100000)
xt = np.cos(np.pi*100.0*t) + np.cos(np.pi*300.0*t)

lb.output.write_wav('100_300.wav', xt, 5000)
