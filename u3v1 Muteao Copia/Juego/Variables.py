import pygame, sys
from pygame.locals import *
import random as r
#FUNCIONES DE PYGAME
pygame.init()
reloj = pygame.time.Clock()

#PANTALLA
largo= 1280
ancho= 600
pygame.display.set_caption("The Battle of the Tanks")
Pant = pygame.display.set_mode([largo,ancho])

mousex, mousey = pygame.mouse.get_pos()

#COLORES
Celeste = (54,203,201)
Verde = (44,177,26)
Azul = (0,0,255)
Blanco = (255,255,255)
#colores que pueden ser para tanques
Amarillo = (255, 255, 0)
Naranja = (253,126,0)
Morado = (105,0,144)
Negro = (0,0,0)
Rojo = (255, 0, 0) 

color = (r.randint(0,255), r.randint(0,255), r.randint(0,255))
color2 =  (r.randint(0,255), r.randint(0,255), r.randint(0,255))

#INFORMACION DE LOS TANQUES
XdelTank = [0,1]

X_Y_Tanques = [0,1,2,3] #XA,YA,XR,YR

xtanque = [0,1,2,3,4,5]
ytanque = [0,1,2,3,4,5]

Angulo_Rojo = [0]
Velocidad_Rojo = [0]
Angulo_Azul = [0]
Velocidad_Azul = [0]

vidaTank = [0,1]

#BALAS
Balaaux = [0]
balaspj1 = [0,1,2]
balaspj2 = [0,1,2]
balaspj3 = [0,1,2]
balaspj4 = [0,1,2]

#OTRAS VARIABLES DEL JUEGO
Turno = [0]
Partida = [0]
aux = False
mapa = []

prueba = 0
text = str

botonamarillo = False
botonnaranja = False
botonmorado = False  