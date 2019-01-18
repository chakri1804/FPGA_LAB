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
xt = np.cos(2*np.pi*f_0*t)
yt = abs(H(f_0)) * np.cos(2*np.pi*f_0*t + np.angle(H(f_0)))

plt.subplot(2,1,1)
plt.plot(t, xt)
plt.grid()
plt.subplot(2,1,2)
plt.plot(t, yt)
plt.grid()
plt.show()
