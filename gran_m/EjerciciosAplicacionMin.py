#Importación de la libreria scipy
from scipy.optimize import  linprog
import math

#Declara la funcion objetivo
"""En este caso se declara como una lista con los coeficientes de la función
Si se trata de maximización: declarar la función objetivo con los coeficientes opuestos"""

objective_function = [3,1] # z = 2x1 + 3x

#restricciones

"""
Se declara el lado izquierdo de las restricciones
"""

left_side_restrictions = [
    [1,1],# 1x1 + 1x2 <= 1800 
    [0,-1],# x2 >= 1000
    [-2,-1], # 2x1 + x2 >= 2000
]

"""
Se declara el lado derecho o el elemento independiente de las restricciones
"""

right_side_restrictions = [1800,-1000,-2000]

"""
Se usa el modulo linprog que lo que hace es que toma como argumentos la funcion obejtivo, las restricciones y el lado derecho
de las restricciones para luego aplicar el metodo simplex, integrado en la libreria
"""

solution = linprog(objective_function,left_side_restrictions,right_side_restrictions, method = 'simplex')

print("Funcion Objetivo: z = 2x1 + 3x")
print("\nRestricciones:\n")
print(" 1x1 + 1x2 <= 1800 ")
print("x2 >= 1000")
print("2x1 + x2 >= 2000")
print("")

"""
Se imprimen los valores del que la funcion linprog calcula anteriormente, y se guardan en una variable solution, para luego mostrar
los valores, tanto de las variables, como el valor de maximizacion o minimizacion
"""

print("Valor de Optimizacion (Minimizar): "+str(int(math.fabs(solution.fun))))
print("")
print("Valor de las Variables")
print(solution.x)