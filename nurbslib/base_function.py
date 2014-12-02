# -*- coding: cp936 -*-
#B������������deBoor�㷨�������˺�������˴˺������Ը����ˣ�
from __future__ import division
import numpy as np

def N(u, i, k, U): #B��������������
    '''�ڵ����i���״�order(k)���ڵ�ʸ��knot-vector(U)'''
    if k==0:
        if U[i]<= u <U[i+1]: return 1
        else: return 0
    else:
        if U[i+k] == U[i]: a=0
        else:
            a = (u-U[i])/(U[i+k] - U[i])
        if U[i+k+1] == U[i+1]: b=0
        else:
            b=(U[i+k+1]-u)/(U[i+k+1] - U[i+1])
        return a*N(u, i, k-1, U) + b*N(u, i+1, k-1, U)

if __name__ == '__main__':
    pass
