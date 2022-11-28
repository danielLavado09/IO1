from numpy import inf
import networkx as nx
import pylab

############# Ejercicio 3.

#Acá se declaron los grafos.
grafo = {'A':{'B':2,'C':4,'D':3},'B':{'E':7,'F':4,'G':6},'C':{'E':3,'F':2,'G':4},'D':{'E':4,'F':1,'G':5},'E':{'H':1,'I':4},'F':{'H':6,'I':3},'G':{'H':3,'I':3},'H':{'J':3},'I':{'J':4},'J':{'J':0}}

#Acá se analiza cuál es el camino con coste minimo.
def calcularCosteMinimo(grafo,i,f):
    min_camino = {}
    anterior = {}
    nodos = grafo
    camino = []
    for nodo in nodos:
        min_camino[nodo] = inf
    min_camino[i] = 0
 
    # Se recorre el arreglo de los nodos.
    while nodos:
        nodoMin = None
        for nodo in nodos:
            if nodoMin is None:
                nodoMin = nodo
            elif min_camino[nodo] < min_camino[nodoMin]:
                nodoMin = nodo
 
        for nodoHijo, costo in grafo[nodoMin].items():
            if costo + min_camino[nodoMin] < min_camino[nodoHijo]:
                min_camino[nodoHijo] = costo + min_camino[nodoMin]
                anterior[nodoHijo] = nodoMin
        nodos.pop(nodoMin)
    # Se asigna el nodo actual.
    nodoActual = f
    while nodoActual != i:
        try:
            camino.insert(0,nodoActual)
            nodoActual = anterior[nodoActual]
        except KeyError:
            print('No existe un camino')
            break
    camino.insert(0,i)
    # Dependiendo si existe un camino, se pinta el resultado.
    if min_camino[f] != inf:
        print('Costo mínimo: ' + str(min_camino[f]))
        print('Camino: ' + str(camino))
  
calcularCosteMinimo(grafo, 'A', 'J')

# Se crea el objeto grafo.
grafo = nx.DiGraph()

# Se añaden los vertices del grafo.
grafo.add_edges_from([('D', 'F'),('E','H')], costo=1)
grafo.add_edges_from([('A', 'B'),('C','F')], costo=2)
grafo.add_edges_from([('A', 'D'),('C','E'),('F','I'),('G','I'),('G','H')], costo=3)
grafo.add_edges_from([('A', 'C'),('B','F'),('C','G'),('D','E'),('E','I'),('I','J')], costo=4)
grafo.add_edges_from([('D', 'G')], costo=5)
grafo.add_edges_from([('B', 'G'),('F','H')], costo=6)
grafo.add_edges_from([('B', 'E')], costo=7)

# Se grafica la solución
solucion = [('A','C'),('C','E'),('E','H'),('H','J')]

# Se asigna el color para la solución.
color_aristas = ['black' if not arista in solucion else 'red' for arista in grafo.edges()]

# Configuración del grafo.
valores = {
    'node_color': 'yellow',
    'node_size': 170,
    'width': 1,
    'arrowsize': 12
}

# Acá se pinta el grafo.
nx.draw_networkx(grafo, **valores,edge_color = color_aristas)
pylab.show()