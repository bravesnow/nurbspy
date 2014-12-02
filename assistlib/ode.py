#coding: cp936
#常微分方程(ordinary differential equation)求解之改进的欧拉法dy=f*dx
import numpy as np

def odeiem(f, y0, x): #for: f(x, y)
    '''f是微分方程，y0是初值，x是给定的序列，注意f(x,y)函数的参数顺序是x与y'''
    y = np.array([y0])
    for i in xrange(len(x)-1):
        h = x[i+1]-x[i]
        yp = y[i,:]+h*f(x[i],y[i])
        yc = y[i,:]+h/2*(f(x[i],y[i])+f(x[i+1],yp))
        y = np.vstack([y,yc])
    return y

def odeiems(f, y0, x): #for: f(x)
    '''f是微分方程，y0是初值，x是给定的序列，注意f(x)带有唯一的参数x'''
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
    
  
