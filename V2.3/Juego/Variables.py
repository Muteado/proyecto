import pygame
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
###############################################################
#Textos esquinas
ang_ROJO=' '
vel_ROJO=' '
met_ROJO='Rojo'

ang_AZUL=' '
vel_AZUL=' '
met_AZUL='Azul'