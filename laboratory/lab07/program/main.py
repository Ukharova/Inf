import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from math import sin

N = 1500
n = 15

a1 = 1
a2 = 0.3
t = np.arange(0,0.5,0.01)

dn_max = [-1,-1]

def f(n,t):
    dn = (a1 + a2*n)*(N-n)
    global dn_max
    if dn > dn_max[0]:
        dn_max = [dn,t]
    return dn

res = odeint(f,n,t)

print(dn_max[1])

plt.plot(t, res[:,0])
plt.show()