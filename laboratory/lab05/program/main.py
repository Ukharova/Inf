import numpy as np
import math
from scipy.integrate import odeint
import matplotlib.pyplot as plt

a = 0.22
b = 0.066
c = 0.66
d = 0.022
x0=np.array([7,15])
t=np.arange(0,400,0.1)

def syst(x,t):
    dx_1=-a*x[0]+b*x[0]*x[1]
    dx_2=c*x[1]-d*x[0]*x[1]
    return [dx_1,dx_2]

y=odeint(syst, x0,t)

plt.plot([i[0] for i in y], [i[1] for i in y], lw=2)
plt.title('График зависимости численности хищников от численности жертв')
plt.grid('True')

plt.show()

plt.plot(t, [i[0] for i in y], lw=2)
plt.title ('График изменения численности хищников')

plt.show()

plt.plot(t, [i[1] for i in y], lw=2)
plt.title ('График изменения численности жертв')
plt.grid('True')

plt.show()
xc=c/d
yc=a/b
print(xc,yc)