# -*- coding: cp936 -*-
#�˴�������20140428
#���ڸ��ַ��ž���ļ������⣬ʹ�÷������ź�����
#ʹ��sympy���Ű����������ߵĲ�����
#�������ݽṹ��Matrix�����
import sympy as sp
def norm(vec):
    #����ģ��������һά�����������к���
    return vec.norm()

def dot(vec1,vec2):
    #�������������������
    return vec1.dot(vec2)

def cross(vec1,vec2):
    #����������������ά����
    if len(vec1)==len(vec2)==3:
        return vec1.cross(vec2)
    else:
        print 'ERROR:dimmension'
        return
'''=================================================='''
#����
def alpha(p1):
    #��λ��ʸ
    return p1/norm(p1)
    
def gamma(p1,p2):
    #����ʸ
    ans=cross(p1,p2)
    return ans/norm(ans)
    
def beta(p1,p2):
    #����ʸ
    return cross(gamma(p1,p2),alpha(p1))
'''=================================================='''
#���β�����
def rcurvature(p1,p2):
    #������ʣ����ڶ�άƽ�����ߣ�������(ps: û�в������)
    #p(u)=[x(u),y(u)],����Ϊp'(u),p''(u)
    mat=sp.Matrix([p1,p2])
    molecular=mat.det()#����
    denominator=norm(p1)**3#��ĸ
    kappa_r=molecular/denominator
    return kappa_r 
  
def acurvature(p1,p2):
    #�������ʣ�������ά�������ϣ�ֻΪ��
    #����p'(u),p''(u)
    molecular=norm(cross(p1,p2))
    denominator=norm(p1)**3
    kappa=molecular/denominator
    return kappa
    
def curvature(p1,p2):
    #ƽ���ռ����ߵ�����
    if len(p1)!=len(p2):
        print "ERROR:dimmension"
        return
    if len(p1)==2:
        return rcurvature(p1,p2)
    if len(p1)==3:
        return acurvature(p1,p2)
        
def torsion(p1,p2,p3):
    #�ռ����ߵ�����
    #����p',p'',p'''
    if len(p1)==len(p2)==len(p3)==3:
        #�ж��ǲ�����ά������
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

               
        
    
