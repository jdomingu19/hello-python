class Nodo:

	def __init__(self, dato):
		self.dato      =  dato
		self.izquierda = None
		self.derecha   = None

class Arbol:

	def __init__(self, nodo):
		self.raiz = nodo

	def __agregar(self , nodo, nuevo_nodo):
		if nuevo_nodo.dato < nodo.dato:
			if nodo.izquierda is None:
				nodo.izquierda = nuevo_nodo
			else:
				self.__agregar(nodo.izquierda, nuevo_nodo)
		else:
			if nodo.derecha is None:
				nodo.derecha = nuevo_nodo
			else:
				self.__agregar(nodo.derecha, nuevo_nodo)	

	def agregar(self, nuevo_nodo):
		self.__agregar(self.raiz, nuevo_nodo)

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


n1 = Nodo(10)
n2 = Nodo(8)
n3 = Nodo(5)
n4 = Nodo(11)

a1 = Arbol(n1)
a1.agregar(n2)
a1.agregar(n3)
a1.agregar(n4)


a1.inorden()
print("")
a1.preorden()

encontrado = a1.buscar(50)
if encontrado is None:
	print("no encontrado")
else:	
	print("Encontrado")