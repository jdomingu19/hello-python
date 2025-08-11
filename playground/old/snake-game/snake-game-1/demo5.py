# Snake game by: YouDevs
import turtle
import time
import random

posponer = 0.1

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

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle') # forma comida
comida.color('red')
comida.penup() # no dejar rastro al mover
comida.goto(0, 100) # ir a x, y

# Cuerpo serpiente
segmentos = []

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
        cabeza.sety(y + 20)
        
    if cabeza.direction == 'down':
        y = cabeza.ycor() # obtener coordenada y
        cabeza.sety(y - 20)
    
    if cabeza.direction == 'left':
        x = cabeza.xcor() # obtener coordenada x
        cabeza.setx(x - 20)
        
    if cabeza.direction == 'right':
        x = cabeza.xcor() # obtener coordenada x
        cabeza.setx(x + 20)

# Teclado
wn.listen() # eschucar eventos teclado y más
wn.onkeypress(arriba, 'Up') # (función SIN PARÉNTESIS NO EJECUTAR, 'NombreTecla')
wn.onkeypress(abajo, 'Down') # (función SIN PARÉNTESIS NO EJECUTAR, 'NombreTecla')
wn.onkeypress(izquierda, 'Left') # (función SIN PARÉNTESIS NO EJECUTAR, 'NombreTecla')
wn.onkeypress(derecha, 'Right') # (función SIN PARÉNTESIS NO EJECUTAR, 'NombreTecla')

# Bucle juego
while True:
    wn.update() # actualizar ventana

    # Comer
    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape('square') # forma nuevo_segmento
        nuevo_segmento.color('grey')
        nuevo_segmento.penup() # no dejar rastro al mover
        segmentos.append(nuevo_segmento)

    # Crecer
    totalSeg = len(segmentos)
    for i in range(totalSeg - 1, 0, -1):
        x = segmentos[i - 1].xcor() # coordenada x segmento anterior
        y = segmentos[i - 1].ycor() # coordenada x segmento anterior
        segmentos[i].goto(x, y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)


    movimiento()

    time.sleep(posponer)

# Mantener ventana abierta
# turtle.mainloop() 
