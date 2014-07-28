# -*- coding: cp936 -*-
#关于各种误差分析函数
#参数准确值aVal，估计值eVal
#属于行向量组合矩阵
import numpy as np
from numpy import sqrt
def mse(aVal,eVal):
    #均方误差
    n,m=len(aVal),len(eVal)
    if n!=m:
        print "维数不匹配"
        return
    return sum((aVal-eVal)**2)/n

def rmse(aVal,eVal):
    #均方根误差(RMSE)
    return sqrt(mse(aVal,eVal))

def per(rmse,s):
    #s是对应系统的常数，一般取弧长
    #rmse是均方根误差，以narray为类型
    return ["%.4f"%one+"%" for one in rmse*100/s]

def sper(rmse,s,num):
    #Single point error rate
    #单点误差率，衡量了插值的能力，对于点的密集性的要求
    #转成百分比的形式，小数点后两位
    ret = ["%.2f"%one+"%" for one in rmse*num*100/s]
    return ret 
    
if __name__=='__main__':   
    a=np.array([[2,3],[1,5],[3,9]])
    b=np.array([[2.1,2.9],[1,5.1],[3.2,8.7]])
    print per(a,b,3)

    
