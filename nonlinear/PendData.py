# -*- coding: cp936 -*-
#单摆数据的提取
#单摆simple pendulum运动方程
#物理非线性动力方程，微分方程的数值解法数据点及其导数
import numpy as np
import math
from scipy.integrate import odeint
def pend(w,t):
    m,l,k,g=1.,1.,1.,9.8
    x1,x2=w
    dx1=x2
    dx2=-g/l*np.sin(x1)-k/m*x2
    return dx1,dx2

def data(t,initial=(math.pi/12,0)):
    #参数t是时间序列
    #initial=(math.pi/12,0)#初值对应于init时间的时候
    #initial=(math.pi/6,0)
    #warning:求解微分方程的时候,t从0开始对应初值,init参数为零
    points=odeint(pend,initial,t)
    m,l,k,g=1.,1.,1.,9.8
    x1,x2=points[:,0],points[:,1]
    pointsder=[x2,-g/l*np.sin(x1)-k/m*x2]
    pointsder=np.transpose(pointsder)#转置
    return points,pointsder

def penddata(init,final,step):
    t=np.arange(init,final,step)#时间取值序列
    initial=(math.pi/12,0)#初值对应于init时间的时候
    #warning:求解微分方程的时候,t从0开始对应初值,init参数为零
    points=odeint(pend,initial,t)
    m,l,k,g=1.,1.,1.,9.8
    x1,x2=points[:,0],points[:,1]
    pointsder=[x2,-g/l*np.sin(x1)-k/m*x2]
    pointsder=np.transpose(pointsder)#转置
    return points,pointsder

if __name__=='__main__':
    import matplotlib.pyplot as plt
    T=np.arange(0,5.,0.1)
    p,pder=data(T)
    i=0
    for v in p:
        s=str(i)
        plt.text(v[0],v[1],s)
        i=i+1
    plt.plot(p[0:5,0],p[0:5,1],'r-->')
    plt.plot(p[4:9,0],p[4:9,1],'r-o')
    plt.plot(p[8:29,0],p[8:29,1],'b-*')
    plt.plot(p[28:49,0],p[28:49,1],'g-<')
    plt.show()
    
