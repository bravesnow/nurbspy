# -*- coding: cp936 -*-
# Thu Apr 17 09:34:28 2014
# bravesnowxue@NOSPAM.163.com
#曲线的几何不变量，活动框架等
#向量的运算，包括向量模，内积，外积，混合积
import numpy as np
from numpy import linalg as nlg

def norm(vec):
    #向量（一维数组）求模
    return nlg.norm(vec)
def dot(a,b):
    #向量内积，返回数值
    return np.dot(a,b)
    
def cross(a,b):
    #向量外积（差积）,注意二维三维及高维有些不同
    #注：所有的二维都扩展成了三维的
    if len(a)>3 or len(b)>3:
        print "ERROR:dimension"
        return
    if len(a)==2:
       a=np.hstack([a,0])
    if len(b)==2:
       b=np.hstack([b,0])        
    return np.cross(a,b)
'''=================================================='''
#活动标架
def alpha(p1):
    #单位切矢
    return p1/norm(p1)
    
def gamma(p1,p2):
    #副法矢
    ans=cross(p1,p2)
    return ans/norm(ans)
    
def beta(p1,p2):
    #主法矢
    return cross(gamma(p1,p2),alpha(p1))
'''=================================================='''
#几何不变量
def rcurvature(p1,p2):
    #相对曲率，对于二维平面曲线，有正负(ps: 没有差积运算)
    #p(u)=[x(u),y(u)],参数为p'(u),p''(u)
    molecular=np.linalg.det([p1,p2])#分子
    denominator=norm(p1)**3#分母
    kappa_r=molecular/denominator
    return kappa_r 
  
def acurvature(p1,p2):
    #绝对曲率，对于三维及其以上，只为正
    #参数p'(u),p''(u)
    molecular=norm(cross(p1,p2))
    denominator=norm(p1)**3
    kappa=molecular/denominator
    return kappa
    
def curvature(p1,p2):
    #平面或空间曲线的曲率
    if len(p1)!=len(p2):
        print "ERROR:dimmension"
        return
    if len(p1)==2:
        return rcurvature(p1,p2)
    if len(p1)==3:
        return acurvature(p1,p2)
        
def torsion(p1,p2,p3):
    #空间曲线的挠率
    #参数p',p'',p'''
    if len(p1)==len(p2)==len(p3)==3:
        #判断是不是三维的向量
        cs = cross(p1,p2)
        molecular=dot(cs,p3)
        denominator=norm(cs)**2
        tau=molecular/denominator
        return tau
    else:
        print "ERROR:dimmension"
        return
        
if __name__ == '__main__':
    p1=[1,2,3]
    p2=[3,4,2]
    p3=[1,4,2]
    print torsion(p1,p2,p3)
               
    
    


    



