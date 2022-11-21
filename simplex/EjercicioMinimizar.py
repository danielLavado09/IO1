#Importación de la libreria scipy
from scipy.optimize import  linprog
import math

#Declara la funcion objetivo

objective_function = [10,30] # P = 10x + 30y


#restricciones

"""
Si la función es de maximizacion y alguna restriccion es >= (mayor o igual que)
tambien se deben invertir el signo de los coeficientes
"""

"""
Se declara el lado izquierdo de las restricciones
"""

left_side_restrictions = [
    [-1,-5],# x + 5y
    [-5,-1],# 5x + y
]

"""
Se declara el lado derecho o el elemento independiente de las restricciones
"""

right_side_restrictions = [-15,-15]

"""
Se usa el modulo linprog que lo que hace es que toma como argumentos la funcion obejtivo, las restricciones y el lado derecho
de las restricciones para luego aplicar el metodo simplex, integrado en la libreria
"""

solution = linprog(objective_function,left_side_restrictions,right_side_restrictions, method = 'simplex')

print("------"+"Metodo Simplex"+"------")
print("Funcion Objetivo: p = 10x + 30y")
print("\nRestricciones:\n")
print("x + 5y >= 15")
print("5x + y >= 15")
print("")

"""
Se imprimen los valores del que la funcion linprog calcula anteriormente, y se guardan en una variable solution, para luego mostrar
los valores, tanto de las variables, como el valor de maximizacion o minimizacion
"""

print("Valor de Optimizacion (Mnimizar): "+str(int(math.fabs(solution.fun))))
print("")
print("Valor de las Variables")
print(solution.x)