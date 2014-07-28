# -*- coding: cp936 -*-
# Thu Apr 17 09:34:28 2014
# bravesnowxue@NOSPAM.163.com
#���ߵļ��β����������ܵ�
#���������㣬��������ģ���ڻ����������ϻ�
import numpy as np
from numpy import linalg as nlg

def norm(vec):
    #������һά���飩��ģ
    return nlg.norm(vec)
def dot(a,b):
    #�����ڻ���������ֵ
    return np.dot(a,b)
    
def cross(a,b):
    #��������������,ע���ά��ά����ά��Щ��ͬ
    #ע�����еĶ�ά����չ������ά��
    if len(a)>3 or len(b)>3:
        print "ERROR:dimension"
        return
    if len(a)==2:
       a=np.hstack([a,0])
    if len(b)==2:
       b=np.hstack([b,0])        
    return np.cross(a,b)
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
    molecular=np.linalg.det([p1,p2])#����
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
               
    
    


    



