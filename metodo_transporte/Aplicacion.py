from ortools.linear_solver import pywraplp

# Declarar el solucionador que abordará el modelo
solver = pywraplp.Solver.CreateSolver('GLOP')

# Data del modelo
costos = [
    [15, 30, 80, 50],
    [70, 90, 30, 40],
    [80, 40, 110, 90]
]

origen = ['1', '2', '3']
destino = ['Cali', 'Bogota','Medellin', 'Barranquilla']

num_destino = len(costos)
num_origen = len(costos[0])

# Variables del modelo
x = {}
for i in range(num_destino):
    for j in range(num_origen):
        x[i, j] = solver.IntVar(0, solver.infinity(), '')
        
#Restricciones de disponibilidad (oferta en DESTINO) 
solver.Add(solver.Sum([x[0, j] for j in range(num_origen)]) <= 15) 
solver.Add(solver.Sum([x[1, j] for j in range(num_origen)]) <= 35)
solver.Add(solver.Sum([x[2, j] for j in range(num_origen)]) <= 40)  

#Restricciones de demanda  
solver.Add(solver.Sum([x[i, 0] for i in range(num_destino)]) >= 35) 
solver.Add(solver.Sum([x[i, 1] for i in range(num_destino)]) >= 25)    
solver.Add(solver.Sum([x[i, 2] for i in range(num_destino)]) >= 10)     
solver.Add(solver.Sum([x[i, 2] for i in range(num_destino)]) >= 20) 

# Función objetivo con criterio de optimización: minimizar
objective_terms = []
for i in range(num_destino):
    for j in range(num_origen):
        objective_terms.append(costos[i][j] * x[i, j])

solver.Minimize(solver.Sum(objective_terms))

# Invoca el solucionador
status = solver.Solve()

# Configura los parámetros de impresión, las salidas del modelo
if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
    print('Costo total = ', solver.Objective().Value(), '\n')

    for i in range(num_destino):
        for j in range(num_origen):
            print('|{:^20} -> {:^20} | Cantidad: {:^20}|'.format(
            origen[i],
            destino[j],
            x[i, j].solution_value()))