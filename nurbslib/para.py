# -*- coding: cp936 -*-
#节点矢量
#各种数据点参数化方法
#参数为数据点集q,次数k
from __future__ import division
import numpy as np
import math
import PendData as pd
#注：已经全部归一化了，可以直接使用
def uniform(T,k=3):
    #均匀参数化&&等距参数化
    T=T-T[0]#映射到0-End
    T=T/T[-1]#映射到0-1
    T=np.hstack([np.zeros(k),T,np.ones(k)])
    return T
def frac(T,k=3):
    #一种新的尝试，为了扩展t到无穷
    T=T/(1.0+T)
    T=np.hstack([np.zeros(k),T,np.ones(k)])
    return T

def accumul(q,k=3,argv=False):
    #规范积累弦长参数化法
    if len(q.shape)==1:#一维修改成二维
        q.shape=-1,1#可直接对T求弦长参数化了！
    m=len(q)-1
    U=np.array([0])
    for i in range(1,m+1):
        tmp=np.sum((q[i,:]-q[i-1,:])**2)
        tmp=math.sqrt(tmp)
        tmp=tmp+U[i-1]
        U=np.hstack([U,tmp])
    sumU=U[-1]
    U=U/U[-1]
    U=np.hstack([np.zeros(k),U,np.ones(k)])
    if argv:
        return U,sumU
    else:
        return U

def centrip(q,k=3,argv=False):
    #向心参数化
    if len(q.shape)==1:
        q.shape=-1,1
    m=len(q)-1
    U=np.array([0])
    for i in range(1,m+1):
        tmp=np.sum((q[i,:]-q[i-1,:])**2)
        tmp=math.sqrt(math.sqrt(tmp))
        tmp=tmp+U[i-1]
        U=np.hstack([U,tmp])
    sumU=U[-1]
    U=U/U[-1]
    U=np.hstack([np.zeros(k),U,np.ones(k)])
    if argv:
        return U,sumU
    else:
        return U
    
def foley(q,k=3):
    #福利参数化
    if len(q.shape)==1:
        q.shape=-1,1
    pass

if __name__=="__main__":
    qv=pd.penddata(0.5,5,0.5)
    q=qv[0]
    print accumul(q,3,True)
