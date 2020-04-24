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
            ys[it] = ys[it] + mag
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
            ys[it] = ys[it]+ramp
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

#CREATING TIME-AXIS...
time = np.linspace(-2*math.pi, 2*math.pi, num = 256, endpoint=True)
#CONSTRUCTING STEP WAVE...
step_wave = np.zeros(len(time))
step_wave = UNIT_STEP(step_wave, time, offset=2.0, mag=1, direction=1)
#CONSTRUCTING RAMP...
ramp_wave = np.zeros(len(time))
ramp_wave = RAMP(ramp_wave, time, offset=1.0, mag=1, direction=1)
#PLOTTING THE WAVES...
#TO PLOT THE STEP WAVE, REPLACE THE SECOND ARG IN THE BELOW 'PLOT' FUNCTION WITH 'step_wave', OTHERWISE 'ramp_wave'
plt.plot(t, rect_wave)
plt.show()