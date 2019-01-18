import numpy as np
import librosa as lb
from scipy import signal
import matplotlib.pyplot as plt

wav, sr = lb.load("Sound_Noise.wav")
file = "val_out_sound.txt"
wav_ard = np.loadtxt(file)


cutoff = 50
sampl_fs = 1e4
order = 4

wn = 2*cutoff/sampl_fs

b, a = signal.butter(order, wn, 'low')
output = signal.filtfilt(b, a, wav)
differ = wav_ard - output
diff = np.linalg.norm(differ)
print(diff)
t = np.linspace(0,1,len(output))
# plt.plot(wav)
plt.plot(wav_ard)
plt.plot(output)
plt.plot(differ)
plt.show()
