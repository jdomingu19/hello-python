# Snake game by: YouDevs
import turtle

# Inicializar tortuga
pluma = turtle.Turtle()

# Propiedades tortuga
pluma.speed(1) # velocidad
pluma.pensize(3) # tamaño lápiz

# Dibujar un cuadrado
for _ in range(4):
    pluma.forward(100) # avanzar 100 pixeles
    pluma.left(90) # izquierda 90 grados

# Mantener ventana abierta
turtle.mainloop() 
