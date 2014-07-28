# -*- coding: cp936 -*-
#б�����е���غ���
import numpy as np
def projfun(tls,r):
    #������ʱ���к͵����Ľ���
    if r>2:
        print "Error"
    if r==0:
        return [f(t) for t in tls]
    if r==1:
        return [f1der(t) for t in tls]
    if r==2:
        return [f2der(t) for t in tls]
def f(t,v0=39.2,a=np.pi/6,g=9.8):
    #б��ϵͳ��x,y��ĺ�������tΪ����
    fx=v0*np.cos(a)*t
    fy=v0*np.sin(a)*t-0.5*g*t**2
    return [fx,fy]#����ֵ��һ���б�
    
def f1der(t,v0=39.2,a=np.pi/6,g=9.8):
    #б��ϵͳ��x,y��ĺ�������tΪ����
    fx=v0*np.cos(a)
    fy=v0*np.sin(a)-g*t
    return [fx,fy]#����ֵ��һ���б�

def f2der(t,v0=39.2,a=np.pi/6,g=9.8):
    #б��ϵͳ��x,y��ĺ�������tΪ����
    fx=0
    fy=-g
    return [fx,fy]#����ֵ��һ���б�
    
if __name__ == '__main__':
    import invari
    for t in np.arange(0,9,0.45):
        p1=f1der(t)
        p2=f2der(t)
        print invari.curvature(p1,p2)
    

    
