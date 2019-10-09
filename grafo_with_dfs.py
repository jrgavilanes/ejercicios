class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices

    @property
    def num_vertices(self):
        return len(self.__ady_list)

    @num_vertices.setter
    def num_vertices(self, value):
        self.__ady_list = {}
        for i in range(1, value + 1):
            self.__ady_list[i] = []

    def addArista(self, origen, destino):
        if not (origen in self.__ady_list and destino in self.__ady_list):
            print("Error: Los puntos a unir deben existir en el grafo", origen, destino)
            return -1

        if not destino in self.__ady_list[origen]:
            self.__ady_list[origen].append(destino)
            self.__ady_list[origen]=sorted(self.__ady_list[origen])
            return 0
        else:
            print("Warning: La arista ya existe. No la añado", origen, destino)
            return -1

    def addAristas(self, origen, destinos):
        for destino in destinos:
            self.addArista(origen, destino)

    def DFS(self, origen=1):
        visited={}
        for i in range(1, self.num_vertices + 1):
            visited[i] = False
        self.__DFS_util(visited, origen)

    def __DFS_util(self, visited, v):
        if not visited[v]:
            visited[v] = True
            print(v, end= " ")
            for i in self.__ady_list[v]:
                self.__DFS_util(visited, i)

    def show(self):
        return self.__ady_list.copy()

    def __str__(self):
        return str(self.__ady_list)


g = Grafo(7)
g.addAristas(1,[2,3,4])
g.addAristas(2,[1,5])
g.addAristas(3,[1,6])
g.addAristas(4,[1])
g.addAristas(5,[2,6])
g.addAristas(6,[3,5,7])
g.addAristas(7,[6])

print(g)
g.DFS(1)
