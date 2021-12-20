import pygame
from pygame.locals import *

#FUNCIONES DE PYGAME
pygame.init()
reloj = pygame.time.Clock()

#PANTALLA
largo= 1280
ancho= 600
pygame.display.set_caption("The Battle of the Tanks")
Pant = pygame.display.set_mode([largo,ancho])

#COLORES
Celeste = (54,203,201)
Verde = (44,177,26)
Azul = (0,0,255)
Blanco = (255,255,255)
Amarillo = (255, 255, 0)
Naranja = (253,126,0)
Morado = (105,0,144)
Negro = (0,0,0)
Rojo = (255, 0, 0) 

#INFORMACION DE LOS TANQUES
XdelTank = [0,1]

X_Y_Tanques = [0,1,2,3] #XA,YA,XR,YR

Angulo_Rojo = [0]
Velocidad_Rojo = [0]
Angulo_Azul = [0]
Velocidad_Azul = [0]

vidaTank = [0,1]

#BALAS
Balaaux = [0]
balas = [0,1,2,3,4,5]

#OTRAS VARIABLES DEL JUEGO
Turno = [0]
Partida = [0]
aux = False
mapa = []