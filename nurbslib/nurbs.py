# -*- coding: cp936 -*-
#���룺��������ux�����Ƶ�CtrlPoint��Ȩ��Weight���ڵ�ʸ��U�����߽״�k��������r
#����������������е�NURBS���ߵĵ�/������
from __future__ import division
import numpy as np
import bspline

#=======================================================
def nbs(ux, CtrlPoint, Weight, U, k=3):
    '''�����б�,���Ƶ�,Ȩ����,�ڵ�ʸ��,Ĭ�ϲ�����������3'''
    #��Ȩֵ��չ���Ƶ��ά��(��һά)
    wCtrlPoint = np.array([np.hstack([CtrlPoint[i,:]*Weight[i],Weight[i]])
                         for i in xrange(0, len(Weight))])
    wPoint = bspline.bspline(ux, wCtrlPoint, U, k) #��ø�һάB�������ߵĵ�
    wPoint.shape = (-1, 3) #ת��һ��ά��
    reduce_dim = lambda vec:vec[0:-1]/vec[-1] #������������һά
    Point = np.array([reduce_dim(vec) for vec in wPoint]) #�Ը�һάB�����㽵һά�õ�NURBS��
    return Point

def nbsder(ux,CtrlPoint,Weight,U,k=3,r=1):
    '''�����б�,���Ƶ�,Ȩ����,�ڵ�ʸ��,Ĭ�ϲ�����������3,Ĭ�����ߵ�������1'''
    #��Ȩֵ��չ���Ƶ��ά��(��һά)
    wCtrlPoint = np.array([np.hstack([CtrlPoint[i,:]*Weight[i],Weight[i]])
                         for i in xrange(0, len(Weight))])
    def der(u): #�Ե�ֵ����u�����䵼����
        Aw=bspline.bspline(u, wCtrlPoint, U, k)#��ά(A(u) w(u))
        Awr=bspline.deBoorDer(u, wCtrlPoint, U, k, r)#��ά����(A'(u) Weight'(u))
        Cu=Aw[0:-1]/Aw[-1] #��ά���NURBS��
        return (Awr[0:-1]-Awr[-1]*Cu)/Aw[-1]
    
    rPoint= np.array([der(u) for u in ux]) #�Բ����б����Nurbs����
    return rPoint

#===========================================================
if __name__ == '__main__':
    CtrlPoint=np.array([[-24,0],[-12,6],[1,8],[10,2],[12,0] ])
    Weight = np.array([1,1,0.8,1,1])
    U = np.array([ 0,0,0,0,0.75,1,1,1,1 ])
    u = 0.9; ux = [0.5,0.8]
    foo = lambda x: nbs(x, CtrlPoint, Weight, U)
    print foo(u)
    print foo(ux)



