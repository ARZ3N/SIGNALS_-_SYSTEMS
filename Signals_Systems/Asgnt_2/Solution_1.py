import numpy as np
import matplotlib.pyplot as plt
import math

def Sinusoid(ts, amp, freq, offset):
    phases = 2*math.pi*freq*ts + offset
    ys = amp*np.sin(phases)
    return ys

def UNIT_STEP(ys, ts, offset=0, mag=1, direction=1):
    if offset>ts[-1] or offset<ts[0]:
        for it in range(len(ts)):
            ts[it] = ts[it] + offset
    for it in range(len(ts)):
        if ts[it]< offset:
            ys[it] = 0
        else:
            ys[it] = ys[it] * mag
    return ys

def RAMP(ys, ts, offset, mag=1, direction=1):
    if offset>ts[-1] or offset<ts[0]:
        for it in range(len(ts)):
            ts[it] = ts[it] + offset
    for it in range(len(ts)):
        if ts[it] <= offset:
            ys[it] = 0
        else:
            ramp = mag*ts[it] - offset
            ys[it] = ys[it]*ramp
    return ys

def Cn(ys, ts):
    N = len(ys)
    real_cn = np.zeros(len(ys))
    imag_cn = np.zeros(len(ys))
    for k in range(0, len(ys)):
        for n in range(0, len(ys)):
            real_cn[k] += ys[k] * math.cos((2*math.pi*k* ts[n]) / N)
            imag_cn[k] += -1* ys[k] * math.sin((2*math.pi*k* ts[n]) / N)
    return real_cn/N, imag_cn/N

def magnitude(real_ys, imag_ys):
    mag_ys = np.zeros(len(real_ys))
    mag_ys = (real_ys**2 + imag_ys**2)**0.5
    return mag_ys

#CREATING A TIME-AXIS ARRAY...
frequency = 50.0
time = np.linspace(-2*math.pi, 2*math.pi, num = 1152, endpoint=True)/frequency
#CREATING A SINUSOIDAL WAVE ARRAY...
wave = Sinusoid(time, amp=2, freq=50.0, offset=0)
#APPLYING A RAMP SIGNAL AT A PARTICULAR INSTANCE (the 'offset' value in the below fn)...
wave = RAMP(wave, time, offset=-1*math.pi, mag=1, direction=1)
#CALCULATING THE FOURIER SERIES COEFFICIENTS (Cn)...
"""
Once we have the C(i) coefficients, one can reconstruct the wave by multiplication with
the corresponding : exp(-1*j * (2*pi*k)/N) term, and then add the terms to get the original wave back.
"""
fs_wave_r, fs_wave_i = Cn(wave, time) #THE REAL AND IMAG PART OF ALL THE COEFFICIENTS 
fs_wave_coeff = magnitude(fs_wave_r, fs_wave_i) #THE MAGNITUDE OF THE COMPLEX COEFFICIENTS
#HENCE PRINTING THE COEFFICIENTS...
print("Fourier series coefficients...\n")
print(fs_wave_coeff)

#plt.plot(time, fs_wave_coeff)
#plt.show()
"""
fs_wave_r, fs_wave_i = Cn(wave, time)
fs_wave_coeff = magnitude(fs_wave_r, fs_wave_i)
"""
"""
plt.plot(time, fs_wave_coeff)
plt.show()
"""