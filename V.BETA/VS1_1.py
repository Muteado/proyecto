import pygame
import sys
import random as r
from pygame.locals import *
from math import *


###############################################################
                        ##VARIABLES##
largo= 1280
ancho= 600
pygame.init()
Pant = pygame.display.set_mode([largo,ancho], pygame.RESIZABLE)
pygame.display.set_caption("The Battle of the Tanks")
a = r.randint(2,21) #PUNTA IZQUIERDA
b = r.randint(21,40) #PUNTA DERECHA
c = r.randint(2,14) #Determina la posicion del tanque AZUL
d = r.randint(28,40) #Determina la posicion del tanque ROJO
e = r.randint(2,21) #CAÑON IZQUIERDO
f = r.randint(21,40) #CAÑON DERECHO
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
ang_ROJO=''
vel_ROJO=''
met_ROJO='Rojo'

ang_AZUL=''
vel_AZUL=''
met_AZUL='Azul'


def calculofuturo(β, vi):
    om=((β*pi)/180) #Angulo de disparo multiplicado por pi y dividido en 180 que es el angulo de disparo
    #g=9.81 # m/s**2 #gravedad de la tierra
    a=tan(om) #tangente del angulo ingresado
    b=((9.81)/((2*vi**2)*cos(om)**2)) #formula que usa la gravedad, velocidad inicial ingresada y el angulo de inicio que ingresamos
    ymax=(vi**2)*(sin(om)*sin(om))/(2*9.81) # el movimiento que hace la bala, esto marca el punto maximo que alcanza el disparo
    xmax=(vi**2)*(sin(2*om))//(9.81) # La distancia maxima que hace la bala al usar la velocidad y el angulo inicial
    tmax=(vi*sin(om))/(9.81) # tiempo que tarda la bala en llegar al punto mas alto
    tv=2*(tmax)
    return xmax
    




            
#main_menu(Pant,ang_ROJO,vel_ROJO,ang_AZUL,vel_AZUL)
