# -*- coding: cp936 -*-
#�ڵ�ʸ��
#�������ݵ����������
#����Ϊ���ݵ㼯q,����k
from __future__ import division
import numpy as np
import math
import PendData as pd
#ע���Ѿ�ȫ����һ���ˣ�����ֱ��ʹ��
def uniform(T,k=3):
    #���Ȳ�����&&�Ⱦ������
    T=T-T[0]#ӳ�䵽0-End
    T=T/T[-1]#ӳ�䵽0-1
    T=np.hstack([np.zeros(k),T,np.ones(k)])
    return T
def frac(T,k=3):
    #һ���µĳ��ԣ�Ϊ����չt������
    T=T/(1.0+T)
    T=np.hstack([np.zeros(k),T,np.ones(k)])
    return T

def accumul(q,k=3,argv=False):
    #�淶�����ҳ���������
    if len(q.shape)==1:#һά�޸ĳɶ�ά
        q.shape=-1,1#��ֱ�Ӷ�T���ҳ��������ˣ�
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
    #���Ĳ�����
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
    #����������
    if len(q.shape)==1:
        q.shape=-1,1
    pass

if __name__=="__main__":
    qv=pd.penddata(0.5,5,0.5)
    q=qv[0]
    print accumul(q,3,True)
