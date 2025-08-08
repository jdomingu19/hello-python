# Sistema de notas CUC

# Leer notas
nota_c1 = eval(input("Ingrese la nota primer corte (0 - 10): "))

while nota_c1 < 0 or nota_c1 > 10:
    print("La nota mínima es 0 y la máxima 10...")
    nota_c1 = eval(input("Ingrese la nota primer corte (0 - 10): "))

nota_c2 = eval(input("Ingrese la nota segundo corte (0 - 10): "))

while nota_c2 < 0 or nota_c2 > 10:
    print("La nota mínima es 0 y la máxima 10...")
    nota_c2 = eval(input("Ingrese la nota segundo corte (0 - 10): "))

nota_c3 = eval(input("Ingrese la nota tercer corte (0 - 10): "))

while nota_c3 < 0 or nota_c3 > 10:
    print("La nota mínima es 0 y la máxima 10...")
    nota_c3 = eval(input("Ingrese la nota tercer corte (0 - 10): "))

# Convertir a procentajes
nota_c1 = nota_c1 * 0.35 # 35%
nota_c2 = nota_c2 * 0.35 # 35%
nota_c3 = nota_c3 * 0.30 # 30%

promedio = nota_c1 + nota_c2 + nota_c3

# Mostrar resultados
if promedio >= 0 and promedio <= 4:
    print("Nota muy baja. Promedio:", promedio)
elif promedio > 4 and promedio < 6:
    print("Nota baja. Promedio:", promedio)
elif promedio >= 6 and promedio <= 8:
    print("Nota media. Promedio:", promedio)
else:
    print("Nota alta. Promedio:", promedio)