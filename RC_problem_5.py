import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex

# RC filter response
def H(f):
    s = 1j*2*np.pi*f
    den = np.polyval([1,1],s*R*C)
    H = 1/den
    return H

# Filter Charecteristics
R = 5*1e2
C = 10e-6

# Pltting the filter amplitude
f_0 = 50.0
f = np.linspace(-3*f_0, 3*f_0, 1e2)
plt.plot(f, abs(H(f)))
plt.grid()
plt.xlabel('$f$ (Hz)')
plt.ylabel('$H(f)$')

##
plt.savefig('./figs/lpf.png')
subprocess.run(shlex.split('terminator --open ./figs/lpf.pdf'))

## Input and output plotting
t = np.linspace(-50e-3, 50e-3, 5e2)
# k = np.linspace(0,100,2)
xt = np.cos(np.pi*100.0*t) + np.cos(2*np.pi*0*t)
yt1 = abs(H(f_0)) * np.cos(np.pi*100.0*t + np.angle(H(f_0))) + abs(H(0)) * np.cos(2*np.pi*0*t + np.angle(H(0)))
xt = np.cos(np.pi*100.0*t) + np.cos(2*np.pi*25*t)
yt2 = abs(H(f_0)) * np.cos(np.pi*100.0*t + np.angle(H(f_0))) + abs(H(50)) * np.cos(2*np.pi*25*t + np.angle(H(50)))
xt = np.cos(np.pi*100.0*t) + np.cos(2*np.pi*50*t)
yt3 = abs(H(f_0)) * np.cos(np.pi*100.0*t + np.angle(H(f_0))) + abs(H(100)) * np.cos(2*np.pi*50*t + np.angle(H(100)))
xt = np.cos(np.pi*100.0*t) + np.cos(2*np.pi*75*t)
yt4 = abs(H(f_0)) * np.cos(np.pi*100.0*t + np.angle(H(f_0))) + abs(H(300)) * np.cos(2*np.pi*75*t + np.angle(H(300)))


plt.subplot(4,1,1)
plt.plot(t, yt1)
plt.grid()
plt.subplot(4,1,2)
plt.plot(t, yt2)
plt.grid()
plt.subplot(4,1,3)
plt.plot(t, yt3)
plt.grid()
plt.subplot(4,1,4)
plt.plot(t, yt4)
plt.grid()
plt.show()
