import numpy as np 
import math
n= int(input('order of matrix = '))
a= np.zeros((n,n))
l= np.zeros((n,n))
b= np.zeros((n))
x= np.zeros((n))
print('Enter the elements of matrix a:\n')
for i in range(n):
    for j in range(n):
        a[i][j]= float(input('a['+str(i)+']['+str(j)+'] = '))       
for k in range(n):
    for i in range(k):
        sum = 0
        for j in range(i):
            sum = sum + a[i][j]*a[k][j]
        a[k][i]= (a[k][i]-sum)/a[i][i]
        l[k][i]= a[k][i]
    sum = 0
    for j in range(k):
        sum = sum + a[k][j]*a[k][j]
    a[k][k] =math.sqrt(a[k][k] - sum)  
    l[k][k] = a[k][k]
print(l)
print("\n")
t = l.T
print(t)
print("\n")
result = np.dot(l, t)