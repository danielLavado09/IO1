import numpy as np 
import matplotlib.pyplot as plt  

#Se marcan los puntos de interseccion
plt.plot(-5,5,'go',markersize=10) 
plt.plot(5,5,'go',markersize=10) 
plt.plot(5,-10,'go',markersize=10) 
plt.plot(-5,-10,'go',markersize=10) 

#Se grafica del área solución   
plt.fill([-5,5,5,-5,-5],[5,5,-10,-10,5],'y',alpha=0.75, label = 'Area solucion')  

#Aca se muestra la grafica
plt.hlines(5,xmin = -5, xmax = 5,color = 'blue', label = '$y \leq 5$') # grafica los puntos
plt.axhline(0, color="black")#da color a las lineas que conforman la grafica
plt.axvline(0, color="black") 

plt.grid(True, which='both')
plt.legend()#Se muestra la leyenda de las funciones    
plt.show()#Se muestra la grafica