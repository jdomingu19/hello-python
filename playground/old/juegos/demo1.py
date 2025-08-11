# Mi primer juego en Python

# Importar librerías
from ursina import *

from ursina.prefabs.\
    first_person_controller \
    import FirstPersonController

from ursina.shaders import\
    lit_with_shadows_shader

# Crear ventana
app = Ursina(borderless=False)
random.seed(0)
Entity.default_shader = \
    lit_with_shadows_shader
window.size = (700, 700)

# Suelo
ground = Entity(
    model = 'plane',
    collider = 'box',
    scale = 64,
    color = color.red
)

# Jugador
player = FirstPersonController()
player.position = Vec3(0,3,0)

# Cubos
class Cubo(Entity):
    def __init__(self,position=(0,0,0)):
        super().__init__(position=position, model='cube', scale = (1,1), origin_y= .5, color = color.light_gray, collider = 'box')

# Cubo inicial
Cubo(position = (0,1,0))

# 30 cubos aleatorios
for z in range(30):
    Cubo(position = (random.randint(1,5),1,z))

# Si el personaje se cae...
def update():
    if player.position.y <= -4:
        player.position = Vec3(0,10,0)

# Suelo más profundo
ground.position = Vec3(0,-5,0)

# Añadir cielo     
Sky()

# Iniciar
app.run()