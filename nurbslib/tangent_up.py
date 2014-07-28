# -*- coding: cp936 -*-
#给出数据点，计算相应的切矢,参数p是行向量
import numpy as np
import para
import error
from math import sqrt
#20140515注意：所得的点都是对u的导数，不是对t的，切记啊
def fmill(p,T):
    #弗密尔方法
    #此处误差极大，不知道是程序的问题，还是本身的方法有问题。
    #U=para.accumul(p,0)
    #warning:没有初始与终止的值的切矢
    #U=para.uniform(T,0)
    U=T
    r,c=p.shape#行列
    n=r-1
    deltap=p[2:n+1,:]-p[0:n-1,:]
    g1=lambda vec:sqrt(sum(vec**2))#求向量模的匿名函数
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
    #对t求导的
    #(old贝塞尔方法:注意的是由对u求导转换成对t求导)
    #U=para.accumul(p,0)#数据点参数
    U=T
    r,c=p.shape#行列
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
    #秋间方法:注意的是对t求导，没有终值与初值的切矢
    U=T
    r,c=p.shape
    n=r-1
    f=lambda vec:sqrt(sum(vec**2))#求向量模的匿名函数
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
    #当这个值小于1的时候，点差切矢才有效
    #数据衡量三种方法的优劣
    p,pder=data(T)#提取数据点   
    '''开始实验'''
##    fder=fmill(p,tlimit)#有问题，需要调试
##    print error.rmse(pder,fder)#维数统一
    bder=bessell(p,tlimit)
    print error.rmse(pder,bder)
##    ader=akima(p,tlimit)
##    print error.rmse(pder,ader)
   
if __name__=='__main__':
    import LorenzData as dlib
    main(dlib.data,0.03)
