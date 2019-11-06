from typing import Optional


def is_conected(ady, a, b) -> bool:
    """Are vertex a and b conected in the adyacence list given?"""
    if type(a) == str and type(b) == str:
        a = str(a).lower()
        b = str(b).lower()

    visited = {}
    for n in ady:
        visited[n] = False

    cola = [a]
    while len(cola) > 0:
        intento = cola.pop(0)
        for n in ady[intento]:
            if not visited[n]:
                cola.append(n)
                visited[n] = True

    return visited.get(b, False)


def get_arista_id(a, b) -> tuple:
    """Return lower vertex first"""
    arista = ()
    if a >= b:
        arista = (b, a)
    else:
        arista = (a, b)

    return arista


class Grafo:
    def __init__(self):
        self._ady = {}
        self._aristas = []
        self._vertices = []

    def _best_aristas(self, descendiente=False):
        return sorted(self._aristas, key=lambda x: x[2], reverse=descendiente)

    def set_arista(self, a, b, w: float) -> None:
        arista = get_arista_id(a, b)
        self._aristas.append((arista[0], arista[1], w))
        try:
            self._ady[arista[0]].append(arista[1])
        except KeyError:
            self._ady[arista[0]] = []
            self._ady[arista[0]].append(arista[1])

        try:
            self._ady[arista[1]].append(arista[0])
        except KeyError:
            self._ady[arista[1]] = []
            self._ady[arista[1]].append(arista[0])

        self._vertices = self._get_vertices()[:]

    def get_generador(self, maximo=False) -> Optional[tuple]:
        """Devuelvo aristas y lista de adyacencias del mejor arbol generador del grafo"""
        generador_ady = {}
        for i in self._get_vertices():
            generador_ady[i] = []

        best = self._best_aristas(descendiente=maximo)

        generador_aristas = []
        while len(generador_aristas) < len(self._get_vertices()) - 1:
            if len(best) <= 0:
                return None
            a, b, w = best.pop(0)
            if not is_conected(generador_ady, a, b):
                generador_aristas.append((a, b, w))
                generador_ady[a].append(b)
                generador_ady[b].append(a)

        return list(generador_aristas), generador_ady.copy()

    def _get_vertices(self) -> list:
        vertices = []
        for i in self._aristas:
            vertices.append(i[0])
            vertices.append(i[1])
        vertices = list(set(vertices))

        return sorted(vertices)


g = Grafo()
g.set_arista("a1", "a2", 0.75)
g.set_arista("a1", "c1", 0.71)
g.set_arista("a1", "c2", 0.68)
g.set_arista("a2", "b2", 0.75)
g.set_arista("a2", "c1", 0.78)
g.set_arista("a2", "c2", 0.81)
g.set_arista("b2", "c1", 0.82)
g.set_arista("c1", "c2", 0.7)
g.set_arista("b2", "c2", 0.85)

print(g._get_vertices())
print(g._ady)
print(g._aristas)
print(g._best_aristas())
print(g._best_aristas(True))
print(g.get_generador(True))

mejores_aristas = g.get_generador(True)[0]

x = 1
for n in [n[2] for n in mejores_aristas]:
    x *= n

print("Probabilidad:", x)


