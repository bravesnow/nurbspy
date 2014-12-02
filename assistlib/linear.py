# -*- coding: cp936 -*-
#线性方程组增强求解函数
from __future__ import division
import numpy as np
from scipy import linalg as lin

def solve(A, B):
    #A,B可以是矩阵数组类型,返回值是数组类型(解矩阵)
    #参数A是线性方程组的系数矩阵
    #参数B是方程组右端的常数项矩阵
    #Ax=B
    B = np.mat(B) #将B转成矩阵类型
    dim = B.shape #维度
    ncol = dim[1] #列数
    #按列求解线性方程组的解
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
