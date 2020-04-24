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

def convolution(ht, gt):
    # here 'ht' is the parent wave, and 'gt' is the scanner wave.
    conv = np.linspace(0.0, 4*math.pi, num=11520, endpoint=True)
    conv = ht - ht
    for it in range(0,len(ht)):
        jt=0
        while jt<=it:
            conv[it] += (gt[jt] * ht[it-jt])
            jt = jt + 1
    return conv

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


time = np.linspace(0.0, 4*math.pi, num=11520, endpoint=True)/50
sine50 = Sinusoid(time, 1, 50, 0)
rect2, dummy = Rectangular(1, 2/50, 0, 1/50, time, ys=None)
conv = convolution(sine50, rect2)
plt.plot(time, conv)
plt.show()
