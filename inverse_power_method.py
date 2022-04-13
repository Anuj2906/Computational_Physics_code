import numpy as np
print("Enter the size of matrix:")
n = int(input())  #size of array or variables in equation
a = np.zeros((n, n))
Y = np.zeros((n, n))
   
l = np.eye(n)         
u = np.zeros((n, n))
x = np.zeros((n))

#print('Enter Matrix Coefficients:')
#for i in range(n):
 #   for j in range(n):
  #      a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))
print("Enter the cofficient\n")
for i in range(n):
    a[i][i] = 4
for i in range(n-1):    
    a[i][i+1] = 2
    a[i+1][i] = 2
for i in range(n-2):    
    a[i][i+2]= 1
    a[i+2][i]= 1

    
print(a)        

# Decomposition    
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
# print("Lower tringular matrix L\n")                  
# print(l)            
# print("Upper tringular matrix U\n")                  
# print(u)
# print("Product of both L and U\n")
# result = np.dot(l, u)
# print(result)  
for v in range(n):
    # print("Enter the element of B\n")
    b = np.zeros((n))
    b[v] = 1

    

    # forward substitution
    for i in range(1, n):
        sum = b[i]
        for j in range(i):
            sum = sum - (l[i][j]*b[j])
        b[i] = sum
    # for i in range(n):
        # print('b[%d] = %0.6f' % (i, b[i]), end='\t')

    # back substitution
    x[n-1] = b[n-1]/u[n-1][n-1]
    for i in range(n-2, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] = x[i] - (u[i][j]*x[j])
        x[i] = x[i]/u[i][i]
    for k in range(n):
        Y[k][v]= x[k]
#     #Solution
#     for k in range(n):
#         print('X[%d] = %0.6f' % (k, x[k]), end='\t')
#     print('\n')    
# print(Y)





x = np.ones((n))

# Reading initial guess vector
# print('Enter initial guess vector: ')
# for i in range(n):
#     x[i] = float(input( 'x['+str(i)+']='))

# Reading tolerable error
tolerable_error = float(input('Enter tolerable error: '))

# Reading maximum number of steps
max_iteration = int(input('Enter maximum number of steps: '))

# Power Method Implementation
lambda_old = 1.0
condition =  True
step = 1
while condition:
    # Multiplying a and x
    x = np.matmul(Y,x)
    
    # Finding new Eigen value and Eigen vector
    lambda_new = max(abs(x))
    
    x = x/lambda_new
    
    # Displaying Eigen value and Eigen Vector
    print('\nSTEP %d' %(step))
    print('----------')
    print('Eigen Value = %0.6f' %(1/lambda_new))
    print('Eigen Vector: ')
    # x.T
    print(x)
    # for i in range(n):
    #     print('%0.3f\t' % (x[i]))
    
    # Checking maximum iteration
    step = step + 1
    if step > max_iteration:
        print('Not convergent in given maximum iteration!')
        break
    
    # Calculating error
    error = abs(lambda_new - lambda_old)
    print('errror=%0.6f'%(error))
    #lambda_old = lambda_new
    #condition = error > tolerable_error
