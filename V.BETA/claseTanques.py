import pygame
from VS1_1 import Azul, Rojo, Pant,c,d


class Tanque:
    def __init__(self, Pantalla, color, x , y, alto, largo):
        #Posibles atributos del constructor
        #self.pant = Pantalla
        self.color =  color
        self.x = x
        self.y = y
        self.alto = alto
        self.largo = largo
    
    #Posibles metodos
    #Color???
    def colorTanque(self):
        if self.color == Rojo:
            return Rojo
        else:
            return Azul
        
    def movimiento(self):
        #Esto es en caso de aplicar los movimientos asi
        self.x+=1
        self.y+=1


def generar_tanques(posicion):
    pygame.draw.rect(Pant,Azul,
                    (c*posicion,
                    (Pant.get_height()/2)-30
                    ,30,30)) #TankBlue(d)
        
    pygame.draw.rect(Pant,Rojo,
                    (d*posicion,
                    (Pant.get_height()/2)-30
                    ,30,30)) #TankRed(c)
