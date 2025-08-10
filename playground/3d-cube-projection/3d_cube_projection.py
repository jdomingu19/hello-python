# A 3D Cube Projection
# Author: Magoninho
# https://github.com/Magoninho

# ...
import pygame as pg
import numpy as np
import math

# ...
WHITE = (255, 255, 255)
TEAL = (0, 90, 90)
BLACK = (0, 0, 0)

# ...
WIDTH, HEIGHT = 800, 600

# ...
pg.display.set_caption("3D Cube Projection")

# ...
screen = pg.display.set_mode((WIDTH, HEIGHT))
scale = 100
circle_pos = [WIDTH / 2, HEIGHT / 2]
angle = 0
points = []

# ...
points.append(np.matrix([-1, -1, 1]))
points.append(np.matrix([1, -1, 1]))
points.append(np.matrix([1,  1, 1]))
points.append(np.matrix([-1, 1, 1]))
points.append(np.matrix([-1, -1, -1]))
points.append(np.matrix([1, -1, -1]))
points.append(np.matrix([1, 1, -1]))
points.append(np.matrix([-1, 1, -1]))

# ...
projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0]
])

# ...
projected_points = [
    [n, n] for n in range(len(points))
]

# ...
def connect_points(i, j, points):
    pg.draw.line(
        screen,
        BLACK,
        (points[i][0], points[i][1]),
        (points[j][0], points[j][1])
    )

# ...
clock = pg.time.Clock()

# ...
while True:
    # ...
    clock.tick(60)

    # ...
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                exit()
    
    # ...
        rotation_z = np.matrix([
        [math.cos(angle), -math.sin(angle), 0],
        [math.sin(angle), math.cos(angle), 0],
        [0, 0, 1],
    ])

    rotation_y = np.matrix([
        [math.cos(angle), 0, math.sin(angle)],
        [0, 1, 0],
        [-math.sin(angle), 0, math.cos(angle)],
    ])

    rotation_x = np.matrix([
        [1, 0, 0],
        [0, math.cos(angle), -math.sin(angle)],
        [0, math.sin(angle), math.cos(angle)],
    ])

    # ...
    angle += 0.01

    # ...
    screen.fill(WHITE)

    # ...
    i = 0
    for point in points:
        rotated2d = np.dot(rotation_z, point.reshape((3, 1)))
        rotated2d = np.dot(rotation_y, rotated2d)
        rotated2d = np.dot(rotation_x, rotated2d)

        projected2d = np.dot(projection_matrix, rotated2d)

        x = int(projected2d[0][0] * scale) + circle_pos[0]
        y = int(projected2d[1][0] * scale) + circle_pos[1]

        projected_points[i] = [x, y]

        pg.draw.circle(screen, TEAL, (x, y), 5)
        i += 1

    # ...
    for p in range(4):
        connect_points(p, (p + 1) % 4, projected_points)
        connect_points(p + 4, ((p + 1) % 4) + 4, projected_points)
        connect_points(p, (p + 4), projected_points)

    # ...
    pg.display.update()
