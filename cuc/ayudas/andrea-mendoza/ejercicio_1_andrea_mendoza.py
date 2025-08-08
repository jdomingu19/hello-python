# Ejercicio 1

# Entradas
corte1 = eval(input("Ingrese la nota del primer corte: "))
corte2 = eval(input("Ingrese la nota del segundo corte: "))
corte3 = eval(input("Ingrese la nota del tercer corte: "))

# Condiciones
if corte1 >= 0 and corte1 <= 5 and corte2 >= 0 and corte2 <= 5 and corte3 >= 0 and corte3 <= 5:
    notaCorte1 = corte1 * 0.3 # 30%
    notaCorte2 = corte2 * 0.3 # 30%
    notaCorte3 = corte3 * 0.4 # 40%

    print("Nota final: ", round(notaCorte1 + notaCorte2 + notaCorte3, 2))
else:
    print("Notas ingresadas no válidas...")
    print("Deben ser entre 0 y 5...")