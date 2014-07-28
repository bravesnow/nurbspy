# -*- coding: cp936 -*-
#�������ݵ㣬������Ӧ����ʸ,����p��������
import numpy as np
import para
import error
from math import sqrt
#20140515ע�⣺���õĵ㶼�Ƕ�u�ĵ��������Ƕ�t�ģ��мǰ�
def fmill(p,T):
    #���ܶ�����
    #�˴����󣬲�֪���ǳ�������⣬���Ǳ���ķ��������⡣
    #U=para.accumul(p,0)
    #warning:û�г�ʼ����ֹ��ֵ����ʸ
    #U=para.uniform(T,0)
    U=T
    r,c=p.shape#����
    n=r-1
    deltap=p[2:n+1,:]-p[0:n-1,:]
    g1=lambda vec:sqrt(sum(vec**2))#������ģ����������
    t=[x/g1(x) for x in deltap]
    deltaU=U[2:n+1]-U[0:n-1]
    pder=[t[i]/deltaU[i] for i in xrange(len(t))]
    g=lambda i:(p[i+1,:]-p[i,:])/(U[i+1]-U[i])
    pder0=2*g(0)-pder[0]
    pdern=2*g(n-1)-pder[-1]
    pder.insert(0,pder0)
    pder.append(pdern)
    return np.array(pder)

def bessell(p,T):
    #��t�󵼵�
    #(old����������:ע������ɶ�u��ת���ɶ�t��)
    #U=para.accumul(p,0)#���ݵ����
    U=T
    r,c=p.shape#����
    n=r-1
    deltap=p[2:n,:]-p[0:n-2,:]
    deltaU=U[2:]-U[1:-1]
    g=lambda i:(p[i+1,:]-p[i,:])/(U[i+1]-U[i])
    f=lambda i:(U[i+1]-U[i],U[i]-U[i-1])/(U[i+1]-U[i-1])
    h=lambda i:f(i)[0]*g(i-1)+f(i)[1]*g(i)                                 
    pder=map(h,xrange(1,n))
    pder0=2*g(0)-pder[0]
    pdern=2*g(n-1)-pder[-1]
    pder.insert(0,pder0)
    pder.append(pdern)
    return np.array(pder)

def akima(p,T):
    #��䷽��:ע����Ƕ�t�󵼣�û����ֵ���ֵ����ʸ
    U=T
    r,c=p.shape
    n=r-1
    f=lambda vec:sqrt(sum(vec**2))#������ģ����������
    g=lambda i:(p[i+1,:]-p[i,:])/(U[i+1]-U[i])
    a=lambda i:f(g(i-2))/(f(g(i-2))+f(g(i)))
    h=lambda i:(1-a(i))*g(i-1)+a(i)*g(i)
    pder=map(h,xrange(1,n))
    pder0=2*g(0)-pder[0]
    pdern=2*g(n-1)-pder[-1]
    pder.insert(0,pder0)
    pder.append(pdern)
    return np.array(pder)

def test(p,T):
    #�����ֵС��1��ʱ�򣬵����ʸ����Ч
    #���ݺ������ַ���������
    p,pder=data(T)#��ȡ���ݵ�   
    '''��ʼʵ��'''
##    fder=fmill(p,tlimit)#�����⣬��Ҫ����
##    print error.rmse(pder,fder)#ά��ͳһ
    bder=bessell(p,tlimit)
    print error.rmse(pder,bder)
##    ader=akima(p,tlimit)
##    print error.rmse(pder,ader)
   
if __name__=='__main__':
    import LorenzData as dlib
    main(dlib.data,0.03)
