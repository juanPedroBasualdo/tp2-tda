from collections import deque

def main(s1: int, s2: int, relaciones: list[tuple[int, int, int]]) -> tuple[set[int], set[int]]:
    nodos = {s1, s2}
    for u, v, w in relaciones:
        nodos.add(u)
        nodos.add(v)
    
    capacidad = {nodo: {} for nodo in nodos}
    for u, v, w in relaciones:
        capacidad[u][v] = capacidad[u].get(v, 0) + w

    def bfs_camino_aumento(s, t, padres):
        visitados = {s}
        cola = deque([s])
        while cola:
            u = cola.popleft()
            for v, cap_res in capacidad[u].items():
                if v not in visitados and cap_res > 0:
                    visitados.add(v)
                    padres[v] = u
                    if v == t:
                        return True
                    cola.append(v)
        return False

    # Edmonds-Karp
    padres = {}
    while bfs_camino_aumento(s1, s2, padres):
        flujo_camino = float('inf')
        actual = s2
        while actual != s1:
            previo = padres[actual]
            flujo_camino = min(flujo_camino, capacidad[previo][actual])
            actual = previo
        
        actual = s2
        while actual != s1:
            previo = padres[actual]
            capacidad[previo][actual] -= flujo_camino
            capacidad[actual][previo] = capacidad[actual].get(previo, 0) + flujo_camino
            actual = previo
        padres = {}

    seguidores_s1 = {s1}
    cola_final = deque([s1])
    while cola_final:
        u = cola_final.popleft()
        for v, cap_res in capacidad[u].items():
            if v not in seguidores_s1 and cap_res > 0:
                seguidores_s1.add(v)
                cola_final.append(v)
    
    seguidores_s2 = nodos - seguidores_s1
    
    return seguidores_s1, seguidores_s2
