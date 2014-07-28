# coding:cp936
# Wed Apr 30 08:46:02 2014
import numpy as np
import PendData as pd
m,l,k,g=1.,1.,1.,9.8

def fder(points,nder):
    if nder==1:
        return f1der(points)
    if nder==2:
        return f2der(points)
    else:
        print "Error"
        return
    
def f1der(points):
    f=lambda x,y: [y,-g/l*np.sin(x)-k/m*y]
    return [f(x,y) for [x,y] in points]

def f2der(points):
    fx=lambda x,y:-g/l*np.sin(x)-k/m*y
    fy=lambda x,y: -g/l*np.cos(x)*y+k*g/(l*m)*np.sin(x)+k**2/m**2*y
    f=lambda x,y: [fx(x,y),fy(x,y)]
    return [f(x,y) for [x,y] in points]

if __name__ == '__main__':
    p=pd.penddata(0,10,0.1)
    p1der = f1der(p)
    p2der = f2der(p)
    
