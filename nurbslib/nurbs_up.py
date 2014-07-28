# -*- coding: cp936 -*-
#�����
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import reverse
def N(i,k,u,U):
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
        return a*N(i,k-1,u,U)+b*N(i+1,k-1,u,U)
#=======================================================
'''Nurbs���뵼��'''
def nbs(eu,dP,w,U,k=3):
    '''���Ƶ�,�ڵ�ʸ��,Ȩ����,�����б�,Ĭ�ϲ�����������'''
    '''�˺�����Ҫ��nurbs_high.py���µ��޸�'''
    #��չ�ɸ�һά�Ŀ��Ƶ�
    dPw=np.array([np.hstack([dP[i,:]*w[i],w[i]]) for i in xrange(0,len(w))])
    #dPw=reverse.reverse(dPw,U)
    Cw=bs(eu,dPw,U,k)#�Ը�һά�Ŀ��Ƶ�õ�B��������
    Cw.shape=(-1,3)#ת��һ��ά��
    f=lambda vec:vec[0:-1]/vec[-1]#����������������һά
    C=[f(vec) for vec in Cw]#�����õ�B�����㽵һά�õ�Nurbs��
    return np.array(C)
def nbsder(eu,dP,w,U,k=3,r=1):
    '''���Ƶ�,�ڵ�ʸ��,Ȩ����,�����б�,�����Ĵ�������������'''
    #��չ�ɸ�һά�Ŀ��Ƶ�
    dPw=np.array([np.hstack([dP[i,:]*w[i],w[i]]) for i in xrange(0,len(w))])
    def der(u):
        #�Ե�ֵ����u�����䵼����
        Aw=bspmak(u,dPw,U,k)#��һάNurbs(A(u) w(u))
        Awr=deBoorder(u,dPw,U,k,r)#��һάNurbs����(A'(u) w'(u))
        Cu=Aw[0:-1]/Aw[-1]#��һά��Nurbs��
        return (Awr[0:-1]-Awr[-1]*Cu)/Aw[-1]
    rder=[der(u) for u in eu]#�Բ����б����Nurbs����
    return np.array(rder)
#=========================================================
'''B�����㣬���Դ���ֵ���б�'''
def bs(eu,dP,U,k=3):
    '''B�������߹���
    ���Ƶ�dP(������)���ڵ�ʸ��U����������k
    ����u����eu'''
    if isinstance(eu,int) or isinstance(eu,float):
        #�ж��ǵ�ֵ��ֱ����
        return deBoor(eu,dP,U,k)
    else:
        #�б��Ƶ�ʽ
        rval=[deBoor(u,dP,U,k) for u in eu]
        return np.array(rval)
'''B������֮r�׵��������Դ���ֵ�����б�'''
def bsder(eu,dP,U,k=3,r=1):
    '''B����������������Ҫ�ǲ����б�
���Ƶ�dP(������)���ڵ�ʸ��U����������k������Ϊr������u����eu'''
    if isinstance(eu,int) or isinstance(eu,float):
        #�жϵ�ֵ
        return deBoorder(eu,dP,U,k,r)
    else:
        #�б��Ƶ�ʽ
        rval=[deBoorder(u,dP,U,k,r) for u in eu]
        return np.array(rval)
#===========================================================
'''B�����ĵ²����㷨'''
def deBoor(u,dP,U,k=3):
    '''�Ե�ֵu���B�������ߵĵ�ֵ,ʵ�ֵ��㷨�ǵ²����㷨'''
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
    gen=(i for i in xrange(k,len(U)) if U[i]<=u<=U[i+1])#����������
    #�˴����u����1����ô����������쳣�أ���Ҫ��ϸ��ӡ�
    i=gen.next()#ȡ�������ĵ�һ��ֵ
    return d(k,i-k)

def deBoorder(u,dP,U,k=3,r=1):
    '''��ֵu��B�������ߵĵ�����ʹ�õ��ǵ²����㷨lesP68'''
    if u>1:
        print u,"Error: u>1"
        return
    n=len(dP)-1
    Ur=U[1:-1]
    dPr=[k*(dP[i+1,:]-dP[i,:])/(U[i+k+1]-U[i+1]) for i in range(0,n)]
    gen=(i for i in xrange(k,n+2) if U[i]<=u<=U[i+1])#����������
    i=gen.next()#ȡ��������һ��ֵ
    dPr=np.array(dPr)
    if r==1:
        return deBoor(u,dPr,Ur,k-1)
    else:
        return deBoorder(u,dPr,Ur,k-1,r-1)
#===========================================================
#����������
if __name__ == '__main__':
    #���Ƶ����
    dP=np.array([[-24,0],[-12,6],[1,8],[10,2],[12,0] ])
    w=np.array([1,1,0.8,1,1])
    #�ڵ�ʸ��
    U=np.array([ 0,0,0,0,0.75,1,1,1,1 ])
    #����
    k=3;u=[0.5,0.8]
    h = lambda u: nbs(u,dP,w,U)
    print h(0.9)



