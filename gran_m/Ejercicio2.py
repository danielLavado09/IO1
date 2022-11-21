#Importación de la libreria scipy
from scipy.optimize import  linprog
import math

#Declara la funcion objetivo
"""En este caso se declara como una lista con los coeficientes de la función
Si se trata de maximización: declarar la función objetivo con los coeficientes opuestos"""

objective_function = [6,5] # z = 6x1 + 5x2

#restricciones

"""
Se declara el lado izquierdo de las restricciones
"""

left_side_restrictions = [
    [3,1],# 3x1 + x2 = 3 
    [-4,-3],# 4x1 + 3x2 >= 6
    [1,2], # x1 + 2x2 <= 4
]

"""
Se declara el lado derecho o el elemento independiente de las restricciones
"""

right_side_restrictions = [3,-6,4]

"""
Se usa el modulo linprog que lo que hace es que toma como argumentos la funcion obejtivo, las restricciones y el lado derecho
de las restricciones para luego aplicar el metodo simplex, integrado en la libreria
"""

solution = linprog(objective_function,left_side_restrictions,right_side_restrictions, method = 'simplex')

print("")
print("Funcion Objetivo: z = 6x1 + 5x2")
print("\nRestricciones:\n")
print(" 3x1 + x2 = 3 ")
print(" 4x1 + 3x2 >= 6 ")
print(" x1 + 2x2 <= 4 ")
print("")

"""
Se imprimen los valores del que la funcion linprog calcula anteriormente, y se guardan en una variable solution, para luego mostrar
los valores, tanto de las variables, como el valor de maximizacion o minimizacion
"""

print("Valor de Optimizacion (Minimizar): "+str(int(math.fabs(solution.fun))))
print("")
print("Valor de las Variables")
print(solution.x)