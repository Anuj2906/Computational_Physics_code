import numpy as np

# import sys

# Reading number
n = int(input('Enter order of matrix: '))

Y = float(input('Enter Y: '))  # Input lemda calue in range 0 to 2
es = 0.0000001                 # maximum error

# numpy array of size nxn+1

a = np.zeros((n, n+1))

# Making numpy array of n size and initializing

x = np.zeros(n)
dummy = 0.0
big = 0.0


# Reading of array element
print('Enter element of array:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input('a['+str(i)+']['+str(j)+'] = '))

for i in range(n):
    p = i  # pivoting row
    big = abs(a[i][i])   # pivoting element
    for k in range(n):
        if(i != k):
            dummy = abs(a[i][k])
        if(dummy > big):
            big = dummy
            p = k

# Swapping the pivoting row
    if(p != i):
        for j in range(n+1):
            dummy = a[p][j]
            a[p][j] = a[i][j]
            a[i][j] = dummy
print(a)

# Here we find the variable solution x[i] in form of other variable
for i in range(n):
    dummy = a[i][i]
    for j in range(n+1):
        a[i][j] = a[i][j]/dummy
for i in range(n):
    sum = a[i][n]
    for j in range(n):
        if(i != j):
            sum = sum - a[i][j]*x[j]
    x[i] = sum

# Here we perform iteration and error analysis
sentinel = 1
count = 0
while(sentinel == 1):
    for i in range(n):
        old = x[i]
        sum = a[i][n]
        for j in range(n):
            if(i != j):
                sum = sum - a[i][j]*x[j]
        x[i] = Y*sum + (1-Y)*old
        count=count+1
        if(sentinel == 1 and x[i] != 0):
            ea = abs((sum - old))
        if(ea < es):
            sentinel = 0
        print('X[%d] = %0.6f' % (i, sum), end='\t')   # print solution in each step
        print('error = %0.7f'%(sum-old),end='\n')             #error

print(count/3)