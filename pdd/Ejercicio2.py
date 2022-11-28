from numpy import inf
import networkx as nx
import pylab

############# Ejercicio 2.

#Acá se declaron los grafos.
grafo = {'A':{'B':3,'C':4,'D':5},'B':{'E':7,'F':5},'C':{'E':2,'F':5,'G':7},'D':{'F':8,'G':6},'E':{'H':1},'F':{'H':5},'G':{'H':4},'H':{'H':0}}

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
  
calcularCosteMinimo(grafo, 'A', 'H')

# Se crea el objeto grafo.
grafo = nx.DiGraph()

# Se añaden los vertices del grafo.
grafo.add_edges_from([('E','H')], costo=1)
grafo.add_edges_from([('C','E')], costo=2)
grafo.add_edges_from([('A','B')], costo=3)
grafo.add_edges_from([('A','C'),('G','H')], costo=4)
grafo.add_edges_from([('A','D'),('B','F'),('C','F'),('F','H')], costo=5)
grafo.add_edges_from([('D','G')], costo=6)
grafo.add_edges_from([('C','G'),('B','E')], costo=7)

# Se grafica la solución.
solucion = [('A','C'),('C','E'),('E','H')]
 
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