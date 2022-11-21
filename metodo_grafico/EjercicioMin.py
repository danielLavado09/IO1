import numpy as np 
import matplotlib.pyplot as plt
from numpy.lib.ufunclike import fix 

#Se define rango de la grafica
x = np.arange(-8,16)

#Se definen las funciones
gx = (15-x)/5
tx = (15-5*x)

#Se definen las graficas de las funciones
plt.axhline(0, color="black")
plt.axvline(0, color="black")

#Se definen los puntos de interseccion
plt.plot(0,3,'go',markersize=8)
plt.plot(15,0,'go',markersize=8)
plt.plot(2.5,2.5,'ro',markersize=8, label = '(5/2,5/2) Punto de Minimizacion')
plt.plot(0,15,'go',markersize=8)
plt.plot(3,0,'go',markersize=8)

y3 = np.minimum(gx,tx)

#Se muestra el area solucion
plt.fill([15,0,2.5,15,0,0],[0,15,2.5,0,60,15],color='c',alpha=0.75,label='Area Solucion') 

#Se define y se muestra los puntos de interseccion y las funciones
plt.plot()
plt.plot(x,gx,label='$y \geq (15-x)/5$')
plt.plot(x,tx,label='$y \geq 15-5x$')
plt.axis(ymin=0)
plt.axis(xmin=0)

#Se muestra la grafica y las leyendas de la funciones
plt.grid(True, which='both')
plt.legend()
plt.show()