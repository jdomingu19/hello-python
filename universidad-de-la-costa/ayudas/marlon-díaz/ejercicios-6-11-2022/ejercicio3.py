# Ejercicio 3
n = 20

notas = []
i = 1
while i <= n:
    nota = eval(input("Ingrese nota (0 - 5): "))
    notas.append(nota)
    i = i + 1

cont_1 = 0
cont_2 = 0
cont_3 = 0
i = 0
while i < len(notas):
    if notas[i] > 4:
        cont_1 = cont_1 + 1
    if notas[i] >= 3 and notas[i] <= 4:
        cont_2 = cont_2 + 1
    if notas[i] < 3:
        cont_3 = cont_3 + 1
    i = i + 1

print("Notas mayores que 4:", cont_1)
print("Notas entre 3 y 4:", cont_2)
print("Notas menores que 3:", cont_3)