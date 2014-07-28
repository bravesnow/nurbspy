# coding: cp936
import numpy as np
from scipy.integrate import odeint

def lorenz(w,t,a,r,b):
    #����λ��ʸ��w,����������p,r,b�����
    #dx/dt,dy/dt,dz/dt��ֵ
    x,y,z=w
    return np.array([a*(y-x), x*(r-z)-y, x*y-b*z])

def data(T,initval=(0.,1.,0.),args=(16.,45.92,4.)):
    #����ʱ����T,��ֵinitval,Lorenz���̲���args,������ȱʡ����
    points=odeint(lorenz,initval,T,args)
    a,r,b=args
    f=lambda (x,y,z):[a*(y-x), x*(r-z)-y, x*y-b*z]
    pointsder=np.array([f(x) for x in points])
    return points,pointsder

if __name__=='__main__':   
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D    
    T=np.arange(0,20,0.01)
    p,pder=data(T,(0,1.,0),(10,3,8./3))
    plt.plot(p[:,0],p[:,1])
##    ax = Axes3D(plt.figure())  
##    ax.plot(p[:,0], p[:,1], p[:,2])
    plt.show()
