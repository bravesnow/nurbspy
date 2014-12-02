# -*- coding: cp936 -*-
#输入：时间序列Time-Series(T,Point)和阶次order(k)
#输出：节点矢量Knot-Vector(U) #注：已经全部归一化了
from __future__ import division
import numpy as np
from math import sqrt

def uniform(T, k = 3):
    '''均匀参数化&&等距参数化'''
    U = T - T[0] #映射到0-End
    U = U / T[-1] #映射到0-1
    U = np.hstack([np.zeros(k), T, np.ones(k)])
    return U

def accumul(Point, k = 3, argv = False):
    '''规范积累弦长参数化法'''
    if len(Point.shape) == 1: #一维扩展成二维
        Point.shape = -1, 1 #可直接对T求弦长参数化了！
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
    '''向心参数化'''
    if len(Point.shape) == 1: #一维扩展成二维
        Point.shape = -1, 1 #可直接对T求弦长参数化了！
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
