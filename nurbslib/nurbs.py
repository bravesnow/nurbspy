# -*- coding: cp936 -*-
#输入：参数序列ux，控制点CtrlPoint，权重Weight，节点矢量U，曲线阶次k，导数阶r
#输出：给定参数序列的NURBS曲线的点/导数点
from __future__ import division
import numpy as np
import bspline

#=======================================================
def nbs(ux, CtrlPoint, Weight, U, k=3):
    '''参数列表,控制点,权因子,节点矢量,默认参数样条次数3'''
    #按权值扩展控制点的维度(高一维)
    wCtrlPoint = np.array([np.hstack([CtrlPoint[i,:]*Weight[i],Weight[i]])
                         for i in xrange(0, len(Weight))])
    wPoint = bspline.bspline(ux, wCtrlPoint, U, k) #获得高一维B样条曲线的点
    wPoint.shape = (-1, 3) #转换一下维度
    reduce_dim = lambda vec:vec[0:-1]/vec[-1] #函数：向量降一维
    Point = np.array([reduce_dim(vec) for vec in wPoint]) #对高一维B样条点降一维得到NURBS点
    return Point

def nbsder(ux,CtrlPoint,Weight,U,k=3,r=1):
    '''参数列表,控制点,权因子,节点矢量,默认参数样条次数3,默认曲线导数阶数1'''
    #按权值扩展控制点的维度(高一维)
    wCtrlPoint = np.array([np.hstack([CtrlPoint[i,:]*Weight[i],Weight[i]])
                         for i in xrange(0, len(Weight))])
    def der(u): #对单值参数u，求其导数点
        Aw=bspline.bspline(u, wCtrlPoint, U, k)#高维(A(u) w(u))
        Awr=bspline.deBoorDer(u, wCtrlPoint, U, k, r)#高维导数(A'(u) Weight'(u))
        Cu=Aw[0:-1]/Aw[-1] #降维获得NURBS点
        return (Awr[0:-1]-Awr[-1]*Cu)/Aw[-1]
    
    rPoint= np.array([der(u) for u in ux]) #对参数列表计算Nurbs导数
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



