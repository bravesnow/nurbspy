#coding:cp936
def plot(a,b,c1='b',c2='g'):
    #图形化显示，函数封装
    #同时显示二维矩阵的a与b，以是比较
    import matplotlib.pyplot as plt
    plt.plot(a[:,0],a[:,1],c1)
    plt.plot(b[:,0],b[:,1],c2)
    plt.show()

def plot3d(a,b,c1='b',c2='g'):
    #同时显示三维矩阵的a与b，以是比较
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    #ax=Axes3D(plt.figure())
    #ax=plt.figure().add_subplot(111, projection='3d')
    ax = plt.subplot(111, projection='3d')
    ax.plot(a[:,0],a[:,1],a[:,2],c1)#可以加各种参数
    ax.plot(b[:,0],b[:,1],b[:,2],c2)
    plt.show()

if __name__=='__main__':
    import numpy as np
    a=np.array([[2,1,2],[4,5,1],[1,7,2]])
    b=np.array([[2,8,7],[5,6,4],[3,5,1]])
    plot3d(a,b)
