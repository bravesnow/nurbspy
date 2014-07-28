#coding: cp936
import numpy as np

def data(T,v0=39.2,a=np.pi/6,g=9.8):
    fx=lambda t:v0*np.cos(a)*t
    #warning:整数的除法要特别注意
    fy=lambda t:v0*np.sin(a)*t-0.5*g*t**2
    fxder=lambda t:v0*np.cos(a)
    fyder=lambda t:v0*np.sin(a)-g*t
    
    points=[(fx(t),fy(t)) for t in T]
    points=np.array(points)
    pointsder=[(fxder(t),fyder(t)) for t in T]
    return np.array(points),np.array(pointsder)
    
if __name__=="__main__":
    import matplotlib.pyplot as plt
    T=np.arange(0,10.,0.5)
    p,pder=data(T)
    plt.plot(p[:,0],p[:,1],'*--')
    plt.show()
    
