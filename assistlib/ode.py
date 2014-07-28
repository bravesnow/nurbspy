#coding: cp936
#�Ľ���ŷ����
#dy/dx=f(x,y)
import numpy as np

def f(x):
    return np.array([2*x,x,x**2])

def odeiem(f,y0,x):
    #f��΢�ַ��̣�y0�ǳ�ֵ��x�Ǹ���������
    #dy/dx=f(x,y)ע���Զ���f�����ģ�������x��y˳��
    y=np.array([y0])
    for i in xrange(len(x)-1):
        h=x[i+1]-x[i]
        yp=y[i,:]+h*f(x[i],y[i])
        yc=y[i,:]+h/2*(f(x[i],y[i])+f(x[i+1],yp))
        y=np.vstack([y,yc])
    return y

def odeiems(f,y0,x):
    #f��΢�ַ��̣�y0�ǳ�ֵ��x�Ǹ���������
    #dy/dx=f(x)ע���Զ���f�����ģ�������x��y˳��
    y=np.array([y0])
    for i in xrange(len(x)-1):
        h=x[i+1]-x[i]
        yc=y[i,:]+h/2*(f(x[i])+f(x[i+1]))
        y=np.vstack([y,yc])
    return y

if __name__=='__main__':
    print odeiems(f,[0,0,0],[0,0.2,0.4])
