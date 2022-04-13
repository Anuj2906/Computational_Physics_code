from cProfile import label
import matplotlib .pyplot as plt
import math
last = float(input('Enter the last value:'))
step = float(input('Enter the step size:'))

# Eulers method
a = []
b = []
c = []
t = 0
a.append(t)
x = 1
b.append(x)
w = 0
c.append(w)

while t <last:
    o1 = w
    o2 = -1*x
    x = x + o1*step
    w = w + o2*step
    b.append(x)
    c.append(w)
    t= t+step
    a.append(t)
plt.plot(a,b,  label= 'Euler method')
plt.ylabel('Y')
plt.xlabel('X')
plt.legend(loc = 'upper left')
# plt.show()
print(a,"\n")
print(b,"\n")
print(c,"\n")

#4th order runge kutta method

a = []
b = []
c = []
t = 0
a.append(t)
x = 1
b.append(x)
w = 0
c.append(w)

while t <last:
    k11 = w
    k12 = -1*x
    x1= x + k11*(step/2)
    w1 = w + k12*(step/2)
    k21 = w1
    k22 = -1*x1
    x1= x + k21*(step/2)
    w1 = w + k22*(step/2)
    k31 = w1
    k32 = -1*x1
    x1= x + k31*(step)
    w1 = w + k32*(step)
    k41 = w1
    k42 = -x1
    o1 = (k11+(2*k21)+(2*k31)+k41)/6
    o2 = (k12+(2*k22)+(2*k32)+k42)/6
    x = x + o1*step
    w = w + o2*step
    b.append(x)
    c.append(w)
    t= t+step
    a.append(t)
plt.plot(a,b,  label= 'Runge kutta')
plt.ylabel('Y')
plt.xlabel('X')
plt.legend(loc = 'upper left')
# plt.show()
print(a,"\n")
print(b,"\n")
print(c,"\n")

#real solution

a = []
b = []
c = []
t = 0
a.append(t)
x = 1
b.append(x)
while t<last:
    x= math.cos(t)
    b.append(x)
    t= t+step
    a.append(t)
plt.plot(a,b, label= 'Real solution')
plt.ylabel('Y')
plt.xlabel('X')
plt.legend(loc = 'upper left')
plt.show()