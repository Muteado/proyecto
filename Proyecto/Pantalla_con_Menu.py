import pygame
import sys
import random as r
from pygame.locals import *


#Variables
###############################################################
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
Rojo = (255, 0, 0) 
Azul = (0,0,255)
Blanco = (255,255,255)
Amarillo = (255, 233, 0)
###############################################################

#Fuentes de las letras para el menu
font = pygame.font.SysFont(None, 80)
font2 = pygame.font.SysFont(None, 50)


def draw_text(text, font, color, Pant, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    Pant.blit(textobj, textrect)
 


def main_menu(Pant):
    click = False
    while True:
        juego(Pant,aux=False)
        #Pant.fill(Celeste)
        draw_text('Menú', font,Blanco, Pant, (Pant.get_width()/2)-75, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        boton_1 = pygame.Rect((Pant.get_width()/2)-100, 100, 200, 50)
        
        boton_2 = pygame.Rect((Pant.get_width()/2)-100, 200, 200, 50)
        if boton_1.collidepoint((mx, my)):
            if click:
                juego(Pant,aux=True)
        if boton_2.collidepoint((mx, my)):
            if click:
                opciones()
        pygame.draw.rect(Pant, Amarillo, boton_1)
        draw_text('JUEGO', font2, Blanco, Pant, (Pant.get_width()/2)-60, 110)
        pygame.draw.rect(Pant, Amarillo, boton_2)
        draw_text('OPCIONES', font2, Blanco, Pant, (Pant.get_width()/2)-90, 210)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    juego(Pant,aux=True)
                    
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        
 


def opciones():
    running = True
    click = False
    while running:
        rectOpciones= pygame.Rect((Pant.get_width()/2)-125, 20, 300, 60)
        pygame.draw.rect(Pant, Celeste, rectOpciones)
        draw_text('Opciones', font, (255, 255, 255), Pant, (Pant.get_width()/2)-125, 20)
        boton_1_aux= pygame.Rect((Pant.get_width()/2)-100, 100, 200, 50)
        pygame.draw.rect(Pant, Amarillo, boton_1_aux)
        draw_text('SALIR', font2, Blanco, Pant, (Pant.get_width()/2)-60, 110)
        mx, my = pygame.mouse.get_pos()
        if boton_1_aux.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
                
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()

def pausa():
    pause = True
    while pause:
        pauseOpcion = pygame.Rect((Pant.get_width()/2)-100, 100, 200, 70)
        pygame.draw.rect(Pant, Amarillo, pauseOpcion)
        draw_text('Pause', font, Blanco, Pant, (Pant.get_width()/2)-80, 110)
        draw_text('Presione P para volver al juego', font, Blanco,
                  Pant, (Pant.get_width()/4)-100, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                        pause = False 
        pygame.display.update()
        

def juego(Pant, aux):
    
    #loop principal
    salir = False
    while salir!=True:
        posicion = Pant.get_width()/42
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
                        (((e*posicion)+100,Pant.get_height()/2), #arriba
                        ((e*posicion)+200,Pant.get_height()/2), #derecha
                        ((e*posicion)+100,400), #abajo
                        (e*posicion,Pant.get_height()/2))) #izquierda

        pygame.draw.polygon(Pant,Celeste,
                        (((f*posicion)+100,Pant.get_height()/2), #arriba
                        ((f*posicion)+200,Pant.get_height()/2), #derecha
                        ((f*posicion)+100,400), #abajo
                        (f*posicion,Pant.get_height()/2))) #izquierda
        

        '''pygame.draw.rect(Pant,Azul,
                        (c*posicion,
                        (Pant.get_height()/2)-30
                        ,30,30)) #TankBlue(d)'''

        pygame.draw.circle(Pant,Azul,
                          (c*posicion,
                          (Pant.get_height()/2)-17)
                          ,17,17) #TankBlue(d)
        


        '''pygame.draw.rect(Pant,Rojo,
                        (d*posicion,
                        (Pant.get_height()/2)-30
                        ,30,30)) #TankRed(c)'''

        pygame.draw.circle(Pant,Rojo,
                          (d*posicion,
                          (Pant.get_height()/2)-17)
                          ,17,17) #TankRed(c)
        

        if aux == False:
            salir =True
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    salir=True
                    pygame.quit()
                if event.type == VIDEORESIZE:
                    Pant = pygame.display.set_mode((event.w, event.h),
                                                  pygame.RESIZABLE)
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        print ("escape")
                        salir=True
                    if event.key == pygame.K_p:
                            pause = True
                            pausa()
                            print('pico')
            pygame.display.update()


main_menu(Pant)



'''
OpenGl
Tile
'''
