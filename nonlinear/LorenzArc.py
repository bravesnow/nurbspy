# -*- coding: cp936 -*-
#求系统的弧长
import numpy as np
import para
import LorenzData as dlib
def arclen(istart=0,istop=10.,istep=0.001):
    #弦长代替弧长sumu约等于arclen
    T=np.arange(istart,istop,istep)#时间列
    p=dlib.data(T)[0]
    U,sumu=para.accumul(p,3,True)
    return sumu
if __name__=='__main__':
    print arclen()
