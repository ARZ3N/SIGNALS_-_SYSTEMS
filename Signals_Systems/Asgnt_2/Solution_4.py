import numpy as np
import matplotlib.pyplot as plt
import math

def Sinusoid(ts, amp, freq, offset):
    phases = 2*math.pi*freq*ts + offset
    ys = amp*np.sin(phases)
    return ys

def spectrum(ys, ts):
    freq_mag = (ys.real**2 + ys.imag**2)**0.5
    return freq_mag
#CONSTRUCTING A TIME-AXIS FOR OUR WAVE...
lrange = -2*math.pi
rrange = 2*math.pi
frequency = 50.0
time = np.linspace(lrange, rrange, num = 1152, endpoint=True)/frequency
#CONSTRUCTING A SINE WAVE ON OUR TIME-AXIS...
wave = Sinusoid(time, amp=5.0, freq=50.0, offset=0)
#BUILDING THE FFT ARRAY OUR SINE_WAVE...
"""
The numpy.fft class of the Numpy module uses the Cooley-Tuckey FFt algorithm which is also known as the 
2-RADIX FFT algorithm which was developed to make this mathematical function faster-to process.
The runtime complexity of this algorithm is O(Nlog(N)).
""" 
fft_wave = np.fft.fft(wave) #THE DFT OF wave...
#THE MAGNITUDE OF THE COMPLEX FFT_WAVE...
spect_wave = spectrum(fft_wave, time)
#PLOTTING THE SPECTRUM... 
plt.plot(time, spect_wave)
plt.show()