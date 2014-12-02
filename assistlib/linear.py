# -*- coding: cp936 -*-
#���Է�������ǿ��⺯��
from __future__ import division
import numpy as np
from scipy import linalg as lin

def solve(A, B):
    #A,B�����Ǿ�����������,����ֵ����������(�����)
    #����A�����Է������ϵ������
    #����B�Ƿ������Ҷ˵ĳ��������
    #Ax=B
    B = np.mat(B) #��Bת�ɾ�������
    dim = B.shape #ά��
    ncol = dim[1] #����
    #����������Է�����Ľ�
    solution = [lin.solve(A, B[:,col]) for col in xrange(ncol)]
    return np.hstack(solution)

if __name__ == "__main__":
    #Ax = B
    A = np.array([[1,-2,3],
                  [3,-2,1],
                  [1,1,-1]])
    B = np.array([[2,2],
                  [7,7],
                  [1,1]])
    print solve(A,B)
