import pygame
import random
from pygame.locals import *

###############################################################
                        ##VARIABLES##
largo= 1280
ancho= 600
pygame.init()
Pant = pygame.display.set_mode([largo,ancho], pygame.RESIZABLE)
pygame.display.set_caption("The Battle of the Tanks")

Celeste = (54,203,201)
Verde = (44,177,26)
Azul = (0,0,255)
AzulClaro = (96,98,253)
Blanco = (255,255,255)
Amarillo = (255, 233, 0)
Negro = (0,0,0)
Rojo = (255, 0, 0) 
reloj = pygame.time.Clock()
aux = False
mapa = []
XdeTankA = random.randint(40,426)
XdeTankR = random.randint(800,1240)
X_Tanque_Rojo = [0]
Y_Tanque_Rojo = [0]
X_Tanque_Azul = [0]
Y_Tanque_Azul = [0]
Angulo_Rojo = [0]
Velocidad_Rojo = [0]
Angulo_Azul = [0]
Velocidad_Azul = [0]
Turno = [0]
Partida = [0]
###############################################################


vidaAzul = [0]
vidaRojo = [0]

#quedaste en implementar las vidas de los tanques como una lista

Balaaux = [0]

c105 = [0,1]
cperforante = [0,1]
c60 = [0,1]

EleccionbalaAzul = [0]
EleccionbalaRojo = [0]