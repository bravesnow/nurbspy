# -*- coding: cp936 -*-
from __future__ import division
import numpy as np
from scipy import linalg as lin
import matplotlib.pyplot as plt
import para,enlin
import PendData as pd
def reverse(q,U):
    #此处修改了参数个数，如果出现问题，请注意。
    #型值点反求控制点
    #q是m+1(n-1)个行向量
    m=len(q)-1
    n=m+2
    #U=para.accumul(q,3)
    if len(q.shape)==1:
        q.shape=-1,1
    def dt(i):
        return U[i+1]-U[i]
    def a(i):
        pval=dt(i+2)**2
        nval=dt(i)+dt(i+1)+dt(i+2)
        return pval/nval
    def b(i):
        fpval=dt(i+2)*(dt(i)+dt(i+1))
        fnval=dt(i)+dt(i+1)+dt(i+2)
        bpval=dt(i+1)*(dt(i+2)+dt(i+3))
        bnval=dt(i+1)+dt(i+2)+dt(i+3)
        return fpval/fnval+bpval/bnval
    def c(i):
        pval=dt(i+1)**2
        nval=dt(i+1)+dt(i+2)+dt(i+3)
        return pval/nval
    def e(i):
        fval=dt(i+1)+dt(i+2)
        return fval*q[i-1,:]
    #Ax=B
    A=np.zeros([n-1,n-1])
    A[0,:3]=1,0,0
    A[n-2,-3:]=0,0,1
    qder0=q[1,:]-q[0,:]
    qderm=q[-1,:]-q[-2,:]#端点切矢
    B=q[0]+dt(3)*qder0/3
    for i in range(1,n-2):
        A[i,i-1:i+2]=a(i+1),b(i+1),c(i+1)
        B=np.vstack([B,e(i+1)])
    qderm=q[m]-dt(n)*qderm/3
    B=np.vstack([B,qderm])
    solve=enlin.enlin(A,B)#方程的解
    solve=np.vstack([q[0,:],solve,q[-1,:]])
    return solve

if __name__=="__main__":
    pv=pd.penddata(0.5,8,1.5)
    q=pv[0]
    U=None#要给定参数化的
    print reverse(q,U)

    
