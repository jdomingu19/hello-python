"""
Semana 5 | Parcial 1 | Jesús Alberto Domínguez Charris

Diseñe un método que indique si un dato ingresado 
por el usuario aparece repetido en la lista.
"""

# Importar todo de ListaSimple2023.py
from ListaSimple2023 import *

# Creación lista
miLista = ListaEnlazadaSimple()
miLista.adicionarAlFinal(10)
miLista.adicionarAlFinal(20)
miLista.adicionarAlFinal(30)
miLista.adicionarAlFinal(40)
miLista.adicionarAlFinal(50)
miLista.adicionarAlFinal(50)
miLista.adicionarAlFinal(50)
miLista.adicionarAlFinal(60)
miLista.adicionarAlFinal(70)

print(f"-> Lista simple: {miLista} ({miLista.contarNodos()} nodos)")
print(f"¿10 está repetido?: {miLista.datoRepetido(10)} ({miLista.repeticionesDato(10)} apariciones)")
print(f"¿20 está repetido?: {miLista.datoRepetido(20)} ({miLista.repeticionesDato(20)} apariciones)")
print(f"¿30 está repetido?: {miLista.datoRepetido(30)} ({miLista.repeticionesDato(30)} apariciones)")
print(f"¿40 está repetido?: {miLista.datoRepetido(40)} ({miLista.repeticionesDato(40)} apariciones)")
print(f"¿50 está repetido?: {miLista.datoRepetido(50)} ({miLista.repeticionesDato(50)} apariciones)")
print(f"¿60 está repetido?: {miLista.datoRepetido(60)} ({miLista.repeticionesDato(60)} apariciones)")
print(f"¿70 está repetido?: {miLista.datoRepetido(70)} ({miLista.repeticionesDato(70)} apariciones)")

print(f"¿80 está repetido?: {miLista.datoRepetido(80)} ({miLista.repeticionesDato(80)} apariciones)")
print(f"¿90 está repetido?: {miLista.datoRepetido(90)} ({miLista.repeticionesDato(90)} apariciones)")
print(f"¿100 está repetido?: {miLista.datoRepetido(100)} ({miLista.repeticionesDato(100)} apariciones)")

"""

El método del parcial es: miLista.datoRepetido(dato_buscar)

Para saber el número de repeticiones utilice el método
miLista.repeticionesDato(dato_buscar), este le devolverá 
un número entero que representa la cantidad exacta de 
apariciones de un dato buscado en la lista simple.

miLista.datoRepetido(dato_buscar)    -> devuelve un booleano o None
miLista.repeticioneDato(dato_buscar) -> devuelve un entero o None

"""
