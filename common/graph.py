import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import cm

def graph2D(function, min_x, max_x):
    x = np.arange(min_x, max_x, 0.1)
    y = function(x)
    
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x, y)
    plt.show()
    

def graph_mesh3D(function):
    x = np.linspace(-6, 6, 30)
    y = np.linspace(-6, 6, 30)
    
    X, Y = np.meshgrid(x, y)
    Z = function(X, Y)
    
    ax = plt.axes(projection='3d')
    ax.contour3D(X, Y, X, 50, cmap=cm.coolwarm)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')