# -*- coding: cp936 -*-
#���Է�������ǿ��⺯��
from __future__ import division
import numpy as np
from scipy import linalg as lin
def enlin(A,B):
    #A,B�����Ǿ�����������,����ֵ����������
    #����A�����Է������ϵ������
    #����B�Ƿ������Ҷ˵ĳ��������
    #Ax=B
    B=np.mat(B)#��Bת�ɾ�������
    dim=B.shape#ά��
    ncol=dim[1]#����
    x=[]#���б�
    for j in xrange(ncol):
        x.append(lin.solve(A,B[:,j]))
    return np.hstack(x)

if __name__=="__main__":
    a=np.array([[1,-2,3],[3,-2,1],[1,1,-1]])
    b=np.array([[2,2],[7,7],[1,1]])
    print enlin(a,b)
