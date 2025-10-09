from listas_2022 import ListaSimple
#Creacion de listas
lista01 = ListaSimple()
lista02 = ListaSimple()
#Adicionamos datos a las listas
lista01.adicionarAlInicio(1)
lista01.adicionarAlInicio(2)
lista01.adicionarAlInicio(3)
print("Lista 01:",lista01)
lista02.adicionarAlInicio(2)
lista02.adicionarAlInicio(2)
lista02.adicionarAlInicio(3)
print("Lista 02:",lista02)
print("Igualdad:",lista01.comparar(lista02))