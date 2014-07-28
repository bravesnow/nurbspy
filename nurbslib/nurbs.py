# -*- coding: cp936 -*-
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
#已经修改完毕。
def N(i,k,u,U):
    #B样条基函数定义
    if k==0:
        if U[i]<=u<U[i+1]:return 1
        else:return 0
    else:
        if U[i+k]==U[i]:a=0
        else:
            a=(u-U[i])/(U[i+k]-U[i])
        if U[i+k+1]==U[i+1]:b=0
        else:
            b=(U[i+k+1]-u)/(U[i+k+1]-U[i+1])
        return a*N(i,k-1,u,U)+b*N(i+1,k-1,u,U)
def inNbs(P,U,ulst,k=3):
    from scipy import interpolate
    '''封装Python scipy库的B样条插值函数'''
    '''型值点(不是控制点),参数列表(不是节点矢量),阶次(整数，或者字符串指定)'''
    '''返回值是关于参数u的函数'''
    #虽然此结果很不错，但是其中的插值，控制点与型值点有较大的不同，被优化了！
    if len(P.shape)!=1:
        P=np.transpose(P)
    f=interpolate.interp1d(U,P,k)
    ret=f(ulst)#结果做一次转置，为了统一点的维数
    return np.transpose(ret)
           
'''Nurbs点与导数'''
def Nurbs(dP,w,U,ulist,k=3):
    #可能有问题，待检测
    '''控制点,节点矢量,权因子,参数列表,默认参数样条次数'''
    #扩展成高一维的控制点
    dPw=np.array([np.hstack([dP[i,:]*w[i],w[i]]) for i in xrange(0,len(w))])
    Cw=bspmak(dPw,U,k,ulist)#对高一维的控制点得到B样条曲线
    f=lambda vec:vec[0:-1]/vec[-1]#匿名函数：向量降一维
    C=[f(vec) for vec in Cw]#对所得的B样条点降一维得到Nurbs点
    return np.array(C)
def Nurbsder(dP,w,U,ulist,r=1,k=3):
    '''控制点,节点矢量,权因子,参数列表,导数的次数，样条次数'''
    #扩展成高一维的控制点
    dPw=np.array([np.hstack([dP[i,:]*w[i],w[i]]) for i in xrange(0,len(w))])
    def der(u):
        #对单值参数u，求其导数点
        Aw=bspmak(dPw,U,k,u)#高一维Nurbs(A(u) w(u))
        Awr=deBoorder(dPw,U,k,u,r)#高一维Nurbs导数(A'(u) w'(u))
        Cu=Aw[0:-1]/Aw[-1]#降一维得Nurbs点
        return (Awr[0:-1]-Awr[-1]*Cu)/Aw[-1]
    rder=[der(u) for u in ulist]#对参数列表计算Nurbs导数
    return np.array(rder)
'''B样条点与导数'''
def bspmak(dP,U,k,ulist):
    '''B样条曲线构建
    控制点dP(行向量)，节点矢量U，样条次数k
    参数u序列ulist'''
    if isinstance(ulist,int) or isinstance(ulist,float):
        #判断是不是单值
        return deBoor(dP,U,k,ulist)
    else:
        #列表推导式
        rval=[deBoor(dP,U,k,u) for u in ulist]
        return np.array(rval)

def bspder(dP,U,k,ulist,r=1):
    '''B样条曲线求导数，主要是参数列表
控制点dP(行向量)，节点矢量U，样条次数k，次数为r，参数u序列ulist'''
    if isinstance(ulist,int) or isinstance(ulist,float):
        #判断是不是单值
        return deBoorder(dP,U,k,ulist,r)
    else:
        #列表推导式
        rval=[deBoorder(dP,U,k,u,r) for u in ulist]
        return np.array(rval)
'''B样条的德布尔算法'''
def deBoor(dP,U,k,u):
    '''对单值u求得B样条曲线的点值,实现的算法是德布尔算法'''
    def a(p,j):
        if U[j+k+1]==U[j+p]:
            return 0
        else:
            return (u-U[j+p])/(U[j+k+1]-U[j+p])
    def d(p,j):
        if p==0:
            return dP[j,:]
        else:
            return (1-a(p,j))*d(p-1,j)+a(p,j)*d(p-1,j+1)
    gen=(i for i in xrange(k,len(U)) if U[i]<=u<=U[i+1])#迭代生成器
    #此处如果u超过1该怎么样处理这个异常呢，需要详细添加。
    i=gen.next()#取迭代器的第一个值
    return d(k,i-k)

def deBoorder(dP,U,k,u,r):
    '''单值u的B样条曲线的导数，使用的是德布尔算法lesP68'''
    n=len(dP)-1
    Ur=U[1:-1]
    dPr=[k*(dP[i+1,:]-dP[i,:])/(U[i+k+1]-U[i+1]) for i in range(0,n)]
    gen=(i for i in xrange(k,n+2) if U[i]<=u<=U[i+1])#迭代生成器
    i=gen.next()#取迭代器第一个值
    dPr=np.array(dPr)
    if r==1:
        return deBoor(dPr,Ur,k-1,u)
    else:
        return deBoorder(dPr,Ur,k-1,u,r-1)
if __name__ == '__main__':
    #控制点矩阵
    dP=np.array([[-24,0],[-12,6],[1,8],[10,2],[12,0] ])
    w=np.array([1,1,1,1,1])
    #节点矢量
    U=np.array([ 0,0,0,0,0.75,1,1,1,1 ])
    #次数
    k=3;u=[0.5,0.8]
    #print bspmak(dP,U,k,u)
    #print Nurbs(dP,w,U,u)
    print Nurbsder(dP,w,U,u)
    #print bspder(d,U,k,0.5,1)#当0.8的时候有问题，测试。还有如何扩展成列表。


##=======================================================================
##代码分割线:本代码来自施法中P244页的算法，存在一些问题，尚未找到。
##def bspder(dP,U,k,u,r):
##    '''德布尔算法求b样条r阶导数'''
##    n=len(dP)-1
##    gen=(i for i in xrange(k,n+2) if U[i]<=u<=U[i+1])#迭代生成器
##    i=gen.next()#取迭代器第一个值
##    print i
##    def d(p,j):
##        if p==0:
##            return dP[j,:]
##        else:
##            return (k-p+1)*(d(p-1,j+1)-d(p-1,j))/(U[j+k+1]-U[j+p])
##    dPr=[d(r,it) for it in xrange(i-k,i-r+1)]
##    #dPr.append(dP[-1,:])
##    dPr=np.array(dPr)
##    print dPr
##    Ur=np.hstack([np.zeros(k+1-r),U[k+1:n+1],np.ones(k+1-r)])
##    kr=k-r
##    return deBoor(dPr,Ur,kr,u)

##def bspder(dP,U,k,u,r):
##    n=len(dP)-1
##    gen=(i for i in xrange(k,n+2) if U[i]<=u<=U[i+1])#迭代生成器
##    i=gen.next()#取迭代器第一个值
##    print i
##    def dr(p,j):
##        if p==0:
##            return dP[j,:]
##        else:
##            return (k-p+1)/(U[j+k+1]-U[j+p])*(dr(p-1,j+1)-dr(p-1,j))
##    a=[dr(r,j)*N(j,k-r,u,U) for j in xrange(i-k,i-r+1)]#此处问题待定。
##    print a
##    a=[N(j,k-r,u,U) for j in range(i-k,i-r+1)]#此处问题待定。


