# -*- coding: cp936 -*-
#���ڸ�������������
#����׼ȷֵaVal������ֵeVal
#������������Ͼ���
import numpy as np
from numpy import sqrt
def mse(aVal,eVal):
    #�������
    n,m=len(aVal),len(eVal)
    if n!=m:
        print "ά����ƥ��"
        return
    return sum((aVal-eVal)**2)/n

def rmse(aVal,eVal):
    #���������(RMSE)
    return sqrt(mse(aVal,eVal))

def per(rmse,s):
    #s�Ƕ�Ӧϵͳ�ĳ�����һ��ȡ����
    #rmse�Ǿ���������narrayΪ����
    return ["%.4f"%one+"%" for one in rmse*100/s]

def sper(rmse,s,num):
    #Single point error rate
    #��������ʣ������˲�ֵ�����������ڵ���ܼ��Ե�Ҫ��
    #ת�ɰٷֱȵ���ʽ��С�������λ
    ret = ["%.2f"%one+"%" for one in rmse*num*100/s]
    return ret 
    
if __name__=='__main__':   
    a=np.array([[2,3],[1,5],[3,9]])
    b=np.array([[2.1,2.9],[1,5.1],[3.2,8.7]])
    print per(a,b,3)

    
