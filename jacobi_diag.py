import numpy as np

n= int(input('Enter the order of matrix: '))
a= np.zeros((n,n))

with open(r'in.txt') as f:
     a = [[float(num) for num in line.split(',')] for line in f]

#For banded matrix.
#for i in range(n):
#    a[i][i] = 4
#for i in range(n-1):    
#    a[i][i+1] = 2
#    a[i+1][i] = 2
#for i in range(n-2):    
#    a[i][i+2]= 1
#    a[i+2][i]= 1

print(a)    
Tolerance = 0.000001
step = 1
max_iteration= 1000
v=1
while(v==1):
    sum = 0
    max= -100
    
    for i in range(n):
        for j in range(i+1,n):
            if(abs(a[i][j])>max):
                max= abs(a[i][j])
                p= i
                q= j
    o = (a[q][q] - a[p][p])/(2*a[p][q])
    si = np.sign(o)
    if(si==0):
        si = 1
    t= si/(abs(o)+np.sqrt(o*o+1))
    c= 1/(np.sqrt(1+t*t))
    s= c*t
    
    r =np.eye(n)
    r[p][p]= c
    r[q][q]= c
    r[p][q]= s
    r[q][p]= -s
    rt = r.T
    print(r)
    D = rt.dot(a)
    D = D.dot(r)
    a=D
    step = step + 1
    print(step)
    
    if(step > max_iteration):
        print('Not convergent in given maximum iteration!')
        break
    for i in range(n):
        for j in range(i+1, n):
            sum = sum + abs(a[i][j])
    if(sum < Tolerance):        
        v = 0
print(D)
print(r)
Y= np.zeros(n)
for i in range(n):
    Y[i]= a[i][i]
Y = sorted(Y)  
for i in range(n-1,-1,-1): 
    print('Y[%d] = %0.5f' % (i, Y[i]), end='\t\n')
print(D)    