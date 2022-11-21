import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol

#Se definen las funciones
def f1(x):
    return 3-2*x

def f2(x):
    return x

x = Symbol('x')

#Se definen los puntos de las graficas
plt.plot(1,1,'go',markersize = 5)
plt.plot(1.25,1/2,'go',markersize = 5)

#Se grafica el area solucion
plt.fill([1,1.25,2,2,1],[1,0.5,0.5,2,1],'y',alpha=0.75, label = 'Area solucion')

xr = np.linspace(0,2,100)

#Se rafica las funciones
y1r = f1(xr)
y2r = f2(xr)

#Se definen las leyendas de las funciones a mostrar en la grafica
plt.plot(xr,y1r, label = 'y > 3 - 2x')
plt.plot(xr,y2r, label = '$y \leq x$')
plt.vlines(0,ymin = -1, ymax = 3,color = 'black')
plt.hlines(0,xmin = 0, xmax = 2,color = 'black')
plt.hlines(0.5,xmin = 0, xmax = 2,color = 'green', label = 'y = 1/2')

#Se muestra la leyenda y la grafica final
plt.legend()
plt.show()