from cProfile import label
import matplotlib .pyplot as plt
last = float(input('Enter the last value:'))
step = float(input('Enter the step size:'))
# Eulers method
a = []
b = []
y = 1
a.append(y)
x= 0
b.append(x)
while x <last:
   o = (-2*x*x*x)+(12*x*x)-(20*x)+8.5
   y = y + o*step
   a.append(y)
   x= x+step
   b.append(x)
plt.plot(b,a, '-o', label= 'Euler method')
plt.ylabel('Y')
plt.xlabel('X')
plt.legend(loc = 'upper left')
# print(y)
# print("\n\n")
# print(a)
# Heuns method
a1 = []
b1 = []
y = 1
a1.append(y)
x= 0
b1.append(x)
while x <last:
    o = (-2*x*x*x)+(12*x*x)-(20*x)+8.5
    x1 = x+step
    o1 = (-2*x1*x1*x1)+(12*x1*x1)-(20*x1)+8.5
    of = (o + o1)/2
    y = y + of*step
    a1.append(y)
    x= x+step
    b1.append(x)
plt.plot(b1,a1, '-o', label = 'heuns method')
plt.ylabel('Y')
plt.xlabel('X') 
plt.legend(loc = 'upper left')
# print(a1)
#midpoint method:
a2 = []
b2 = []
y = 1
a2.append(y)
x= 0
b2.append(x)
while x <last:
    x1 = x+(step/2)
    o1 = (-2*x1*x1*x1)+(12*x1*x1)-(20*x1)+8.5
    y = y + o1*step
    a2.append(y)
    x= x+step
    b2.append(x)
plt.plot(b2,a2, '-o', label = 'mid point method')
plt.ylabel('Y')
plt.xlabel('X') 
plt.legend(loc = 'upper left') 
print(a2)
# Actual solutons
a3 = []
b3 = []
x= 0
y=1
a3.append(y)
b3.append(x)
while x <last:
    x= x+step
    y= (-0.5*x*x*x*x)+(4*x*x*x)- (10*x*x)+ (8.5*x)+1
    a3.append(y)
    b3.append(x)
plt.plot(b3,a3, '-o', label = 'Actual solution')
plt.ylabel('Y')
plt.xlabel('X') 
plt.legend(loc = 'upper left') 
print(a3)
#plt.show() 
print("x value   Euler_value   Heuns_value   Midpiont_value   Actual_value ")
for i in range(len(b)):
    print('%0.2f       %0.6f      %0.6f       %0.6f        %0.6f' % (b[i],a[i],a1[i],a2[i],a3[i]), end='\n')

 