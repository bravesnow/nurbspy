# -*- coding: cp936 -*-
# ���룺����ֵ����ux���ڵ�ʸ��U�����Ƶ�����CtrlPoint���״�k��������r
# ���룺����������B���������ϵ�/������
from __future__ import division
import numpy as np

#=================================================
def bspline(ux,CtrlPoint,U,k=3):
    '''B������ֵ���б��������ux��������һ����ֵ��Ҳ�����Ƕ�ֵ����
    ���Ƶ�CtrlPoint(������)���ڵ�ʸ��U����������kȱʡΪ3'''
    if isinstance(ux,int) or isinstance(ux,float): #��ֵ�ж�
        return deBoor(ux,CtrlPoint,U,k)
    else:
        rval=[deBoor(u,CtrlPoint,U,k) for u in ux]
        return np.array(rval)

def bsplineDer(ux,CtrlPoint,U,k=3,r=1):
    '''B����������������Ҫ�ǲ����б�B������֮r�׵��������Դ���ֵ�����б�
    ���Ƶ�CtrlPoint(������)���ڵ�ʸ��U����������k����������Ϊr������u����ux'''
    if isinstance(ux,int) or isinstance(ux,float): #��ֵ�ж�
        return deBoorDer(ux,CtrlPoint,U,k,r)
    else:#�б��Ƶ�ʽ
        rval = [deBoorDer(u,CtrlPoint,U,k,r) for u in ux]
        return np.array(rval)

#================================================
def deBoor(u,CtrlPoint,U,k=3):
    ''' �²����㷨����ֵu��B�������ߵĵ�ֵ'''
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
    gen=(i for i in xrange(k,len(U)) if U[i]<=u<=U[i+1])#����������
    #�˴����u����1����ô����������쳣�أ���Ҫ��ϸ��ӡ�
    i=gen.next()#ȡ�������ĵ�һ��ֵ
    return d(k,i-k)

def deBoorDer(u,CtrlPoint,U,k=3,r=1):
    '''�²����㷨(les-P68)����ֵu��B�������ߵĵ���'''
    if u>1:
        print(u,"ERROR:u>1")
        exit(1)
    n=len(CtrlPoint)-1
    rU=U[1:-1]
    rCtrlPoint=[k*(CtrlPoint[i+1,:]-CtrlPoint[i,:])/(U[i+k+1]-U[i+1]) for i in range(0,n)]
    gen=(i for i in xrange(k,n+2) if U[i]<=u<=U[i+1])#����������
    i=gen.next()#ȡ��������һ��ֵ
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
