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

def Sinusoid(ts, amp, freq, offset):
    phases = 2*math.pi*freq*ts + offset
    ys = amp*np.sin(phases)
    return ys

def DIFFERENTIATION(ys, ts):
    #implementing a FORWARD DIFFERENCE QUOTIENT ALGORITHM...
    dy = np.linspace(ys[0], ys[-1], num=len(ys), endpoint=True)
    dy = ys - ys
    dt = ts[2] - ts[1]
    for it in range(len(ys)-1):
        dy[it] = (ys[it+1] - ys[it])/dt
    return dy
def IMPULSE(ts, offset=0):
    ys = UNIT_STEP(np.ones(len(ts)), ts, 0,1,1)
    dy = DIFFERENTIATION(ys, ts)
    return dy
def Integration(ys):
    return np.trapz(ys)

#CONSTRUCTING TIME-AXIS...
time = np.linspace(-2*math.pi, 2*math.pi, num=11520, endpoint=True)/50.0
#HERE IS SINE WAVE...
wave = Sinusoid(time, 1, 50.0, 0)
#CONSTRUCTING STEP WAVE...
step_wave = UNIT_STEP(np.ones(len(time)), time, 0,1,1)
#CONSTRUCTING RAMP WAVE...
ramp_wave = RAMP(np.ones(len(time)), time, 0, 1, 1)
#DIFFERENTIATING THE STEP AND RAMP WAVES...
dy_ramp = DIFFERENTIATION(ramp_wave, time)
dy_step = DIFFERENTIATION(step_wave, time)
#plt.plot(time, dy_wave)
plt.plot(time, dy_ramp)

plt.show()
#IMPLEMENTING THE TRAPEZOIDAL INTEGRATION SCHEME ON THE SINUSOID CREATED EARLIER...
int_wave = Integration(wave)
print(int_wave)

