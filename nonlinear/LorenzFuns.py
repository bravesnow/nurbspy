# coding: cp936
# Lorenz的方程(done)
import sympy as smp
x,y,z=smp.symbols('x,y,z')
p,r,b=smp.symbols('a,r,b')
def gen_expressions():    
    f1=x1,y1,z1=-p*(x-y),x*(r-z)-y,x*y-b*z
    f2=x2,y2,z2=-p*(x1-y1),x1*(r-z)-x*z1,x1*y+x*y1-b*z1
    f3=x3,y3,z3=-p*(x2-y2),x2*(r-z)-2*x1*z1-x*z2,2*x1*y1+x2*y+x*y2-b*z2
    return f1,f2,f3
def fder(points,nder,args=[10.,28.,3.]):
    #参数points是曲线的点
    #nder是曲线的导数阶数参数
    if nder>3:
        print "Error"
        return
    else:
        vp,vr,vb=args#取得常数
        fsym=gen_expressions()[nder-1]#得到sympy表达式列表
        fsym=[f.subs([(p,vp),(r,vr),(b,vb)]) for f in fsym]#替换a,b,c
        foo=[smp.lambdify([x,y,z],f) for f in fsym]#sympy表达式转成python函数
        fr=lambda x,y,z:[f(x,y,z) for f in foo]
        return [fr(vx,vy,vz) for [vx,vy,vz] in points]
    
if __name__ == '__main__':
    import numpy as np
    pt=[[1,2,3],[2,5,1]]
    print fder(pt,3)

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
    
