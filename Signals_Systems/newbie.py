import numpy as np
import math
import matplotlib.pyplot as plt

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
#def IMPULSE(ys, ts, offset, direction)
def Sinusoid(ts, amp, freq, offset):
    phases = 2*math.pi*freq*ts + offset
    ys = amp*np.sin(phases)
    return ys

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

def scale(ys, mag):
    for it in ys:
        it = it*mag

def reverse(ys, ts):
    temp = 0.0
    for it in range(0,len(ys)):
        temp = ys[it]
        ys[it] = ys[len(ys)-1-it]
        ys[len(ys)-1-it] = temp
    return ys,ts

def convolution(ht, gt):
    # here 'ht' is the parent wave, and 'gt' is the scanner wave.
    mah = np.linspace(0.0, 4*math.pi, num=11520, endpoint=True)
    mah = ht - ht
    for it in range(0,len(ht)):
        jt=0
        while jt<=it:
            mah[it] += (gt[jt] * ht[it-jt])
            jt = jt + 1
    return mah

    

def differentiation(ys, ts):
    #implementing a FORWARD DIFFERENCE QUOTIENT ALGORITHM...
    dy = np.linspace(ys[0], ys[-1], num=len(ys), endpoint=True)
    dy = ys - ys
    dt = ts[2] - ts[1]
    for it in range(len(ys)-1):
        dy[it] = (ys[it+1] - ys[it])/dt
    return dy



"""   
wave,time = Rectangular(2, 0.008, 50, 0)
plt.plot(time,wave)    
plt.show()
"""

lrange = 0.0
rrange = 4*math.pi
freq = 20.0
magnitude = 5.0
times = np.linspace(lrange, rrange, num = 11520, endpoint=True)/freq
waves = Sinusoid(times, magnitude, freq, math.pi/2)  
wah = np.trapz(waves)
print("integration:") 
print(wah)

"""
waves = RAMP(waves, times, 10)
plt.plot(times, waves)
plt.show()
"""

"""
time = np.linspace(0.0, 4*math.pi, num=11520, endpoint=True)/50
sine50 = Sinusoid(time, 1, 50, 0)
rect2, dummy = Rectangular(1, 2/50, 0, 1/50, time, ys=None)
conv = convolution(sine50, rect2)
plt.plot(time, conv)
plt.show()
"""