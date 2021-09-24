import pygame , sys
import math
import random as r
from pygame import transform
from pygame.locals import *

pygame.init()
largo= 1280
ancho= 600
Pant = pygame.display.set_mode((largo,ancho))
pygame.display.set_caption("The Battle of the Tanks")
Celeste = (54,203,201)

###########################################################
# DESDE AQUI PARA ABAJO HAY QUE TOMAR EN CUENTA EL CODIGO #
###########################################################


class tanque:
    
    def __init__(self):
        # Atributos de instancia
        self.imagen = pygame.image.load("tanquem.png")
        self.imagen = transform.scale(self.imagen,(60,60))
        self.imagen2 = pygame.image.load("tanquem2.png")
        self.imagen2 = transform.scale(self.imagen2,(60,60))
        self.disparos=[]
        self.vida=True

        self.rect=self.imagen.get_rect()
        self.rect.centerx= ancho - 500
        self.rect.centery=420
    

        self.rest=self.imagen2.get_rect()
        self.rest.centerx= ancho+ancho
        self.rest.centery=420


    def dibujartanque(self, Pant):
        Pant.blit(self.imagen,self.rect)
        Pant.blit(self.imagen2,self.rest)
           

            #def dibujarAzul(self,Pant):
                #pass           
                
jugador1= tanque()
    #jugador2= tanque()

while True:
    Pant.fill(Celeste) #Cielo
    jugador1.dibujartanque(Pant)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

   
    pygame.display.flip()