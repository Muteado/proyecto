import pygame
from pygame import *
from claseEsquinas import DatosEsquinas
from claseTanques import Tanque
from claseTerreno import Terreno
from VS1_1 import Azul, Celeste, Pant, Rojo, aux, Pant


class Juego:
    def juego():
        #Variables bloques de datos:
        posIniX=0
        posIniY=0
        largoBloq = 200
        altoBloq = 20
        texto_metros = 'Poner metros'
        color1 = Azul
        color2 = Rojo    
        activo = False
        activo1R = False
        activo2R= False
        activo1A= False
        activo2A = False
        angulo_ROJO = 0
        velocidad_ROJO = 0
        angulo_AZUL = 0
        velocidad_AZUL = 0
        total = 0
        total2=0
        ##Crea los rectangulos para el ingreso de datos en las esquinas
        rectTXT1R= pygame.Rect(Pant.get_width()-largoBloq/2-15, posIniY+1,largoBloq,altoBloq)
        rectTXT2R= pygame.Rect(Pant.get_width()-largoBloq/2-15, posIniY+21,largoBloq+2,altoBloq+2)
        rectTXT3R= pygame.Rect(Pant.get_width()-largoBloq/2-15, posIniY+43,largoBloq,altoBloq)

        rectTXT1A= pygame.Rect(posIniX+largoBloq/2-15, posIniY+1,largoBloq,altoBloq)
        rectTXT2A= pygame.Rect(posIniX+largoBloq/2-15, posIniY+22,largoBloq,altoBloq)
        rectTXT3A= pygame.Rect(posIniX+largoBloq/2-15, posIniY+43,largoBloq,altoBloq)

        #Auxiliar loop principal
        salir = False
        while salir!=True:
            #Divide la pantalla en 42 partes para posicionar elemntos proporcionalmente
            posicion = Pant.get_width()/42
            Pant.fill(Celeste) #Cielo
            #Genera terreno, tanques y agrega los recuadros de las esquinas
            #Terreno
            #Tanque
            #DatosEsquinas
            #Detecta el valor de la variabel aux, 
            #para poder generar el juego solo como imagen o el juego normal
            if aux == False:
                salir =True
            #Ejecuta el juego con normalidad
            else:
                #For loop detecta eventos
                for event in pygame.event.get():
                    #Detecta cierre de ventana
                    if event.type==pygame.QUIT:
                        #Termina el while y sale del juego
                        salir=True
                        pygame.quit()
                    #Detecta la redimension de la pantalla
                    if event.type == VIDEORESIZE:
                        Pant = pygame.display.set_mode((event.w, event.h),
                                                    pygame.RESIZABLE)
                    #Detecta el click del mouse
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #Detecta click en rectangulo angulo rojo
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




'''def juego(Pant, aux, ang_ROJO,vel_ROJO,ang_AZUL,vel_AZUL):
    rectTXT1R= pygame.Rect(Pant.get_width()-largoBloq/2-15, posIniY+1,largoBloq,altoBloq)
    rectTXT2R= pygame.Rect(Pant.get_width()-largoBloq/2-15, posIniY+21,largoBloq+2,altoBloq+2)
    rectTXT3R= pygame.Rect(Pant.get_width()-largoBloq/2-15, posIniY+43,largoBloq,altoBloq)

    rectTXT1A= pygame.Rect(posIniX+largoBloq/2-15, posIniY+1,largoBloq,altoBloq)
    rectTXT2A= pygame.Rect(posIniX+largoBloq/2-15, posIniY+22,largoBloq,altoBloq)
    rectTXT3A= pygame.Rect(posIniX+largoBloq/2-15, posIniY+43,largoBloq,altoBloq)

    while salir!=True:
        total = str(total)
        total2 = str(total2)
            
        angu_ROJO = texto_esquinas(ang_ROJO,rectTXT1R,color1,activo1R)
        velo_ROJO = texto_esquinas(vel_ROJO,rectTXT2R,color1,activo2R)
        met_ROJO = texto_esquinas(total,rectTXT3R,color1,activo)

        angu_AZUL = texto_esquinas(ang_AZUL,rectTXT1A,color2,activo1A)
        velo_AZUL = texto_esquinas(vel_AZUL,rectTXT2A,color2,activo2A)
        met_AZUL = texto_esquinas(total2,rectTXT3A,color2,activo)
        
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
                        if event.key == K_ESCAPE:
                            salir=True
                        elif event.key == pygame.K_RETURN:
                            activo1R = False
                        elif event.key == pygame.K_BACKSPACE:
                            ang_ROJO = ang_ROJO[:-1]
                        else:
                            ang_ROJO += event.unicode
                        angulo_ROJO = int(ang_ROJO)
                        
                    elif activo2R == True:
                        if event.key == K_ESCAPE:
                            salir=True
                        elif event.key == pygame.K_RETURN:
                            activo2R = False
                        elif event.key == pygame.K_BACKSPACE:
                            vel_ROJO = vel_ROJO[:-1]
                        else:
                            vel_ROJO += event.unicode
                        velocidad_ROJO = int(vel_ROJO)

                        total = calculofuturo(angulo_ROJO, velocidad_ROJO)
                        
                    elif activo1A == True:
                        if event.key == K_ESCAPE:
                            salir=True
                        elif event.key == pygame.K_RETURN:
                            activo1A = False
                        elif event.key == pygame.K_BACKSPACE:
                            ang_AZUL = ang_AZUL[:-1]
                        else:
                            ang_AZUL += event.unicode
                        angulo_AZUL = int(ang_AZUL)
                        
                    elif activo2A == True:
                        if event.key == K_ESCAPE:
                            salir=True
                        elif event.key == pygame.K_RETURN:
                            activo2A = False
                        elif event.key == pygame.K_BACKSPACE:
                            vel_AZUL = vel_AZUL[:-1]
                        else:
                            vel_AZUL += event.unicode
                        velocidad_AZUL = int(vel_AZUL)

                        total2 = calculofuturo(angulo_AZUL, velocidad_AZUL)
                    else:   
                        if event.key == K_ESCAPE:
                            salir=True
                        if event.key == pygame.K_p:
                            pause = True
                            salir=pausa()

            pygame.display.update()
            reloj.tick(60)
'''