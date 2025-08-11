import pyautogui as pg
import time

time.sleep(5)
multiplicar_dos_numeros = """num1 = int(input('Num1: '))
num2 = int(input('Num2: '))
producto = num1 * num2
print('Producto:', producto)
"""
pg.write(multiplicar_dos_numeros)
