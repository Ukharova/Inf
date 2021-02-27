import math

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

x0 = 250000
y0 = 380000

t0 = 0

a = 0.4
b = 0.607
c = 0.667
h = 0.42

tmax = 1
dt = 0.05

t = np.arange(t0,tmax+dt,dt)
v0 = [x0,y0]

def P_1(t):
p = math.sin(2*t)
return p
def Q_1(t):
q = 2*math.cos(6*t)
return q


def f_1(v,t):
    x,y = v
    return [-a*x-b*y+P_1(t),-c*x-h*y+Q_1(t)]

v0 = [x0,y0]

ans_1 = odeint(f_1,v0,t)



fig1, ax1 = plt.subplots()

ax1.plot(t, ans_1[:,0], label='x армия')
ax1.plot(t, ans_1[:,1], label='y армия')
ax1.set_xlabel('Время')
ax1.set_ylabel('Численность армии')
ax1.set_title("Модель боевых действий №1")
ax1.legend()


a = 0.39
b = 0.84
c = 0.42
h = 0.49


def P_2(t):
    return math.sin(2*t)+1
def Q_2(t):
    return 2*math.cos(t)


def f_2(v,t):
    x,y = v
    return [-a*x-b*y+P_2(t),-c*x*y-h*y+Q_2(t)]

ans_2 = odeint(f_2,v0,t)

fig2, ax2 = plt.subplots()

ax2.plot(t, ans_2[:,0], label='x армия')
ax2.plot(t, ans_2[:,1], label='y армия')
ax2.set_xlabel('Время')
ax2.set_ylabel('Численность армии')
ax2.set_title("Модель боевых действий №2")
ax2.legend()
plt.show()