import numpy as np
import matplotlib.pyplot as plt
import math

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

def Sinusoid(ts, amp, freq, offset):
    phases = 2*math.pi*freq*ts + offset
    ys = amp*np.sin(phases)
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


def spectrum(ys, ts):
    freq_mag = (ys.real**2 + ys.imag**2)**0.5
    return freq_mag, sample

def IMPULSE(ts, t, mag, ys=None):
    if ys is None:
        ys = np.ones(len(ts))
    for it in range(0,len(ts)):
        if ts[it] is t:
            ys[it] += mag
        else:
            ys[it] = 0.0
    return ys

lrange = -2*math.pi
rrange = 2*math.pi
frequency = 50.0
time = np.linspace(lrange, rrange, num = 1152, endpoint=True)/frequency

wave = Sinusoid(time, 2.0, 50.0, 0)
fft_wave = np.fft.fft(wave)
fs_wave_r, fs_wave_i = Cn(wave, time)
fs_wave_coeff = magnitude(fs_wave_r ,fs_wave_i)
plt.plot(fs_wave_coeff, fft_wave)
plt.show()
