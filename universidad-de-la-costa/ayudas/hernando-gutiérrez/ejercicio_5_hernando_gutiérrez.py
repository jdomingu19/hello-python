# Algoritmos pollitos

# Variables
listos_procesados = 0
pollitos_hembras = 0
pollitos_machos = 0
pollitos_hembras_vacunar = 0
pollitos_machos_vacunar = 0

cantidad_pollitos = eval(input("Ingrese la cantidad de pollitos: "))

# Ciclo
for i in range(cantidad_pollitos):
    tiempo = eval(input(f"Ingrese el tiempo de cría del pollito {i+1} (Días): "))
    sexo = eval(input(f"Ingrese el sexo del pollito {i+1} (1 = Hembra 2 = Macho): "))
    
    # Pollos que están listos para procesar
    if tiempo > 45:
        listos_procesados = listos_procesados + 1
    
    # Pollos hembras
    if sexo == 1:
        pollitos_hembras = pollitos_hembras + 1
        # Listos para vacunar
        if tiempo >= 10 and tiempo <= 25:
            pollitos_hembras_vacunar = pollitos_hembras_vacunar + 1
    
    # Pollos machos
    if sexo == 2:
        pollitos_machos = pollitos_machos + 1
        # Listos para vacunar
        if tiempo >= 10 and tiempo <= 25:
            pollitos_machos_vacunar = pollitos_machos_vacunar + 1

# Porcentajes
porcentaje_listos_procesados = (listos_procesados / cantidad_pollitos) * 100
porcentaje_pollitos_hembras = (pollitos_hembras / cantidad_pollitos) * 100
porcentaje_pollitos_machos = (pollitos_machos / cantidad_pollitos) * 100
porcentaje_pollitos_machos_vacunar = (pollitos_machos_vacunar / cantidad_pollitos) * 100
porcentaje_pollitos_hembras_vacunar = (pollitos_hembras_vacunar / cantidad_pollitos) * 100

# Resultados   
print("RESULTADOS")
print("1) Pollitos listo para ser procesados: ", listos_procesados, " (", porcentaje_listos_procesados, "%)")
print("2) Pollitos hembra: ", pollitos_hembras, " (", porcentaje_pollitos_hembras, "%)")
print("3) Pollitos machos listo para vacunar: ", pollitos_machos_vacunar, " (", porcentaje_pollitos_machos_vacunar, "%)")
print("4) Pollitos hembras listo para vacunar: ", pollitos_hembras_vacunar, " (", porcentaje_pollitos_hembras_vacunar, "%)")

if porcentaje_pollitos_hembras > porcentaje_pollitos_machos:
    print("5) Hay más hembras que machos (", porcentaje_pollitos_hembras, " vs ", porcentaje_pollitos_machos, ")")
elif porcentaje_pollitos_hembras < porcentaje_pollitos_machos:
    print("5) Hay menos hembras que machos (", porcentaje_pollitos_hembras, " vs ", porcentaje_pollitos_machos, ")")
else:
    print("5) Hay igual cantidad de hembras que machos (", porcentaje_pollitos_hembras, "% vs ", porcentaje_pollitos_machos, "%)")