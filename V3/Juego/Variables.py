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
cmi= random.randint(150,520)
cmd = random.randint(720,1150)
ccd = random.randint(700,1160)
cci = random.randint(110,550)
XdeTankA = random.randint(40,426)
XdeTankR = random.randint(800,1240)
###############################################################
