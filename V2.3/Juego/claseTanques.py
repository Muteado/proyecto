import pygame
import random as r
from .Variables import Azul, Rojo, Pant


class Tanque:
    c = r.randint(2,14) #Determina la posicion del tanque AZUL
    d = r.randint(28,40) #Determina la posicion del tanque ROJO
    def generar_tanques(posicion):
        pygame.draw.rect(Pant,Azul,
                        (Tanque.c*posicion,
                        (Pant.get_height()/2)-30
                        ,30,30)) #TankBlue(d)
            
        pygame.draw.rect(Pant,Rojo,
                        (Tanque.d*posicion,
                        (Pant.get_height()/2)-30
                        ,30,30)) #TankRed(c)
