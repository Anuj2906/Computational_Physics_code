#For shooting method
import numpy as np
import matplotlib .pyplot as plt

steps=int(input("Enter no of steps : "))
h=(10-0)/steps
T1=np.zeros(steps+1)
T1[0]=40
z1=np.zeros(steps+1)
z1[0]=float(input("Enter first initial guess for T' = "))
for i in range(steps):
 k1=z1[i]
 l1=0.01*(T1[i]-20)
 k2=z1[i]+0.5*l1*h
 l2=0.01*((T1[i]+0.5*k1*h)-20)
 k3=z1[i]+0.5*l2*h
 l3=0.01*((T1[i]+0.5*k2*h)-20)
 k4=z1[i]+l3*h
 l4=0.01*((T1[i]+k2*h)-20)
 z1[i+1]=z1[i]+(1/6)*(l1+2*l2+2*l3+l4)*h
 T1[i+1]=T1[i]+(1/6)*(k1+2*k2+2*k3+k4)*h 
x=np.zeros(steps+1)
i=0
while i<steps:
 x[i+1]=x[i]+h
 i=i+1
plt.grid(linestyle='-',linewidth=0.1,color='m')
plt.plot(x, T1, 'b')
plt.title("First Guess")


T2=np.zeros(steps+1)
T2[0]=40
z2=np.zeros(steps+1)
z2[0]=float(input("Enter second initial guess for T' = "))
for i in range(steps):
 k1=z2[i]
 l1=0.01*(T2[i]-20)
 k2=z2[i]+0.5*l1*h
 l2=0.01*((T2[i]+0.5*k1*h)-20)
 k3=z2[i]+0.5*l2*h
 l3=0.01*((T2[i]+0.5*k2*h)-20)
 k4=z2[i]+l3*h
 l4=0.01*((T2[i]+k2*h)-20)
 z2[i+1]=z2[i]+(1/6)*(l1+2*l2+2*l3+l4)*h
 T2[i+1]=T2[i]+(1/6)*(k1+2*k2+2*k3+k4)*h
x=np.zeros(steps+1)
i=0
while i<steps:
 x[i+1]=x[i]+h
 i=i+1
plt.grid(linestyle='-',linewidth=0.1,color='m')
plt.plot(x, T2, 'r')
plt.title("Second Guess")


z=np.zeros(steps+1)
z[0]=10+((z2[0]-z1[0])/(T2[-1]-T1[-1]))*(200-T1[-1]) 

Ta=np.zeros(steps+1)
Ta[0]=40
i=0
for i in range(steps):
 k1=z[i]
 l1=0.01*(Ta[i]-20)
 k2=z[i]+0.5*l1*h
 l2=0.01*((Ta[i]+0.5*k1*h)-20)
 k3=z[i]+0.5*l2*h
 l3=0.01*((Ta[i]+0.5*k2*h)-20)
 k4=z[i]+l3*h
 l4=0.01*((T2[i]+k2*h)-20)
 z[i+1]=z[i]+(1/6)*(l1+2*l2+2*l3+l4)*h
 Ta[i+1]=Ta[i]+(1/6)*(k1+2*k2+2*k3+k4)*h
x=np.zeros(steps+1)
i=0
while i<steps:
 x[i+1]=x[i]+h
 i=i+1
plt.grid(linestyle='-',linewidth=0.1,color='m')
plt.plot(x, Ta, 'g')
plt.legend(['First guess','Second guess','Linear Interpolation'])
plt.title("Shooting Method")
#plt.show()

#For Finite Difference method
steps=int(input("Enter no of steps : "))
A=np.zeros((steps-1,steps-1))
B=np.zeros(steps-1)
k=2+0.1*h*h
for i in range(steps-1):
 for j in range(steps-1):
     if j==i:
         A[i,j]=k
     elif j==i+1 or j==i-1:
         A[i,j]=-1

for i in range(steps-1):
 if i==0:
     B[i]=40+0.1*h*h*20
 elif i==steps-2:
     B[i]=200+0.1*h*h*20
 else:
     B[i]=0.1*h*h*20
C=np.zeros(steps-1)
for w in range(steps-1):
 for q in range(steps-1):
     if q!=w:
         r=A[q,w]/A[w,w]
         for y in range(steps-1):
             A[q,y]=A[q,y]-r*A[w,y]
         B[q]=B[q]-r*B[w]
for q in range(steps-1):
 C[q]=B[q]/A[q,q]
T=np.zeros(steps+1)
x=np.zeros(steps+1)
for i in range(steps+1):
 if i==0:
     T[i]=40
 elif i==steps:
     T[i]=200
 else:
     T[i]=C[i-1]
 if i<steps:
     x[i+1]=x[i]+h
    
#plt.figure()
plt.grid(linestyle='-',linewidth=0.1,color='m')
plt.plot(x, T, 'r')

plt.title("Finite Difference Method")
plt.show()
