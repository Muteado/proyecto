import pygame
import sys
import random as r
from pygame.locals import *


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
Rojo = (255, 0, 0) 
Azul = (0,0,255)
AzulClaro = (96,98,253)
Blanco = (255,255,255)
Amarillo = (255, 233, 0)
Negro = (0,0,0)
reloj = pygame.time.Clock()
###############################################################

#Fuentes de las letras para los textos
font = pygame.font.SysFont(None, 80)#Titulos arriba de la pantalla
font2 = pygame.font.SysFont(None, 50)#Nombres botones
font3 = pygame.font.SysFont(None, 23)#Textos pequeños


#Textos esquinas
ang_ROJO=''
vel_ROJO=''
met_ROJO='Rojo'

ang_AZUL='AngAzul'
vel_AZUL=''
met_AZUL='Azul'

#Generador del texto
def draw_text(text, font, color, Pant, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    Pant.blit(textobj, textrect)
 

#Menu principal
def main_menu(Pant,ang_ROJO,vel_ROJO,ang_AZUL,vel_AZUL):
    click = False
    while True:
        #Genera el fondo del juego sin iniciarlo aún
        aux=False
        juego(Pant,aux,ang_ROJO,vel_ROJO,ang_AZUL,vel_AZUL)
        draw_text('Menú', font,Blanco, Pant, (Pant.get_width()/2)-75, 20)
 
        mx, my = pygame.mouse.get_pos()
        boton_1 = pygame.Rect((Pant.get_width()/2)-100, 100, 200, 50)
        boton_2 = pygame.Rect((Pant.get_width()/2)-100, 200, 200, 50)

        if boton_1.collidepoint((mx, my)):
            if click:
                aux=True
                juego(Pant,aux,ang_ROJO,vel_ROJO,ang_AZUL,vel_AZUL)
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
                    aux=True
                    juego(Pant,aux,ang_ROJO,vel_ROJO,ang_AZUL,vel_AZUL)
                    
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
    salir = False
    while pause:
        pauseOpcion = pygame.Rect((Pant.get_width()/2)-100, 100, 200, 70)
        pygame.draw.rect(Pant, Amarillo, pauseOpcion)
        draw_text('Pause', font, Blanco, Pant, (Pant.get_width()/2)-80, 110)
        draw_text('Presione P para volver al juego', font,Blanco,
                  Pant, (Pant.get_width()/4)-100, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                        pause == False
                        salir = True
                        return salir
                if event.key == pygame.K_p:
                        pause = False
                        return salir
        pygame.display.update()
        
def generar_terreno(posicion):
    ##TERRENO##
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

def generar_tanques(posicion):
    pygame.draw.rect(Pant,Azul,
                    (c*posicion,
                    (Pant.get_height()/2)-30
                    ,30,30)) #TankBlue(d)
        
    pygame.draw.rect(Pant,Rojo,
                    (d*posicion,
                    (Pant.get_height()/2)-30
                    ,30,30)) #TankRed(c)

def generar_bloques_esquinas(posIniX,posIniY,largoBloq,altoBloq):
    #BLOQUE AZUL
    pygame.draw.rect(Pant,Negro,
                    (posIniX,
                    posIniY
                    ,largoBloq+2,altoBloq+2))#Angulo N
    pygame.draw.rect(Pant,Azul,
                    (posIniX+1,
                    posIniY+1
                    ,largoBloq,altoBloq))#Angulo B
        
    pygame.draw.rect(Pant,Negro,
                    (posIniX,
                    posIniY+21
                    ,largoBloq+2,altoBloq+2))#Angulo N
    pygame.draw.rect(Pant,Azul,
                    (posIniX+1,
                    posIniY+22
                    ,largoBloq,altoBloq))#Angulo B
        
    pygame.draw.rect(Pant,Negro,
                    (posIniX,
                    posIniY+42
                    ,largoBloq+2,altoBloq+2))#Angulo N
    pygame.draw.rect(Pant,Azul,
                    (posIniX+1,
                    posIniY+43
                    ,largoBloq,altoBloq))#Angulo B
    draw_text('Ángulo : ', font3, Blanco, Pant, posIniX+5, posIniY+1)
    draw_text('Velocidad : ', font3, Blanco, Pant, posIniX+5, posIniY+25)
    draw_text('Metros : ', font3, Blanco, Pant, posIniX+5, posIniY+46)

    #BLOQUE ROJO
    pygame.draw.rect(Pant,Negro,
                    (Pant.get_width()-largoBloq,
                    posIniY
                    ,largoBloq+2,altoBloq+2))#Angulo N
    pygame.draw.rect(Pant,Rojo,
                    (Pant.get_width()-largoBloq+1,
                    posIniY+1
                    ,largoBloq,altoBloq))#Angulo B
        
    pygame.draw.rect(Pant,Negro,
                    (Pant.get_width()-largoBloq,
                    posIniY+21
                    ,largoBloq+2,altoBloq+2))#Angulo N
    pygame.draw.rect(Pant,Rojo,
                    (Pant.get_width()-largoBloq+1,
                    posIniY+22
                    ,largoBloq,altoBloq))#Angulo B
        
    pygame.draw.rect(Pant,Negro,
                    (Pant.get_width()-largoBloq,
                    posIniY+42
                    ,largoBloq+2,altoBloq+2))#Angulo N
    pygame.draw.rect(Pant,Rojo,
                    (Pant.get_width()-largoBloq+1,
                    posIniY+43
                    ,largoBloq,altoBloq))#Angulo B
        
    draw_text('Ángulo : ', font3, Blanco, Pant, Pant.get_width()-largoBloq+5, posIniY+1)
    draw_text('Velocidad : ', font3, Blanco, Pant, Pant.get_width()-largoBloq+5, posIniY+25)
    draw_text('Metros : ', font3, Blanco, Pant, Pant.get_width()-largoBloq+5, posIniY+46)

def texto_esquinas(texto_usuario,rectanguloTXT,color,activo):
    if activo == True:
        color = Rojo
    else:
        color = color
        #print(texto_usuario)
    pygame.draw.rect(Pant,color,rectanguloTXT,2)
    textoenPant = font3.render(texto_usuario,True,Blanco)
    Pant.blit(textoenPant,(rectanguloTXT.x+5,rectanguloTXT.y+5))
    rectanguloTXT.w = textoenPant.get_width()+10
    


def juego(Pant, aux, ang_ROJO,vel_ROJO,ang_AZUL,vel_AZUL):
    #Variables bloques de datos:
    posIniX=0
    posIniY=0
    largoBloq = 200
    altoBloq = 20
    #loop principal
    salir = False
    
    texto_metros = 'Poner metros'
    rectTXT1R= pygame.Rect(Pant.get_width()-largoBloq/2-15, posIniY+1,largoBloq,altoBloq)
    rectTXT2R= pygame.Rect(Pant.get_width()-largoBloq/2-15, posIniY+21,largoBloq+2,altoBloq+2)
    rectTXT3R= pygame.Rect(Pant.get_width()-largoBloq/2-15, posIniY+43,largoBloq,altoBloq)

    rectTXT1A= pygame.Rect(posIniX+largoBloq/2-15, posIniY+1,largoBloq,altoBloq)
    rectTXT2A= pygame.Rect(posIniX+largoBloq/2-15, posIniY+22,largoBloq,altoBloq)
    rectTXT3A= pygame.Rect(posIniX+largoBloq/2-15, posIniY+43,largoBloq,altoBloq)

    color1 = Azul
    color2 = Rojo    
    activo = False
    activo1R = False
    activo2R= False
    activo1A= False
    activo2A = False

    while salir!=True:
        posicion = Pant.get_width()/42
        Pant.fill(Celeste) #Cielo
        generar_terreno(posicion)
        generar_tanques(posicion)
        generar_bloques_esquinas(posIniX,posIniY,largoBloq,altoBloq)
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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if rectTXT1R.collidepoint(event.pos):
                        activo1R = True
                    elif rectTXT2R.collidepoint(event.pos):
                        activo2R = True
                    elif rectTXT1A.collidepoint(event.pos):
                        activo1A= True
                    elif rectTXT2A.collidepoint(event.pos):
                        activo2A = True
                    else:
                        activo1R = False
                        activo2R = False
                        activo1A = False
                        activo2A = False

                if event.type == KEYDOWN:
                    if activo1R == True:
                        if event.key == pygame.K_BACKSPACE:
                            ang_ROJO = ang_ROJO[:-1]
                        else:
                            ang_ROJO += event.unicode
                        ang_ROJO = int(ang_ROJO)
                    if activo2R == True:
                        if event.key == pygame.K_BACKSPACE:
                            vel_ROJO = vel_ROJO[:-1]
                        else:
                            vel_ROJO += event.unicode
                        vel_ROJO = int(vel_ROJO)
                    if activo1A == True:
                        if event.key == pygame.K_BACKSPACE:
                            ang_AZUL = ang_AZUL[:-1]
                        else:
                            ang_AZUL += event.unicode
                        ang_AZUL = int(ang_AZUL)
                    if activo2A == True:
                        if event.key == pygame.K_BACKSPACE:
                            vel_AZUL = vel_AZUL[:-1]
                        else:
                            vel_AZUL += event.unicode
                        vel_AZUL = int(vel_AZUL)
                    if event.key == K_ESCAPE:
                        salir=True
                    if event.key == pygame.K_p:
                        pause = True
                        salir=pausa() 

            angu_ROJO = texto_esquinas(ang_ROJO,rectTXT1R,color1,activo1R)
            velo_ROJO = texto_esquinas(vel_ROJO,rectTXT2R,color1,activo2R)
            #met_ROJO = texto_esquinas(texto_metros,rectTXT3R,color1,activo)

            angu_AZUL = texto_esquinas(ang_AZUL,rectTXT1A,color2,activo1A)
            velo_AZUL = texto_esquinas(vel_AZUL,rectTXT2A,color2,activo2A)
            #met_AZUL = texto_esquinas(texto_metros,rectTXT3A,color2,activo)

            pygame.display.update()
            reloj.tick(60)
            
main_menu(Pant,ang_ROJO,vel_ROJO,ang_AZUL,vel_AZUL)