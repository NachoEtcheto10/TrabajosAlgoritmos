import heapq

grafo = {
    "cocina": [],
    "comedor": [],
    "cochera": [],
    "quincho": [],
    "baño 1": [],
    "baño 2": [],
    "habitación 1": [],
    "habitación 2": [],
    "sala de estar": [],
    "terraza": [],
    "patio": []
}

def agregar_arista(grafo, origen, destino, distancia):
    grafo[origen].append((destino, distancia))
    grafo[destino].append((origen, distancia))

agregar_arista(grafo, "cocina", "comedor", 5)
agregar_arista(grafo, "cocina", "baño 1", 8)
agregar_arista(grafo, "cocina", "habitación 1", 10)

agregar_arista(grafo, "comedor", "sala de estar", 7)
agregar_arista(grafo, "comedor", "terraza", 12)
agregar_arista(grafo, "comedor", "baño 2", 6)

agregar_arista(grafo, "cochera", "quincho", 15)
agregar_arista(grafo, "cochera", "patio", 20)
agregar_arista(grafo, "cochera", "terraza", 25)

agregar_arista(grafo, "habitación 1", "baño 1", 3)
agregar_arista(grafo, "habitación 1", "habitación 2", 4)
agregar_arista(grafo, "habitación 1", "sala de estar", 15)

agregar_arista(grafo, "habitación 2", "baño 2", 2)
agregar_arista(grafo, "habitación 2", "terraza", 8)
agregar_arista(grafo, "habitación 2", "patio", 9)

def arbol_expansion_minima(grafo):
    inicio = next(iter(grafo))  
    visitados = set()
    min_heap = [(0, inicio)]
    total_distancia = 0

    while min_heap and len(visitados) < len(grafo):
        distancia, vertice = heapq.heappop(min_heap)
        if vertice not in visitados:
            visitados.add(vertice)
            total_distancia += distancia
            for vecino, peso in grafo[vertice]:
                if vecino not in visitados:
                    heapq.heappush(min_heap, (peso, vecino))

    return total_distancia


distancia_total_mst = arbol_expansion_minima(grafo)
print("Distancia total del árbol de expansión mínima:", distancia_total_mst, "metros")


def camino_mas_corto(grafo, inicio, destino):
    distancias = {v: float("inf") for v in grafo}
    distancias[inicio] = 0
    min_heap = [(0, inicio)]
    visitados = set()

    while min_heap:
        distancia_actual, vertice = heapq.heappop(min_heap)

        if vertice in visitados:
            continue
        visitados.add(vertice)

        if vertice == destino:
            return distancia_actual

        for vecino, peso in grafo[vertice]:
            if vecino not in visitados:
                nueva_distancia = distancia_actual + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    heapq.heappush(min_heap, (nueva_distancia, vecino))

    return float("inf")


distancia_corta = camino_mas_corto(grafo, "habitación 1", "sala de estar")
print("Distancia del camino más corto de habitación 1 a sala de estar:", distancia_corta, "metros")
