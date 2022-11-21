#Importación de la libreria scipy
from scipy.optimize import  linprog
import math

#Declara la funcion objetivo
"""En este caso se declara como una lista con los coeficientes de la función
Si se trata de maximización: declarar la función objetivo con los coeficientes opuestos"""

objective_function = [-40000,-60000] # z = 40000x1 + 60000x2

#restricciones

"""
Se declara el lado izquierdo de las restricciones
"""

left_side_restrictions = [
    [1,0],# 1x1 <= 4000 
    [0,1],# x2 <= 3000
    [-1,-1], # x1 + x2 >= 600
]

"""
Se declara el lado derecho o el elemento independiente de las restricciones
"""

right_side_restrictions = [4000,3000,-600]

"""
Se usa el modulo linprog que lo que hace es que toma como argumentos la funcion obejtivo, las restricciones y el lado derecho
de las restricciones para luego aplicar el metodo simplex, integrado en la libreria
"""

solution = linprog(objective_function,left_side_restrictions,right_side_restrictions, method = 'simplex')

print("Funcion Objetivo: z = 40000x1 + 60000x2")
print("\nRestricciones:\n")
print("1x1 <= 4000")
print("x2 <= 3000")
print("x1 + x2 >= 600")
print("")

"""
Se imprimen los valores del que la funcion linprog calcula anteriormente, y se guardan en una variable solution, para luego mostrar
los valores, tanto de las variables, como el valor de maximizacion o minimizacion
"""

print("Valor de Optimizacion (Maximizar): "+str(int(math.fabs(solution.fun))))
print("")
print("Valor de las Variables")
print(solution.x)