import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol

#Se define la inecuación
def f1(x):
    return 20-((2*x)/3)

#Se define la variable independiente
x = Symbol('x')

#Se definen los puntos interseccion
plt.plot(30,0,'go',markersize = 5)
plt.plot(0,20,'go',markersize = 5)

#Se muestra el area solucion
plt.fill([0,30,0,0],[0,0,20,0],'y',alpha=0.75, label = 'Area solucion')

xr = np.linspace(-5,35,100)
y1r = f1(xr)

#Se grafica las funciones
plt.plot(xr,y1r, label = '$y \leq 20-((2*x)/3)$')
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.hlines(y=0,xmin=0,xmax=70, color="orange", label = '$x \geq 0$')
plt.vlines(x=0,ymin=0,ymax=70, color="red", label = '$y \geq 0$')

#Se muestra la grafica y las leyendas de las funciones graficadas
plt.grid(True, which='both')
plt.legend()
plt.show()