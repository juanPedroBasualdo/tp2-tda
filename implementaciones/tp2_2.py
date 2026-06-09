from collections.abc import Sequence
import math

_productos = []
_k = 0
_C = 0
_a = 0
_n = 0

_mejor_ganancia = float("-inf")
_mejor_solucion = []

_contenedores = []
_ocupacion = []
_valores_restantes = []

def _ganancia_final(ganancia_productos):
    penalizacion = 0

    for j in range(_k):
        if _ocupacion[j] > 0:
            espacio_libre = _C - _ocupacion[j]
            penalizacion += espacio_libre * _a

    return ganancia_productos - penalizacion

def branch_and_bound(i, ganancia_actual):
    global _mejor_ganancia, _mejor_solucion

    if i == _n:
        ganancia_final = _ganancia_final(ganancia_actual)

        if ganancia_final > _mejor_ganancia:
            _mejor_ganancia = ganancia_final
            _mejor_solucion = [contenedor.copy() for contenedor in _contenedores]

        return

    limite_superior = ganancia_actual + _valores_restantes[i]

    if limite_superior <= _mejor_ganancia:
        return

    tamanio, valor = _productos[i]

    for j in range(_k):
        if _ocupacion[j] + tamanio <= _C:
            _contenedores[j].add(i)
            _ocupacion[j] += tamanio

            branch_and_bound(i + 1, ganancia_actual + valor)

            _ocupacion[j] -= tamanio
            _contenedores[j].remove(i)

    branch_and_bound(i + 1, ganancia_actual)

def main(productos: list[tuple[int, int]], k: int, C: int, a: int) -> tuple[int, list[set[int]]]:
    global _productos, _k, _C, _a, _n
    global _mejor_ganancia, _mejor_solucion
    global _contenedores, _ocupacion, _valores_restantes

    _productos = productos
    _k = k
    _C = C
    _a = a
    _n = len(_productos)

    _mejor_ganancia = float("-inf")
    _mejor_solucion = [set() for _ in range(_k)]

    _contenedores = [set() for _ in range(_k)]
    _ocupacion = [0 for _ in range(_k)]

    _valores_restantes = [0] * (_n + 1)
    for i in range(_n - 1, -1, -1):
        _valores_restantes[i] = _valores_restantes[i + 1] + _productos[i][1]

    branch_and_bound(0, 0)

    return _mejor_ganancia, _mejor_solucion
