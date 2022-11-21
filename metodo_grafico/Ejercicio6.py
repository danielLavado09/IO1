import numpy as np
import matplotlib.pyplot as plt

#Se define el rango para mostrar la grafica
x = np.linspace(0,100,100)

#Se definen las inecuaciones
y1 = 180-2*x
y2 = 80-(x/2)
y3 = 100-x

#Se muestran las rectas y puntos interseccion
plt.plot(40, 60, 'go', markersize = 5)
plt.plot(80, 20, 'go', markersize = 5)
plt.plot(90, 0, 'go', markersize = 5)
plt.plot(0, 80, 'go', markersize = 5)
plt.plot(66.6, 46.6, 'go', markersize = 5)
plt.plot(x, y1, label = '$2x + y \leq 180$', color = 'c')
plt.plot(x, y2, label = '$x + 2y \leq 160$', color = 'r')
plt.plot(x, y3, label = '$x + y \leq 100$', color = 'b')

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.plot(40, 60, color = 'r')

y4 = np.minimum(y2,y3)

#Se grafica area solucion
plt.fill_between(x, y4, color = 'y', label = 'Area solucion' )

#Se muestra la grafica y la leyenda de las funciones graficadas
plt.grid(True, which='both')
plt.legend()
plt.show()

