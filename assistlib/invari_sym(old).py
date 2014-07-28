# -*- coding: cp936 -*-
#此代码作罢20140428
#由于各种符号矩阵的计算问题，使得放弃符号函数法
#使用sympy符号包，计算曲线的不变量
#基本数据结构是Matrix类对象
import sympy as sp
def norm(vec):
    #向量模：参数是一维向量，包括行和列
    return vec.norm()

def dot(vec1,vec2):
    #点积：参数是两个向量
    return vec1.dot(vec2)

def cross(vec1,vec2):
    #向量积：参数是三维向量
    if len(vec1)==len(vec2)==3:
        return vec1.cross(vec2)
    else:
        print 'ERROR:dimmension'
        return
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
    mat=sp.Matrix([p1,p2])
    molecular=mat.det()#分子
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
        molecular=dot(cross(p1,p2),p3)
        denominator=norm(cross(p1,p2))**2
        tau=molecular/denominator
        return tau
    else:
        print "ERROR:dimmension"
        return
        
if __name__ == '__main__':
    t=sp.Symbol('t')
    p1=sp.Matrix([t,t**2,2*t])
    p2=sp.Matrix([[t**2,3*t,t**3]])
    p3=sp.Matrix([[sp.sqrt(t),2*t,t]])
    p4=sp.Matrix([[t**2,t]])
    p5=sp.Matrix([[3*t,t**3]])
    print torsion(p1,p2,p3)

               
        
    
