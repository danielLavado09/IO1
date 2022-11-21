#Importación de la libreria scipy
from scipy.optimize import  linprog
import math

#Declara la funcion objetivo
"""En este caso se declara como una lista con los coeficientes de la función
Si se trata de maximización: declarar la función objetivo con los coeficientes opuestos"""

objective_function = [-3,-5] # P = 3x1 + 5x2

#restricciones

"""
Se declara el lado izquierdo de las restricciones
"""

left_side_restrictions = [
    [2,6],# 2x1 + 6x2 
    [1,4],# x1 + 4x3
]

"""
Se declara el lado derecho o el elemento independiente de las restricciones
"""

right_side_restrictions = [12,7]

"""
Se usa el modulo linprog que lo que hace es que toma como argumentos la funcion obejtivo, las restricciones y el lado derecho
de las restricciones para luego aplicar el metodo simplex, integrado en la libreria
"""

solution = linprog(objective_function,left_side_restrictions,right_side_restrictions, method = 'simplex')

print("------"+"Metodo Simplex"+"------")
print("Funcion Objetivo: p = 3x1 + 5x2")
print("\nRestricciones:\n")
print("2x1 + 6x2 <= 12")
print("x1 + 4x2 <= 7")
print("")

"""
Se imprimen los valores del que la funcion linprog calcula anteriormente, y se guardan en una variable solution, para luego mostrar
los valores, tanto de las variables, como el valor de maximizacion o minimizacion
"""

print("Valor de Optimizacion (Maximizar): "+str(int(math.fabs(solution.fun))))
print("")
print("Valor de las Variables")
print(solution.x)