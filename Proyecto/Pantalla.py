import pygame
import random as r
from pygame.locals import *
def main():
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


    #Tanque azul
    '''def TankBlue(d):

        #G=0
        while True:#G!=1
            
           

            if d>=130 and d<=200:
                pass #G=0
            elif d>=330 and d<=500:
                pass #G=0
            else:
                #G=1
                pygame.draw.rect(Pant,Azul,(d,270,30,30))
                break
    '''
    #Tanque rojo
    '''def TankRed(c):
        
        F=0
        while True:#F!=1:
            
            if c>=130 and c<=200:
                pass#F=0
            elif c>=330 and c<=500:
                pass#F=0
            else:
                #F=1
                pygame.draw.rect(Pant,Rojo,(c,270,30,30))
                break
    '''





    #loop principal
    while True:#salir!=True:
        posicion =Pant.get_width()/42


        
        Pant.fill(Celeste) #Cielo

        pygame.draw.rect(Pant,Verde, #Suelo
                        (0,
                        Pant.get_height()/2,
                        Pant.get_width(),
                        Pant.get_height()/2))
    
        pygame.draw.polygon(Pant,Verde, #El poligono mas cercano al azul
                        (((a*posicion)+100,100), #arriba FUNCIONA X,Y
                        ((a*posicion)+200,Pant.get_height()), #derecha
                        ((a*posicion)+100,400), #abajo
                        (a*posicion,Pant.get_height()))) #izquierda

        pygame.draw.polygon(Pant,Verde,
                        (((b*posicion)+100,100), #arriba
                        ((b*posicion)+200,Pant.get_height()), #derecha
                        ((b*posicion)+100,400), #abajo
                        (b*posicion,Pant.get_height()))) #izquierda
        
        pygame.draw.polygon(Pant,Celeste,
                        (((e*posicion)+100,100), #arriba
                        ((e*posicion)+200,Pant.get_height()/2), #derecha
                        ((e*posicion)+100,400), #abajo
                        (e*posicion,Pant.get_height()/2))) #izquierda

        pygame.draw.polygon(Pant,Celeste,
                        (((f*posicion)+100,100), #arriba
                        ((f*posicion)+200,Pant.get_height()/2), #derecha
                        ((f*posicion)+100,400), #abajo
                        (f*posicion,Pant.get_height()/2))) #izquierda
        
        pygame.draw.rect(Pant,Azul,
                        (c*posicion,
                        (Pant.get_height()/2)-30
                        ,30,30)) #TankBlue(d)
        
        pygame.draw.rect(Pant,Rojo,
                        (d*posicion,
                        (Pant.get_height()/2)-30
                        ,30,30)) #TankRed(c)

        pygame.display.update()

        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                #salir=True
                pygame.quit()
            if event.type == VIDEORESIZE:
                Pant = pygame.display.set_mode((event.w, event.h),
                                              pygame.RESIZABLE)





Celeste = (54,203,201)
Verde = (44,177,26)
Rojo = (255, 0, 0)
Azul = (0,0,255)


main()



'''
Circulos pa lo hoyo 
OpenGl
Tile
'''