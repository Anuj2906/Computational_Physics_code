import numpy as np
n = int(input('enter order of matrix = '))
a = np.zeros((n, n))
l = np.eye(n)
u = np.zeros((n, n))
b = np.zeros((n))
x = np.zeros((n))
print("Enter the coefficients of matrix a:\n")
for i in range(n):
    for j in range(n):
        a[i][j] = float(input('a['+str(i)+']['+str(j)+'] = '))
for i in range(n):
    for j in range(i+1, n):
        factor = a[j][i]/a[i][i]
        a[j][i] = factor
        l[j][i]= a[j][i]
        for k in range(n):
            a[j][k] = a[j][k]-(factor*a[i][k])
for i in range(n):
    for j in range(i,n):
        u[i][j]=a[i][j]            
print(l, end= '\n')            
print(u, end= '\n')
result = np.dot(l, u)
print(result)            

