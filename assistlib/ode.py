#coding: cp936
#��΢�ַ���(ordinary differential equation)���֮�Ľ���ŷ����dy=f*dx
import numpy as np

def odeiem(f, y0, x): #for: f(x, y)
    '''f��΢�ַ��̣�y0�ǳ�ֵ��x�Ǹ��������У�ע��f(x,y)�����Ĳ���˳����x��y'''
    y = np.array([y0])
    for i in xrange(len(x)-1):
        h = x[i+1]-x[i]
        yp = y[i,:]+h*f(x[i],y[i])
        yc = y[i,:]+h/2*(f(x[i],y[i])+f(x[i+1],yp))
        y = np.vstack([y,yc])
    return y

def odeiems(f, y0, x): #for: f(x)
    '''f��΢�ַ��̣�y0�ǳ�ֵ��x�Ǹ��������У�ע��f(x)����Ψһ�Ĳ���x'''
    y=np.array([y0])
    for i in xrange(len(x)-1):
        h = x[i+1] - x[i]
        yc = y[i,:] + h/2 * (f(x[i]) + f(x[i+1]))
        y = np.vstack([y,yc])
    return y

if __name__=='__main__':
    f = lambda x, y: np.array([2*x, x, x**2]) #f(x, y)
    g = lambda x : np.array([2*x, x, x**2]) #f(x)
    print odeiem(f, [0, 0, 0], [0, 0.2, 0.4])
    print odeiems(g, [0, 0, 0], [0, 0.2, 0.4])
    
  
