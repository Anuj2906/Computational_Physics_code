import matplotlib .pyplot as plt
import math

stepSize = 0.4
x = [0,0.4,0.8,1.2,1.6,2]
y_d = 0
z_d = 0

#Euler method
ye = [0]
ze = [0]
ky1 = 0
ky2 = 0
kz1 = 0
kz2 = 0
for i in range(5):
    
    ky1 = ye[i]*ze[i] + math.cos(x[i]) - 0.5*math.sin(2*x[i])
    kz1 = ye[i]*ye[i] + ze[i]*ze[i] - (1 + math.sin(x[i]))

    ky2 = (ye[i]+0.2*ky1)*(ze[i]+0.2*kz1) + math.cos(x[i]+0.2) - 0.5*math.sin(2*x[i]+0.2)
    kz2 = (ye[i]+0.2*ky1)*(ye[i]+0.2*ky1) + (ze[i]+0.2*kz1)*(ze[i]+0.2*kz1) - (1 + math.sin(x[i]+0.2))
    t = ye[i] + ky2*0.4
    ye.append(t)
    u = ze[i] + kz2*0.4
    ze.append(u)
print(x)
print(ye)
print(ze)

#Midpoint method
ym = [0]
zm = [0]
for i in range(5):
    y_d = ym[i]*zm[i] + math.cos(x[i]+0.2) - 0.5*math.sin(2*(x[i]+0.2))
    z_d = ym[i]*ym[i] + zm[i]*zm[i] - (1 + math.sin(x[i]+0.2))
    t = ym[i] + y_d*0.4
    ym.append(t)
    u = zm[i] + z_d*0.4
    zm.append(u)
print(x)
print(ym)
print(zm)

#RK4 Method
yr = [0]
zr = [0]
k1y = 0
k2y = 0
k3y = 0
k4y = 0

k1z = 0
k2z = 0
k3z = 0
k4z = 0
for i in range(5):
    k1y = yr[i]*zr[i] + math.cos(x[i]) - 0.5*math.sin(2*(x[i]))
    k1z = yr[i]*yr[i] + zr[i]*zr[i] - (1 + math.sin(x[i]))

    k2y = (yr[i]+0.2*k1y)*(zr[i]+0.2*k1z) + math.cos(x[i]+0.2) - 0.5*math.sin(2*(x[i]+0.2))
    k2z = (yr[i]+0.2*k1y)*(yr[i]+0.2*k1y) + (zr[i]+0.2*k1z)*(zr[i]+0.2*k1z) - (1 + math.sin(x[i]+0.2))

    k3y = (yr[i]+0.2*k2y)*(zr[i]+0.2*k2z) + math.cos(x[i]+0.2) - 0.5*math.sin(2*(x[i]+0.2))
    k3z = (yr[i]+0.2*k2y)*(yr[i]+0.2*k2y) + (zr[i]+0.2*k2z)*(zr[i]+0.2*k2z) - (1 + math.sin(x[i]+0.2))

    k4y = (yr[i]+0.4*k3y)*(zr[i]+0.4*k3z) + math.cos(x[i]+0.4) - 0.5*math.sin(2*(x[i]+0.4))
    k3z = (yr[i]+0.4*k3y)*(yr[i]+0.4*k3y) + (zr[i]+0.4*k3z)*(zr[i]+0.4*k3z) - (1 + math.sin(x[i]+0.4))

    t = yr[i] + (k1y + 2*k2y + 2*k3y + k4y)*0.4/6
    yr.append(t)
    u = zr[i] + (k1z + 2*k2z + 2*k3z + k4z)*0.4/6
    zr.append(u)
print(x)
print(yr)
print(zr)

plt.plot(x,ye,'-o',label = 'Euler method')
plt.ylabel('ye')
plt.xlabel('x')
plt.legend(loc = 'upper left')

plt.plot(x,ym,'-o',label = 'Midpoint method')
plt.ylabel('ym')
plt.xlabel('x')
plt.legend(loc = 'upper left')

plt.plot(x,yr,'-o',label = 'RK4 method')
plt.ylabel('yr')
plt.xlabel('x')
plt.legend(loc = 'upper left')
plt.show()


plt.plot(x,ze,'-o',label = 'Euler method')
plt.ylabel('ze')
plt.xlabel('x')
plt.legend(loc = 'upper left')

plt.plot(x,zm,'-o',label = 'Midpoint method')
plt.ylabel('zm')
plt.xlabel('x')
plt.legend(loc = 'upper left')

plt.plot(x,zr,'-o',label = 'RK4 method')
plt.ylabel('zr')
plt.xlabel('x')
plt.legend(loc = 'upper left')
plt.show()