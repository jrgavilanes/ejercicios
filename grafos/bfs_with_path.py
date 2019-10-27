class G:
	def __init__(self, vertices):
		self._vertices = list(set(vertices))
		self._aristas = {}
		
	
	def addVertice(self,vertice):
		if vertice not in self._vertices:
			self._vertices.append(vertice)
			
			
	def orden(self):
		return len(self._vertices)
		
		
	def medida(self):
		aristas = []
		for k in self._aristas.keys():
			for a in self._aristas[k]:
				if str(sorted([k,a])) not in aristas:
					aristas.append(str(sorted([k,a])))
			
		return len(aristas)
		
	
	def addArista(self,origen,destino):
		if not (origen in self._vertices and destino in self._vertices):
			print("WARNING: Vertices tienen que existir en el grafo", origen, destino)
			return
		
		try:
			self._aristas[origen].append(destino)
			self._aristas[origen]=sorted(list(set(self._aristas[origen])))
		except:
			self._aristas[origen]=[destino]

			
	def addAristas(self,origen,destinos):
		for d in destinos:
			self.addArista(origen,d)
			

	def __str__(self):
		return "Vertices: " + str(self._vertices) + ", Orden: " +  str(len(self._vertices)) +  "\nAristas: " + str(self._aristas)
		
	def BFS(self, origen):
		cola = [origen]
		visitados = []
		
		while len(cola)>0:
			print('Exploro:',cola[0])
			visitados.append(cola[0])			
			
			for e in self._aristas[cola[0]]:
				if e not in visitados:
					cola.append(e)
				
			print("cola",cola)
				
			cola=cola[1:]
			
		print("FIN de exploracion del grafo")
		
	def PATH(self, origen, destino):
		padre = {}
		padre[origen]=origen
		cola = [origen]
		
		while len(cola)>0:						
			nodo=cola.pop(0)			
			for v in self._aristas[nodo]:
				if v not in padre:
					padre[v]=nodo
					cola.append(v)
		
		if destino not in padre:
			return "Destino inalcanzable"		

		camino=[destino]
		while destino != origen:
			destino=padre[destino]
			camino.insert(0,destino)
		
		return camino
			

  
  
g = G(['a','b','c','d','e','f','g','h','i','j','k','l','m'])
print(g)
g.addAristas('a',['b','c'])
g.addAristas('b',['d','e','f','a'])
g.addAristas('c',['g','h','i','a'])
g.addAristas('d',['j','k','b'])
g.addAristas('e',['b'])
g.addAristas('f',['b'])
g.addAristas('g',['c'])
g.addAristas('h',['c'])
g.addAristas('i',['c'])
g.addAristas('j',['l','d'])
g.addAristas('k',['m','d'])
g.addAristas('l',['j'])
g.addAristas('m',['k'])
print(g)
print(g.orden())
print(g.medida())
g.BFS('l')
print("camino de A a H:", g.PATH('a','h'))		
