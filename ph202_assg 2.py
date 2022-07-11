from cProfile import label
#imported libraries matplotlib, numpy, math
import matplotlib.pyplot as plt
import numpy as np
import math

py = math.pi
ind1 = 1.33
ind2 = 2.77
x = 0

a = []
a1 = []

k1 = []
k2 = []
k3 = []
k4 = []
k5 = []


#for s polarisation
for thtai in np.arange(0.0,py/2, py/50):
    thtar = math.asin((ind1/ind2)*math.sin(thtai))
    ref_coff = abs(ind1*math.cos(thtai) - ind2*math.cos(thtar))/(ind1*math.cos(thtai)+ ind2*math.cos(thtar))
    tran_coff = (2*ind1*math.cos(thtai))/(ind1*math.cos(thtai)+ ind2*math.cos(thtar))
    rc11 = (ind1*math.cos(thtar) - ind2*math.cos(thtai))/(ind1*math.cos(thtar)+ ind2*math.cos(thtai))
    tc11 = (2*ind1*math.cos(thtai))/(ind1*math.cos(thtar)+ ind2*math.cos(thtai))
    k1.append(ref_coff)
    k2.append(tran_coff)
    k3.append(rc11)
    k4.append(tc11)
    k5.append(thtar)
    a.append((thtai*180)/py)
    
plt.plot(a, k1, label = 'Reflection' )


plt.xlabel('thtai')
plt.ylabel('ref_coff')
plt.title('S-Polarization')
plt.plot(a, k2, label= 'Transmittance')
plt.xlabel('thtai')
plt.ylabel('tran_coff')
plt.legend(loc = 'upper left')
plt.show()

plt.plot(a, k3, label = 'rc11')
plt.xlabel('thtai')
plt.ylabel('rc11')

# for p polarisation
plt.plot(a, k4, label = 'tc11')
plt.axhline(y = 0.0, color = 'r', linestyle = '-')

plt.xlabel('thtai')
plt.ylabel('tc11')
plt.title('P- Polarization')
plt.legend(loc = 'upper left')
plt.show()
brew_angle = math.atan(ind2/ind1)
print("Theoritical value of brewester angle:")
print(brew_angle*180/py)
