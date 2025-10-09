mi_lista = list((-12, 10, 23, -7, 8, 2, -1, 0, 15, -8))
print(mi_lista, type(mi_lista))

mayor = mi_lista[0]
menor = mi_lista[0]
sumatoria = 0
for i in mi_lista:
    if i > mayor:
        mayor = i
    if i < menor:
        menor = i
    sumatoria = sumatoria + i

promedio = sumatoria / len(mi_lista)

print("Elemento mayor:", mayor)
print("Elemento menor:", menor)
print("Promedio elementos:", promedio)