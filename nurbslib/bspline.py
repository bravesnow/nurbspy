# -*- coding: cp936 -*-
# 输入：参数值序列ux，节点矢量U，控制点序列CtrlPoint，阶次k，导数阶r
# 输入：给定参数的B样条曲线上点/导数点
from __future__ import division
import numpy as np

#=================================================
def bspline(ux,CtrlPoint,U,k=3):
    '''B样条点值，列表参数序列ux，可以是一个单值，也可以是多值集合
    控制点CtrlPoint(行向量)，节点矢量U，样条次数k缺省为3'''
    if isinstance(ux,int) or isinstance(ux,float): #单值判断
        return deBoor(ux,CtrlPoint,U,k)
    else:
        rval=[deBoor(u,CtrlPoint,U,k) for u in ux]
        return np.array(rval)

def bsplineDer(ux,CtrlPoint,U,k=3,r=1):
    '''B样条曲线求导数，主要是参数列表B样条点之r阶导数，可以处理单值或者列表
    控制点CtrlPoint(行向量)，节点矢量U，样条次数k，导数阶数为r，参数u序列ux'''
    if isinstance(ux,int) or isinstance(ux,float): #单值判断
        return deBoorDer(ux,CtrlPoint,U,k,r)
    else:#列表推导式
        rval = [deBoorDer(u,CtrlPoint,U,k,r) for u in ux]
        return np.array(rval)

#================================================
def deBoor(u,CtrlPoint,U,k=3):
    ''' 德布尔算法：单值u在B样条曲线的点值'''
    def a(p,j):
        if U[j+k+1]==U[j+p]:
            return 0
        else:
            return (u-U[j+p])/(U[j+k+1]-U[j+p])
    def d(p,j):
        if p==0:
            return CtrlPoint[j,:]
        else:
            return (1-a(p,j))*d(p-1,j)+a(p,j)*d(p-1,j+1)
    if u>1:
        print u,"Error: u>1"
        return
    gen=(i for i in xrange(k,len(U)) if U[i]<=u<=U[i+1])#迭代生成器
    #此处如果u超过1该怎么样处理这个异常呢，需要详细添加。
    i=gen.next()#取迭代器的第一个值
    return d(k,i-k)

def deBoorDer(u,CtrlPoint,U,k=3,r=1):
    '''德布尔算法(les-P68)：单值u在B样条曲线的导数'''
    if u>1:
        print(u,"ERROR:u>1")
        exit(1)
    n=len(CtrlPoint)-1
    rU=U[1:-1]
    rCtrlPoint=[k*(CtrlPoint[i+1,:]-CtrlPoint[i,:])/(U[i+k+1]-U[i+1]) for i in range(0,n)]
    gen=(i for i in xrange(k,n+2) if U[i]<=u<=U[i+1])#迭代生成器
    i=gen.next()#取迭代器第一个值
    rCtrlPoint=np.array(CtrlPointr)
    if r==1:
        return deBoor(u,rCtrlPoint,rU,k-1)
    else:
        return deBoorder(u,rCtrlPoint,rU,k-1,r-1)

#=================================================
if __name__ == '__main__':
    CtrlPoint=np.array([[-24,0],[-12,6],[1,8],[10,2],[12,0] ])
    U=np.array([ 0,0,0,0,0.75,1,1,1,1 ])
    u = 0.9; ux=[0.5,0.8]
    f = lambda x: bspline(x, CtrlPoint, U)
    print f(ux), f(u)        
