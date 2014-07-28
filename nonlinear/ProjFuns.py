# -*- coding: cp936 -*-
#斜拋运行的相关函数
import numpy as np
def projfun(tls,r):
    #参数是时间列和导数的阶数
    if r>2:
        print "Error"
    if r==0:
        return [f(t) for t in tls]
    if r==1:
        return [f1der(t) for t in tls]
    if r==2:
        return [f2der(t) for t in tls]
def f(t,v0=39.2,a=np.pi/6,g=9.8):
    #斜拋系统的x,y轴的函数，以t为参数
    fx=v0*np.cos(a)*t
    fy=v0*np.sin(a)*t-0.5*g*t**2
    return [fx,fy]#返回值是一个列表
    
def f1der(t,v0=39.2,a=np.pi/6,g=9.8):
    #斜拋系统的x,y轴的函数，以t为参数
    fx=v0*np.cos(a)
    fy=v0*np.sin(a)-g*t
    return [fx,fy]#返回值是一个列表

def f2der(t,v0=39.2,a=np.pi/6,g=9.8):
    #斜拋系统的x,y轴的函数，以t为参数
    fx=0
    fy=-g
    return [fx,fy]#返回值是一个列表
    
if __name__ == '__main__':
    import invari
    for t in np.arange(0,9,0.45):
        p1=f1der(t)
        p2=f2der(t)
        print invari.curvature(p1,p2)
    

    
