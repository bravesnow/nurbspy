# -*- coding: cp936 -*-
#��ϵͳ�Ļ���
import numpy as np
import para
import LorenzData as dlib
def arclen(istart=0,istop=10.,istep=0.001):
    #�ҳ����满��sumuԼ����arclen
    T=np.arange(istart,istop,istep)#ʱ����
    p=dlib.data(T)[0]
    U,sumu=para.accumul(p,3,True)
    return sumu
if __name__=='__main__':
    print arclen()
