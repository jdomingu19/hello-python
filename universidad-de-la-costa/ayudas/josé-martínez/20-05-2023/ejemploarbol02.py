class Nodo:

	def __init__(self, dato):
		self.dato      =  dato
		self.izquierda = None
		self.derecha   = None

class Arbol:

	def __init__(self, dato):
		self.raiz = Nodo(dato)

	def __agregar(self , nodo, nuevo_valor):
		if nuevo_valor < nodo.dato:
			if nodo.izquierda is None:
				nodo.izquierda = Nodo(nuevo_valor)
			else:
				self.__agregar(nodo.izquierda, nuevo_valor)
		else:
			if nodo.derecha is None:
				nodo.derecha = Nodo(nuevo_valor)
			else:
				self.__agregar(nodo.derecha, nuevo_valor)	

	def agregar(self, nuevo_valor):
		self.__agregar(self.raiz, nuevo_valor)

	# inorden
	def __inorden(self, nodo):
		if nodo is not None:
			self.__inorden(nodo.izquierda)
			print(nodo.dato, end=" ")
			self.__inorden(nodo.derecha)

	def inorden(self):
		self.__inorden(self.raiz)

	# preorden
	def __preorden(self, nodo):
		if nodo is not None:
			print(nodo.dato, end=" ")
			self.__preorden(nodo.izquierda)
			self.__preorden(nodo.derecha)

	def preorden(self):
		self.__preorden(self.raiz)

	def __buscar(self, nodo, valor):
		if nodo is None:
			return None
		if nodo.dato ==	valor:
			return nodo
		
		if valor < nodo.dato:
			return self.__buscar(nodo.izquierda, valor)
		else:
			return self.__buscar(nodo.derecha, valor)
			
	    
	def buscar(self, valor):
		nodoTMP = self.__buscar(self.raiz, valor)
		return	nodoTMP


a1 = Arbol(10)
a1.agregar(8)
a1.agregar(5)
a1.agregar(11)
a1.agregar(2)
a1.agregar(9)
a1.agregar(13)
a1.agregar(12)

a1.inorden()
a1.preorden()

# encontrado = a1.buscar(50)
# if encontrado is None:
# 	print("no encontrado")
# else:	
# 	print("Encontrado")