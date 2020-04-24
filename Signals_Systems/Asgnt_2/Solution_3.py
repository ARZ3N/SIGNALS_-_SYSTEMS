import numpy as np
import matplotlib.pyplot as plt

def Rectangular(amp=1, duration=0, freq=0, offset=0, ts=None, ys=None):
    if freq is 0:
        lrange = -4*duration
        rrange = 4*duration
    else:
        lrange = -4*(1/freq)
        rrange = 4*(1/freq)
    if ts is None:
        ts = np.linspace(lrange, rrange, num=11520, endpoint=True)
    if ys is None:
        ys = np.ones(len(ts))
    if freq is 0:
        for t in range(len(ts)):
            if ts[t]>= -1*(duration/2) + offset and ts[t]<= (duration/2) + offset:
                ys[t] = ys[t]*amp
            else:
                ys[t] = 0 
    else:
        for it in range(-4,5):
            periodx = it*(1/freq)
            for t in range(len(ts)):
                if ts[t]>= -1*(duration/2) + offset + periodx and ts[t]<= (duration/2) + offset + periodx:
                    ys[t] = ys[t] *amp
    return ys,ts

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
def spectrum(ys, ts):
    freq_mag = (ys.real**2 + ys.imag**2)**0.5
    return freq_mag

#CREATING A TIMESCALE FOR THE WAVE
time = np.linspace(0,21.0, num=101, endpoint=True)
print(time)
#INITIALIZING THE WAVE ARRAYS
yn  = np.ones(len(time))
yn_11 = np.ones(len(time))
Yn = np.zeros(len(time))
#NOW, FOR x[N] AND y[N], UNIT_STEP METHOD IS USED...
yn = UNIT_STEP(yn, time, 0, mag=1)
yn_11 = UNIT_STEP(yn_11, time, 11, mag=1)
#HENCE THE y[n] AS GIVEN IN THE QUESTION IS REPRESENTED IN THE ARRAY- Yn...
Yn = yn - yn_11 #LOOKING CLOSELY, x[n] AND y[n] IN QUESTION ARE THE SAME...
#CREATING AN ARRAY TO HOLD THE DFT OF Yn...
fft_Yn = np.fft.fft(Yn)
#CREATING AN ARRAY THAT HOLD THE MAGNITUDE OF THE COMPLEX ENTITIES OF THE DFT...
spect_Yn = spectrum(fft_Yn, time)
#PLOTTING THE SPECTRUM OF Yn...
plt.plot(time, spect_Yn)
plt.show()