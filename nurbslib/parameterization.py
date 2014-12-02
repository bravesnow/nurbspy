# -*- coding: cp936 -*-
#���룺ʱ������Time-Series(T,Point)�ͽ״�order(k)
#������ڵ�ʸ��Knot-Vector(U) #ע���Ѿ�ȫ����һ����
from __future__ import division
import numpy as np
from math import sqrt

def uniform(T, k = 3):
    '''���Ȳ�����&&�Ⱦ������'''
    U = T - T[0] #ӳ�䵽0-End
    U = U / T[-1] #ӳ�䵽0-1
    U = np.hstack([np.zeros(k), T, np.ones(k)])
    return U

def accumul(Point, k = 3, argv = False):
    '''�淶�����ҳ���������'''
    if len(Point.shape) == 1: #һά��չ�ɶ�ά
        Point.shape = -1, 1 #��ֱ�Ӷ�T���ҳ��������ˣ�
    num = len(Point)
    chord_len = lambda i: sqrt(np.sum((Point[i,:]-Point[i-1,:])**2))
    U = [0] #initial U
    [U.append(chord_len(i)+U[i-1]) for i in xrange(1, num)]
    U = np.array(U)
    SumU = U[-1] # sum of chord length
    U = U/SumU # normalization
    U = np.hstack([np.zeros(k), U ,np.ones(k)])
    if argv: return U, SumU
    else: return U

def centrip(Point,k=3,argv=False):
    '''���Ĳ�����'''
    if len(Point.shape) == 1: #һά��չ�ɶ�ά
        Point.shape = -1, 1 #��ֱ�Ӷ�T���ҳ��������ˣ�
    num = len(Point)
    chord_len = lambda i: sqrt(sqrt(np.sum((Point[i,:]-Point[i-1,:])**2)))
    U = [0] #initial U
    [U.append(chord_len(i)+U[i-1]) for i in xrange(1, num)]
    U = np.array(U)
    SumU = U[-1] # sum of chord length
    U = U/SumU # normalization
    U = np.hstack([np.zeros(k), U ,np.ones(k)])
    if argv: return U, SumU
    else: return U

if __name__=="__main__":
    Point = np.array([[1,2], [3,4], [1,2]])
    print accumul(Point)
    print centrip(Point)
