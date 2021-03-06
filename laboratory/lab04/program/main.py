import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

w = 7.5
g = 0

x0 = 0
y0 = -1

t0 = 0.0
tmax = 40
dt = 0.05

t = np.arange(t0, tmax + dt, dt)
v0 = [x0,y0]

def y(v, t):
    x, y = v
    return [y, -1 * np.power(w,2) * x - g *y]

ans_1 = odeint(y, v0, t)

fig1, ax1 = plt.subplots()
ax1.plot(ans_1[:, 0], ans_1[:, 1])
fig4, ax4 = plt.subplots()
ax4.plot(t, ans_1[:, 0])
ax4.plot(t, ans_1[:, 1])

w = 5
g = 7

ans_2 = odeint(y, v0, t)

fig2, ax2 = plt.subplots()
ax2.plot(ans_2[:, 0], ans_2[:, 1])
fig5, ax5 = plt.subplots ()
ax5.plot(t, ans_2[:, 0])
ax5.plot(t, ans_2[:, 1])

w = 4
g = 2

def f(t):
    x, y = v
    return [y, -1*np.power(w, 2)*x - g*y - f(t)]

ans_3 = odeint(y, v0, t)

fig3, ax3 = plt.subplots()
ax3.plot(ans_3[:, 0], ans_3[:, 1])
fig6, ax6 = plt.subplots ()
ax6.plot(t, ans_3[:, 0])
ax6.plot(t, ans_3[:, 1])
plt.show()