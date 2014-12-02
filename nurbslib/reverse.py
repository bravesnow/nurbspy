# -*- coding: cp936 -*-
from __future__ import division
import numpy as np
import parameterization as para
import linear

def reverse(Point, U):
    '''型值点反求控制点，Point是m+1(n-1)个行向量'''
    m=len(Point)-1
    n=m+2
    #U=para.accumul(Point,3)
    if len(Point.shape)==1:
        Point.shape=-1,1
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
        return fval*Point[i-1,:]
    #Ax=B
    A=np.zeros([n-1,n-1])
    A[0,:3]=1,0,0
    A[n-2,-3:]=0,0,1
    qder0=Point[1,:]-Point[0,:]
    qderm=Point[-1,:]-Point[-2,:]#端点切矢
    B=Point[0]+dt(3)*qder0/3
    for i in range(1,n-2):
        A[i,i-1:i+2]=a(i+1),b(i+1),c(i+1)
        B=np.vstack([B,e(i+1)])
    qderm=Point[m]-dt(n)*qderm/3
    B=np.vstack([B,qderm])
    solve = linear.solve(A,B)#方程的解
    solve = np.vstack([Point[0,:],solve,Point[-1,:]])
    return solve

if __name__=="__main__":
    import PendData as pd
    pv=pd.data(0.5,8,1.5)
    Point=pv[0]
    U=None#要给定参数化的
    print reverse(Point,U)

    
