import numpy as np 
import matplotlib.pyplot as plt
from numpy.lib.ufunclike import fix 

#Se define el tamaño de la grafica
x = np.arange(-8,8)

#Se definen las funciones 
gx = (12-2*x)/6
tx = (7-x)/4

#Se grafican las funciones
plt.axhline(0, color="black")
plt.axvline(0, color="black")

#Se grafican los puntos de interseccion
plt.plot(0,2,'go',markersize=8)
plt.plot(6,0,'ro',markersize=8, label = '(6,0) Punto de Maximizacion')
plt.plot(0,1.75,'go',markersize=8)
plt.plot(7,0,'go',markersize=8)


y3 = np.minimum(gx,tx)

#Se muestra el area solucion
plt.fill_between(x,0,y3,color='c',alpha=0.75,label='Area Solucion') 
plt.plot()

#Se muestra toda la grafica con las leyendas de cada funcion
plt.plot(x,gx,label='$y \leq (12-2x)/6$')
plt.plot(x,tx,label='$y \leq (7-x)/4$')
plt.axis(ymin=0)
plt.axis(xmin=0)
plt.grid(True, which='both')
plt.legend()
plt.show()