
import numpy as np
import matplotlib.pyplot as plt
import math
def f(x,y,n):
    phi=0
    for i in range(n+1):
        phi=phi+(4*10/math.pi)*np.exp(-math.pi*x*(2*i+1)/1)*np.sin(math.pi*(2*i+1)*y/1)/(2*i+1)
    return phi
            

t=10
xlist=np.linspace(0,1,10)
ylist = np.linspace(0,1,100)
for i in range(10):
    
    philist=f(xlist[i],ylist,t)/10
    plt.figure(num=0,dpi=150)
    plt.plot(ylist,philist,)
plt.xlabel("x/a")
plt.ylabel("$\phi$(x,y)/V")


#import numpy as np
#import matplotlib.pyplot as plt
#import math
def h(x,y,n):
    phi=0
    for i in range(n+1):
        phi=phi+(4*10/math.pi)*np.exp(-math.pi*x*(2*i+1)/1)*np.sin(math.pi*(2*i+1)*y/1)/(2*i+1)
    return phi
            

t=10
xlist=np.linspace(0,1,100)
ylist = np.linspace(0,1,10)
for i in range(10):
    
    philist=h(xlist,ylist[i],t)/10
    plt.figure(num=0,dpi=150)
    plt.plot(xlist,philist)
plt.xlabel("y/a")
plt.ylabel("$\phi$(x,y)/V")


#import numpy as np
#import matplotlib.pyplot as plt
#import math
def f(x,y,n):
    phi=(4*10/math.pi)*np.exp(-math.pi*x*(2*i+1)/1)*np.sin(math.pi*(2*i+1)*y/1)/(2*i+1)
    return phi
            

xlist=0.1
ylist=np.linspace(0,1,100)
t = np.linspace(0,100,100)
for i in range(100):
    
    philist=f(xlist,ylist,t[i])/10
    plt.figure(num=0,dpi=150)
    plt.plot(ylist,philist)

#import numpy as np
#import matplotlib.pyplot as plt
#import math
def f(x,y,n):
    phi=0
    for i in range(n+1):
        phi=phi+(4*10/math.pi)*np.exp(-math.pi*x*(2*i+1)/1)*np.sin(math.pi*(2*i+1)*y/1)/(2*i+1)
    return phi
            

t=100
xlist=np.linspace(0,1,10)
ylist = np.linspace(0,1,100)
for i in range(10):
    
    philist=f(xlist[i],ylist,t)/10
    plt.figure(num=0,dpi=150)
    plt.plot(ylist,philist,)
t=10

for i in range(10):
    
    philist=f(xlist[i],ylist,t)/10
    plt.figure(num=0,dpi=150)
    plt.plot(ylist,philist,)    
plt.xlabel("x/a")
plt.ylabel("$\phi$(x,y)")


#import numpy as np
#import matplotlib.pyplot as plt
#import math
def f(x,y,n):
    phi=0
    for i in range(n+1):
        phi=phi+(4*10/math.pi)*np.exp(-math.pi*x*(2*i+1)/1)*np.sin(math.pi*(2*i+1)*y/1)/(2*i+1)
    return phi
            

t=100
xlist=np.linspace(0,1,100)
ylist = np.linspace(0,1,10)
for i in range(10):
    
    philist=f(xlist,ylist[i],t)/10
    plt.figure(num=0,dpi=150)
    plt.plot(xlist,philist)
t=1
xlist=np.linspace(0,1,100)
ylist = np.linspace(0,1,10)
for i in range(10):
    
    philist=f(xlist,ylist[i],t)/10
    plt.figure(num=0,dpi=150)
    plt.plot(xlist,philist)    
plt.xlabel("y/a")
plt.ylabel("$\phi$(x,y)")




