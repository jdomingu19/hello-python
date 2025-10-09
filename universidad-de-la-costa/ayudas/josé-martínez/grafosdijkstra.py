# Clase grafos con pesos + Dijkstra
import heapq

class Vertices:
    def __init__(self, valor) -> None:
        self.valor = valor


class Grafos:
    def __init__(self, dirigido = False) -> None:
        self.grafo = {}
        self.dirigido = dirigido

    def agregarVertice(self, vertice: Vertices):
        self.grafo.update({vertice.valor: []})

    def agregarArista(self, vertice1, vertice2, peso = 1):
        self.relacionarArista(vertice1, vertice2, peso)

    def relacionarArista(self, origen: Vertices, destino: Vertices, peso):
        self.grafo[origen.valor].append([destino.valor, peso])
        if self.dirigido == False:
            self.grafo[destino.valor].append([origen.valor, peso])
        
    def recorrerProfundidad(self, inicio):
        visitados = set()
        x = self.__dfsComplemento(inicio, visitados, [])
        cont = 0
        cadena = ""
        for vertice in x:
            if cont == len(x) - 1:
                cadena = cadena + f"{vertice}"
            else:
                cadena = cadena + f"{vertice} -> "
            cont = cont + 1
        return cadena
  
    def __dfsComplemento(self, nodo, visitados: set, y:list):
        visitados.add(nodo)
        y.append(nodo)
        for vecino in self.grafo[nodo]:
            if vecino[0] not in visitados:
                self.__dfsComplemento(vecino[0], visitados, y)
        return y

    def caminoMenosPesado(self, inicio, final):
        distancias = {vertice: float('inf') for vertice in self.grafo}
        distancias[inicio.valor] = 0
        cola = [(0, inicio.valor)]
        heapq.heapify(cola)
        
        while cola:
            distancia_actual, nodo_actual = heapq.heappop(cola)
            if nodo_actual == final.valor:
                break
            for vecino, peso in self.grafo[nodo_actual]:
                distancia = distancias[nodo_actual] + peso
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    heapq.heappush(cola, (distancia, vecino))

        camino = []
        nodo_actual = final.valor
        while nodo_actual != inicio.valor:
            camino.append(nodo_actual)
            for vecino, peso in self.grafo[nodo_actual]:
                if distancias[nodo_actual] == distancias[vecino] + peso:
                    nodo_actual = vecino
                    break

        camino.append(inicio.valor)
        camino.reverse()

        cont = 0
        cadena = ""
        for vertice in camino:
            if cont == len(camino) - 1:
                cadena = cadena + f"{vertice}"
            else:
                cadena = cadena + f"{vertice} -> "
            cont = cont + 1
        return cadena
    

# Creación grafo no dirigido
A = Vertices("A") 
B = Vertices("B") 
C = Vertices("C") 
D = Vertices("D") 
E = Vertices("E") 
F = Vertices("F") 
G = Vertices("G") 
H = Vertices("H") 
GR = Grafos()
print(GR.grafo)

# Agregar vértices
GR.agregarVertice(A)
GR.agregarVertice(B)
GR.agregarVertice(C)
GR.agregarVertice(D)
GR.agregarVertice(E)
GR.agregarVertice(F)
GR.agregarVertice(G)
GR.agregarVertice(H)
print(GR.grafo)

# Agregar aristas con pesos
GR.agregarArista(A, B, 3)
GR.agregarArista(A, C, 1)
GR.agregarArista(B, D, 1)
GR.agregarArista(B, G, 5)
GR.agregarArista(C, D, 2)
GR.agregarArista(C, F, 5)
GR.agregarArista(D, F, 2)
GR.agregarArista(D, E, 4)
GR.agregarArista(E, G, 2)
GR.agregarArista(E, H, 1)
GR.agregarArista(F, H, 3)
print(GR.grafo)

# Recorridos en profundidad DFS
print(f"DFS desde 'A': {GR.recorrerProfundidad(A.valor)}")
print(f"DFS desde 'B': {GR.recorrerProfundidad(B.valor)}")
print(f"DFS desde 'C': {GR.recorrerProfundidad(C.valor)}")
print(f"DFS desde 'D': {GR.recorrerProfundidad(D.valor)}")
print(f"DFS desde 'E': {GR.recorrerProfundidad(E.valor)}")
print(f"DFS desde 'F': {GR.recorrerProfundidad(F.valor)}")
print(f"DFS desde 'G': {GR.recorrerProfundidad(G.valor)}")
print(f"DFS desde 'H': {GR.recorrerProfundidad(H.valor)}\n")

# Caminos menos pesados
print(f"Camino menos pesado de 'E' a 'A': {GR.caminoMenosPesado(E, A)}")
