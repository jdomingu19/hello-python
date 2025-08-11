# Generador URL | experimentos-jesus.000webhostapp.com

"""
Cosas por hacer:
- Menú
- Validaciones
- Copiar al portapapeles
"""

# Menú
print("- - Generador de URL - -")
print("1) Páginas")
print("2) Pruebas")
accion = eval(input("¿Qué desea hacer?: "))

while accion != 1 and accion != 2:
    print("Acción no válida...")
    accion = eval(input("¿Qué desea hacer?: "))

# 1) Páginas
if accion == 1:
    pagina = "https://experimentos-jesus.000webhostapp.com"
    categoria = "paginas"
    tipo = "ejemplo"

    print("- - Páginas - -")
    i = 1
    while i <= 4:
        print(f"{pagina}/{categoria}/{tipo}{i}")
        i = i + 1

# 2) Pruebas
elif accion == 2:
    pagina = "https://experimentos-jesus.000webhostapp.com"
    categoria = "pruebas"
        
    print("- - Pruebas - -")
    print("1) Mostar todas las URL de pruebas")
    print("2) Galerias")
    print("3) Tarjetas")
    print("4) Calculadoras")
    menu_pruebas = eval(input("¿Qué desea hacer?: "))
    
    while menu_pruebas != 1 and menu_pruebas != 2 and menu_pruebas != 3 and menu_pruebas != 4:
        print("- - Pruebas - -")
        print("1) Mostar todas las URL de pruebas")
        print("2) Galerias")
        print("3) Tarjetas")
        print("4) Calculadoras")
        print("Acción no válida...")
        menu_pruebas = eval(input("¿Qué desea hacer?: "))

    if menu_pruebas == 3:
        tipo = "tarjetas"
        print("- - Tarjetas - -")
        i = 1
        while i <= 11:
            print(f"{pagina}/{categoria}/{tipo}{i}")
            i = i + 1

        copiar_portapales = eval(input("¿Desea copiar las URL al portapapeles?: "))