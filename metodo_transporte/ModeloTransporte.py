from ortools.linear_solver import pywraplp

# Declarar el solucionador que abordará el modelo
solver = pywraplp.Solver.CreateSolver('GLOP')

# Data del modelo
costos = [
    [10, 2, 20, 11],
    [12, 7, 9, 20],
    [4,  14, 16, 18],
]

granja = ['A', 'B', 'C']
almacen = ['1', '2','3','4']

num_almacen = len(costos)
num_granja = len(costos[0])

# Variables del modelo
x = {}
for i in range(num_almacen):
    for j in range(num_granja):
        x[i, j] = solver.IntVar(0, solver.infinity(), '')
        
#Restricciones de disponibilidad (oferta en ALMACEN) 
solver.Add(solver.Sum([x[0, j] for j in range(num_granja)]) <= 15) 
solver.Add(solver.Sum([x[1, j] for j in range(num_granja)]) <= 25) 
solver.Add(solver.Sum([x[2, j] for j in range(num_granja)]) <= 10) 

#Restricciones de demanda  
solver.Add(solver.Sum([x[i, 0] for i in range(num_almacen)]) >= 5) 
solver.Add(solver.Sum([x[i, 1] for i in range(num_almacen)]) >= 15)    
solver.Add(solver.Sum([x[i, 2] for i in range(num_almacen)]) >= 15) 
solver.Add(solver.Sum([x[i, 3] for i in range(num_almacen)]) >= 15)      

# Función objetivo con criterio de optimización: minimizar
objective_terms = []
for i in range(num_almacen):
    for j in range(num_granja):
        objective_terms.append(costos[i][j] * x[i, j])

solver.Minimize(solver.Sum(objective_terms))

# Invoca el solucionador
status = solver.Solve()

# Configura los parámetros de impresión, las salidas del modelo
if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
    print('Costo total = ', solver.Objective().Value(), '\n')

    for i in range(num_almacen):
        for j in range(num_granja):
            print('|{:^20} -> {:^20} | Cantidad: {:^20}|'.format(
            granja[i],
            almacen[j],
            x[i, j].solution_value()))