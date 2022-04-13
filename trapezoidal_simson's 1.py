import numpy as np

def T(x, y):
    return 2 * x * y + 2 * x - x * x - 2 * y * y + 72
xi,yi = 0,0
xf,yf = 8,6
steps=list(map(int,input('No. of steps: ').split()))

#Code for Trapezoidal method:
print('\nTrapezoidal')
ans =[]
for l in steps:
 hx,hy = xf/l,yf/l
 I = 0
 for i in np.arange(0,xf,hx):
     for j in np.arange(0,yf,hy):
         I += (T(i,j)+2*T(i,j+hy)+T(i,j+2*hy))*(hy*hx/4)
         avg = I/(6*8)
 ans.append(abs(avg))
 print('No. of steps: '+str(l),'\tIntegration Value:'+str(abs(round(I,4))),'\tAverage Value'+str(abs(round(avg,4))))


#Code for Simpson’s (1/3)rd rule:
print('\nSimpson 1/3th')
for l in steps:
 hx,hy= xf/l,yf/l
 I = 0
 for i in np.arange(0,xf,hx):
     for j in np.arange(0,yf,hy):
         I += (T(i,j)+4*T(i,j+hy/2)+T(i,j+hy))*(hy*hx/6)
         avg = I/(6*8)
 ans.append(abs(avg))
 print('No. of steps: '+str(l),'\tIntegration Value:'+str(abs(round(I,4))),'\tAverage Value'+str(abs(round(avg,4))))

 


#code for Simpson’s (3/8)th method:
print('\nSimpson 3/8th')
for l in steps:
 hx,hy= xf/l,yf/l
 I = 0
 for i in np.arange(0,xf,hx):
     for j in np.arange(0,yf,hy):
         I += (T(i,j)+3*T(i,j+hy/3)+3*T(i,j+(2/3)*hy)+T(i,j+hy))*(hy*hx/8)
         avg = I/(6*8)
 ans.append(abs(avg))
 print('No. of steps: '+str(l),'\tIntegration Value: '+str(abs(round(I,4))),'\tAverage Value: '+str(abs(round(avg,4))))

