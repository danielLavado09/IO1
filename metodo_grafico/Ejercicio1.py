import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol

#Se define la inecuacion

def f1(x):
    return 5-(2*x)

#Se define la variable independiente

x = Symbol('x')

#Se define los puntos para graficar

x1, =  solve(f1(x))
x2 =  0
x3 =  0

y1 = f1(x1)
y2 = 0
y3 = f1(x3)

#Se marcan los puntos de interseccion
plt.plot(x1,y1,'go',markersize=10)
plt.plot(x2,y2,'go',markersize=10)
plt.plot(x3,y3,'go',markersize=10)

#Se realiza la gráfica del área solución

plt.fill([x1,x2,x3,x1],[y1,y2,y3,y1],'y',alpha=0.75, label = 'Area Solucion')

xr = np.linspace(-1,4,100)
y1r = f1(xr)

#Se muestra la grafica
plt.plot(xr,y1r, label = '$y \less 5 - 2x$')#Se grafica los puntos
plt.axhline(0, color="black")#Se da color a las lineas que conforman la grafica
plt.axvline(0, color="black")

plt.grid(True, which='both')
plt.legend()#Se muestra la leyenda de las funciones    
plt.show()#Se muestra la grafica
