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

fontiu = pygame.font.SysFont("Minecrafter.Reg.ttf", 20)

#Celeste = (54,203,201)
Celeste = (12,203,199)
#Celeste = (24,195,225)
#Verde = (44,177,26)
Verde = (34,174,2)
Azul = (1,14,193)
AzulClaro = (96,98,253)
Blanco = (255,255,255)
Amarillo = (255,241,25)
Naranja = (253,126,0)
#Morado = (105,0,144)
Morado = (225,175,222)
Negro = (0,0,0)
Rojo = (193,1,20) 
reloj = pygame.time.Clock()
aux = False
mapa = []
XdeTankA = [0]
XdeTankR = [0]
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
