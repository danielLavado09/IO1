import numpy as np 
import matplotlib.pyplot as plt
from numpy.lib.ufunclike import fix 

#Se define el rango de la grafica
x = np.arange(-10,50)

#Se define las funciones a trabajar
gx = (35-x)/2
tx = 35-(5/3)*x

#Se define las graficas de las funciones
plt.axhline(0, color="black")
plt.axvline(0, color="black")

#Se define los puntos de interseccion
plt.plot(15,10,'go',markersize=6,label = '(15,10)')
plt.plot(0,17.5,'ro',markersize=6)
plt.plot(21,0,'ro',markersize=6)
plt.plot(0,0,'ro',markersize=6)

y3 = np.minimum(gx,tx)

#Se muestra el area solucion
plt.fill_between(x,0,y3,color='c',alpha=0.75,label='Area Solucion') 

#Se muestra los puntos de interseccion
plt.plot()
plt.plot(x,gx,label='$y \leq (35-x)/2$')
plt.plot(x,tx,label='$y \leq 35-(5/3)x$')
plt.axis(ymin=0)
plt.axis(xmin=0)

#Se muestra la grafica y las leyendas de al funciones graficadas
plt.grid(True, which='both')
plt.legend()
plt.show()