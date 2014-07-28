# -*- coding: cp936 -*-
#��Ҫʹ������Ȩ������Ϊ���Ƶ��Ȩ���ӣ�ʧ��
#��Ϊ�õ�������ֻ�����Ƕ�Ӧ����ֵ���Ȩ���ӣ��޷���չ������
from __future__ import division
import numpy as np
from scipy import linalg as lin
import matplotlib.pyplot as plt
import para,enlin,tangent_up,invari
import PendData as pd
def N(i,u,U,k=3):
    #B��������������
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
            
        return a*N(i,u,U,k-1)+b*N(i+1,u,U,k-1)
    
def wN(i,u,U,w,k=3):
    return w[i]*N(i,u,U)

def arrwN(u,U,w):
    return [wN(i,u,U,w) for i in range(len(w))]

def arrw(w):
    #�γ�Ȩ���Ӿ���
    n=len(w)-1
    a = np.zeros((n-1,n-1))
    for i in range(1,n-2):
        a[i,i-1:i+2]=w[i:i+3]
    a[0,0:3]=w[0:3]
    a[-1,-3:]=w[-3:]
    return a

def reverse(q,U,w):
    #�˴��޸��˲�������������������⣬��ע�⡣
    #��ֵ�㷴����Ƶ�
    #q��m+1(n-1)��������
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
    qderm=q[-1,:]-q[-2,:]#�˵���ʸ
    B=q[0]+dt(3)*qder0/3
    for i in range(1,n-2):
        A[i,i-1:i+2]=a(i+1),b(i+1),c(i+1)
        B=np.vstack([B,e(i+1)])
    qderm=q[m]-dt(n)*qderm/3
    B=np.vstack([B,qderm])
    
    A=np.dot(A,arrw(w))
    tmp=np.array([arrwN(ui,U,w) for ui in U[3:-3]])
    B=np.dot(B,tmp)
    solve=enlin.enlin(A,B)#���̵Ľ�
    solve=np.vstack([q[0,:],solve,q[-1,:]])
    return solve

if __name__=="__main__":
    import ProjData as dlib
    istart,istop,istep=(0.,10.,0.5)
    #===============================
    T=np.arange(istart,istop,istep)#ʱ����
    p=dlib.data(T)[0]#����
    #=============================
    qdn1=tangent_up.bessell(p,T)#��ʸ
    qdn2=tangent_up.bessell(qdn1,T)#��ʸ����ʸ
    cur=np.array([abs(invari.curvature(p1,p2))
                  for p1,p2 in zip(qdn1,qdn2)])#����Ȩ����
    #================================
    U=para.uniform(T)#�ڵ�ʸ��
    print reverse(p,U,cur)

    
