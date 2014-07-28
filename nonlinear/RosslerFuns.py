# coding: cp936
import sympy as smp
x,y,z=smp.symbols('x,y,z')
a,b,c=smp.symbols('a,b,c')
def gen_expressions():    
    f1=x1,y1,z1=-y-z,x+a*y,b+z*(x-c)
    f2=x2,y2,z2=-y1-z1,x1+a*y1,z1*(x-c)+z*x1
    f3=x3,y3,z3=-y2-z2,x2+a*y2,z2*(x-c)+2*x1*z1+z*x2
    return f1,f2,f3
def fder(points,nder,args=[0.15,0.2,14.]):
    #参数points是曲线的点
    #nder是曲线的导数阶数参数
    if nder>3:
        print "Error"
        return
    else:
        va,vb,vc=args#取得常数
        fsym=gen_expressions()[nder-1]#得到sympy表达式列表
        fsym=[f.subs([(a,va),(b,vb),(c,vc)]) for f in fsym]#替换a,b,c
        foo=[smp.lambdify([x,y,z],f) for f in fsym]#sympy表达式转成python函数
        fr=lambda x,y,z:[f(x,y,z) for f in foo]
        return [fr(vx,vy,vz) for [vx,vy,vz] in points]
        
def f1der(points,args=[0.15,0.2,14.]):
    #见fder
    a,b,c=args
    f=lambda x,y,z:[-y-z,x+a*y,b+z*(x-c)]
    return [f(x,y,z) for x,y,z in points]

def f2der(points,args=[0.15,0.2,14.]):
    #见fder
    a,b,c=args
    f1=lambda x,y,z:-x-a*y-b-z*(x-c)
    f2=lambda x,y,z:-y-z+a*x+a**2*y
    f3=lambda x,y,z:-z*(y+z)+b*(x-c)+z*(x-c)**2
    f=lambda x,y,z:[f1(x,y,z),f2(x,y,z),f3(x,y,z)]
    return [f(x,y,z) for x,y,z in points]
    
if __name__ == '__main__':
    import numpy as np
    p=[[1,2,3],[2,5,1]]
    print fder(p,3)

'''    import RosslerData as rd
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    T=np.arange(0,100,0.01)
    points = rd.data(T)[0]
    track = np.array(f1der(points))
    ax=plt.subplot(111,projection='3d')
    ax.plot(track[:,0], track[:,1], track[:,2])
    plt.show()
    '''
    
