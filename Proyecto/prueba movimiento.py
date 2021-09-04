import pygame
import sys
import random as r
from pygame.locals import *
from math import *

pygame.init()

largo=1280
ancho=600

#colores
negro= (0,0,0)
blanco= (255,255,255)
#ventana
ventana=pygame.display.set_mode((largo,ancho))
#variables

pox = 250 #posicion de partida de la bala en X
poy = 500 #posicion de partida de la bala en Y


#ciclo magno
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.type == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    
    #ordenes a la bala
    pox+=1
    poy-=1
    alturabala=40
    distanciabala=163
    if pox>largo:
        pox=0
    if poy>=ancho:
        poy=0#Funciona en diagonal
    
    #Implementar que la bola suba hasta alturabala y despues baje


    

    '''elif poy>=alturabala:
        poy-=1
        pox+=1
        if pox>=distanciabala:
            pox=0
    '''

    #se rellena la ventana
    ventana.fill(negro)
    pygame.draw.circle(ventana,blanco,
                        (pox,poy),10,10)
    
    #actualizacion de pantalla
    pygame.display.update()
    pygame.time.delay(7)

pygame.quit()