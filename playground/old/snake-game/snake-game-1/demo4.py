# Snake game by: YouDevs
import turtle
# import time

# posponer = 0.1
# Crear ventana
wn = turtle.Screen()

# Propiedades ventana
wn.title('Snake Game 1') # título
wn.bgcolor('black') # color fondo
wn.setup(width=600, height=600) # redimensionar
wn.tracer(0) # animaciones fluidas

# Cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape('square') # forma cabeza
cabeza.color('white')
cabeza.penup() # no dejar rastro al mover
cabeza.goto(0, 0) # ir a x, y
cabeza.direction = 'stop'

# Funciones
def arriba():
    cabeza.direction = 'up'

def abajo():
    cabeza.direction = 'down'

def izquierda():
    cabeza.direction = 'left'

def derecha():
    cabeza.direction = 'right'

def movimiento():
    if cabeza.direction == 'up':
        y = cabeza.ycor() # obtener coordenada y
        # cabeza.sety(y + 20) time
        cabeza.sety(y + 0.05)
        
    if cabeza.direction == 'down':
        y = cabeza.ycor() # obtener coordenada y
        # cabeza.sety(y - 20) time
        cabeza.sety(y - 0.05)
    
    if cabeza.direction == 'left':
        x = cabeza.xcor() # obtener coordenada x
        # cabeza.setx(x - 20) time
        cabeza.setx(x - 0.05)
        
    if cabeza.direction == 'right':
        x = cabeza.xcor() # obtener coordenada x
        # cabeza.setx(x + 20) time
        cabeza.setx(x + 0.05)

# Teclado
wn.listen() # eschucar eventos teclado y más
wn.onkeypress(arriba, 'Up') # (función SIN PARÉNTESIS NO EJECUTAR, 'NombreTecla')
wn.onkeypress(abajo, 'Down') # (función SIN PARÉNTESIS NO EJECUTAR, 'NombreTecla')
wn.onkeypress(izquierda, 'Left') # (función SIN PARÉNTESIS NO EJECUTAR, 'NombreTecla')
wn.onkeypress(derecha, 'Right') # (función SIN PARÉNTESIS NO EJECUTAR, 'NombreTecla')

# Bucle juego
while True:
    wn.update() # actualizar ventana
    movimiento()
    # time.sleep(posponer)

# Mantener ventana abierta
# turtle.mainloop() 
