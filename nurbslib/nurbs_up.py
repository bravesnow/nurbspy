# -*- coding: cp936 -*-
#待检测
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import reverse
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
#=======================================================
'''Nurbs点与导数'''
def nbs(eu,dP,w,U,k=3):
    '''控制点,节点矢量,权因子,参数列表,默认参数样条次数'''
    '''此函数主要在nurbs_high.py有新的修改'''
    #扩展成高一维的控制点
    dPw=np.array([np.hstack([dP[i,:]*w[i],w[i]]) for i in xrange(0,len(w))])
    #dPw=reverse.reverse(dPw,U)
    Cw=bs(eu,dPw,U,k)#对高一维的控制点得到B样条曲线
    Cw.shape=(-1,3)#转换一下维度
    f=lambda vec:vec[0:-1]/vec[-1]#匿名函数：向量降一维
    C=[f(vec) for vec in Cw]#对所得的B样条点降一维得到Nurbs点
    return np.array(C)
def nbsder(eu,dP,w,U,k=3,r=1):
    '''控制点,节点矢量,权因子,参数列表,导数的次数，样条次数'''
    #扩展成高一维的控制点
    dPw=np.array([np.hstack([dP[i,:]*w[i],w[i]]) for i in xrange(0,len(w))])
    def der(u):
        #对单值参数u，求其导数点
        Aw=bspmak(u,dPw,U,k)#高一维Nurbs(A(u) w(u))
        Awr=deBoorder(u,dPw,U,k,r)#高一维Nurbs导数(A'(u) w'(u))
        Cu=Aw[0:-1]/Aw[-1]#降一维得Nurbs点
        return (Awr[0:-1]-Awr[-1]*Cu)/Aw[-1]
    rder=[der(u) for u in eu]#对参数列表计算Nurbs导数
    return np.array(rder)
#=========================================================
'''B样条点，可以处理单值和列表'''
def bs(eu,dP,U,k=3):
    '''B样条曲线构建
    控制点dP(行向量)，节点矢量U，样条次数k
    参数u序列eu'''
    if isinstance(eu,int) or isinstance(eu,float):
        #判断是单值，直接求
        return deBoor(eu,dP,U,k)
    else:
        #列表推导式
        rval=[deBoor(u,dP,U,k) for u in eu]
        return np.array(rval)
'''B样条点之r阶导数，可以处理单值或者列表'''
def bsder(eu,dP,U,k=3,r=1):
    '''B样条曲线求导数，主要是参数列表
控制点dP(行向量)，节点矢量U，样条次数k，次数为r，参数u序列eu'''
    if isinstance(eu,int) or isinstance(eu,float):
        #判断单值
        return deBoorder(eu,dP,U,k,r)
    else:
        #列表推导式
        rval=[deBoorder(u,dP,U,k,r) for u in eu]
        return np.array(rval)
#===========================================================
'''B样条的德布尔算法'''
def deBoor(u,dP,U,k=3):
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
    if u>1:
        print u,"Error: u>1"
        return
    gen=(i for i in xrange(k,len(U)) if U[i]<=u<=U[i+1])#迭代生成器
    #此处如果u超过1该怎么样处理这个异常呢，需要详细添加。
    i=gen.next()#取迭代器的第一个值
    return d(k,i-k)

def deBoorder(u,dP,U,k=3,r=1):
    '''单值u的B样条曲线的导数，使用的是德布尔算法lesP68'''
    if u>1:
        print u,"Error: u>1"
        return
    n=len(dP)-1
    Ur=U[1:-1]
    dPr=[k*(dP[i+1,:]-dP[i,:])/(U[i+k+1]-U[i+1]) for i in range(0,n)]
    gen=(i for i in xrange(k,n+2) if U[i]<=u<=U[i+1])#迭代生成器
    i=gen.next()#取迭代器第一个值
    dPr=np.array(dPr)
    if r==1:
        return deBoor(u,dPr,Ur,k-1)
    else:
        return deBoorder(u,dPr,Ur,k-1,r-1)
#===========================================================
#主函数测试
if __name__ == '__main__':
    #控制点矩阵
    dP=np.array([[-24,0],[-12,6],[1,8],[10,2],[12,0] ])
    w=np.array([1,1,0.8,1,1])
    #节点矢量
    U=np.array([ 0,0,0,0,0.75,1,1,1,1 ])
    #次数
    k=3;u=[0.5,0.8]
    h = lambda u: nbs(u,dP,w,U)
    print h(0.9)



