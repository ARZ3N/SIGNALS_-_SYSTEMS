import numpy as np
import matplotlib.pyplot as plt
import math

def SCALE(ys, mag):
    for it in ys:
        it = it*mag
    return ys

def REVERSE(ys):
    temp = 0.0
    for it in range(0,len(ys)):
        temp = ys[it]
        ys[it] = ys[len(ys)-1-it]
        ys[len(ys)-1-it] = temp
    return ys

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
#CONSTRUCTING TIME-AXIS AND SINE WAVE
time = np.linspace(-2*math.pi, 2*math.pi, num=1152, endpoint=True)/50.0
wave = Sinusoid(time, amp=1, freq = 50.0, offset=0)
wave = RAMP(wave, time, offset=0, mag=1, direction=1)
#PERFORMING THE SCALING AND REVERSING OPERATIONS...
#AND EACH METHOD WRITTEN TO CREAT A WAVE, INHERENTLY HAS AN 'OFFSET' VARIABLE WHICH CAN BE USED FOR SHIFTING OPERATION.
wave = SCALE(wave, mag=2.0)
wave = REVERSE(wave)
plt.plot(time, wave)
plt.show()