import pygame
from pygame.locals import *

from shaders import *

from gl import Renderer, Model

from pickle import TRUE
from math import cos, sin, radians

width = 960
height = 540

deltaTime = 0.0

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rend = Renderer(screen)

rend.setShaders(vertex_shader, fragment_shader,toon_shader)

rend.target.z = -5

cookie = Model("cookie.obj", "body.bmp")

cookie.position.z -= 5
cookie.scale.x = 2
cookie.scale.y = 2
cookie.scale.z = 2

banana = Model("banana.obj", "banana.bmp")
banana.position.z -= 5
banana.scale.x = 9
banana.scale.y = 9
banana.scale.z = 9

oreo = Model("oreo.obj", "skin.bmp")
oreo.position.z -= 3
oreo.scale.x = 0.01
oreo.scale.y = 0.01
oreo.scale.z = 0.01


# face.position.z -= 10

rend.scene.append( cookie )


isRunning = True

while isRunning:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

            elif event.key == pygame.K_z:
                rend.filledMode()
            elif event.key == pygame.K_x:
                rend.wireframeMode()
            

    if keys[K_q]:
        if rend.camDistance > 2:
            rend.camDistance -= 2 * deltaTime
    elif keys[K_e]:
        if rend.camDistance < 10:
            rend.camDistance += 2 * deltaTime

    if keys[K_a]:
        rend.angle -= 30 * deltaTime
    elif keys[K_d]:
        rend.angle += 30 * deltaTime


    if keys[K_w]:
        if rend.camPosition.y < 2:
            rend.camPosition.y += 5 * deltaTime
    elif keys[K_s]:
        if rend.camPosition.y > -2:
            rend.camPosition.y -= 5 * deltaTime

    if keys[K_n]:
        rend.scene.clear()
        rend.scene.append( banana )
    elif keys[K_m]:
        rend.scene.clear()
        rend.scene.append( oreo )
    elif keys[K_l]:
        rend.scene.clear()
        rend.scene.append( cookie )
        
        

    rend.target.y = rend.camPosition.y

    rend.camPosition.x = rend.target.x + sin(radians(rend.angle)) * rend.camDistance
    rend.camPosition.z = rend.target.z + cos(radians(rend.angle)) * rend.camDistance

    if keys[K_LEFT]:
        rend.pointLight.x -= 10 * deltaTime

    elif keys[K_RIGHT]:
        rend.pointLight.x += 10 * deltaTime
    elif keys[K_UP]:
        rend.pointLight.y += 10 * deltaTime
    elif keys[K_DOWN]:
        rend.pointLight.y -= 10 * deltaTime

    deltaTime = clock.tick(60) / 1000
    #print(deltaTime)

    rend.time += deltaTime

    rend.update()
    rend.render()
    pygame.display.flip()

pygame.quit()