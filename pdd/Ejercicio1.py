from numpy import inf
import networkx as nx
import pylab

############# Ejercicio 1.

#Acá se declaron el grafo
grafo = {'1':{'2':8,'3':7,'4':9},'2':{'5':9,'6':10},'3':{'5':5,'6':7,'7':5,'8':8},'4':{'7':8,'8':14},'5':{'9':8,'10':6},'6':{'9':4,'10':3},'7':{'9':11,'10':8,'11':7},'8':{'10':12,'11':6},'9':{'12':14},'10':{'12':6},'11':{'12':15},'12':{'12':0}}

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
 
 
# Se calcula el coste minimo.
calcularCosteMinimo(grafo, '1', '12')

# Se crea el objeto grafo.
grafo = nx.DiGraph()

# Se añaden los vertices del grafo.
grafo.add_edges_from([('1', '2'),('5','9'),('3','8'),('4','7'),('7','10')], costo=8)
grafo.add_edges_from([('5','10'),('8','11'),('10','12')], costo=6)
grafo.add_edges_from([('2','5'),('1','4')], costo=9)
grafo.add_edges_from([('3','5'),('3','7')], costo=5)
grafo.add_edges_from([('1','3'),('3','6'),('7','11')], costo=7)
grafo.add_edges_from([('4','8'),('9','12')], costo=14)
grafo.add_edges_from([('2','6')], costo=10)
grafo.add_edges_from([('6','10')], costo=3)
grafo.add_edges_from([('6','9')], costo=4)
grafo.add_edges_from([('8','10')], costo=12)
grafo.add_edges_from([('11','12')], costo=15)

# Se grafica la solución.
solucion = [('1','3'),('3','6'),('6','10'),('10','12')]
 
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