import pygame
from pygame import *
import sys
from .ClassTextos import Textos
from .ClassOpciones import OpcionesCat
from .ClassRectangulos import Rectangulos
from .ClassEsquinas import DatosEsquinas
from .claseMovParabolico import *
from .claseTanques import Tanque
from .claseTerreno import Terreno
from .Variables import *
from Juego.ClaseBotones import *

class Juego:
    def juego(Pant,aux,ang_ROJO,vel_ROJO,ang_AZUL,vel_AZUL,mapa):
        #Variables bloques de datos:
        posiniX=0
        posiniY=0
        largoBloq = 200
        altoBloq = 20
        activo1R = False
        activo2R= False
        activo1A= False
        activo2A = False
        a = False
        b = False
        c = False  
        x = 0
        
        mousex1, mousey1 = pygame.mouse.get_pos()

        
        ##Crea los rectangulos para el ingreso de datos en las esquinas
        rectTXT1R = Rectangulos.rectangulo(Pant.get_width()-largoBloq/2-15, posiniY+1,largoBloq,altoBloq)#Angulo rojo
        rectTXT2R = Rectangulos.rectangulo(Pant.get_width()-largoBloq/2-15, posiniY+22,largoBloq,altoBloq)#Velocidad rojo

        rectTXT1A= Rectangulos.rectangulo(posiniX+largoBloq/2-10, posiniY+1,largoBloq,altoBloq)#Angulo azul
        rectTXT2A= Rectangulos.rectangulo(posiniX+largoBloq/2-10, posiniY+22,largoBloq,altoBloq)#Velocidead azul


        #Auxiliar loop principal
        if x == 0:
            Terreno.dibuja_mapa(Pant,mapa)
            DatosEsquinas.generarBloques(posiniX,posiniY,largoBloq,altoBloq)

            DatosEsquinas.textosEsquinas(ang_ROJO,rectTXT1R,Azul,activo1R)
            '''vel_ROJO = '''
            DatosEsquinas.textosEsquinas(vel_ROJO,rectTXT2R,Azul,activo2R)
            
            '''ang_AZUL = '''
            DatosEsquinas.textosEsquinas(ang_AZUL,rectTXT1A,Rojo,activo1A)
            '''vel_AZUL = '''
            DatosEsquinas.textosEsquinas(vel_AZUL,rectTXT2A,Rojo,activo2A)
            

            pygame.display.update()
            Terreno.dibuja_mapa(Pant,mapa)
            DatosEsquinas.generarBloques(posiniX,posiniY,largoBloq,altoBloq)
            x += 1
        salir = False
        while salir!=True:
            DatosEsquinas.generarBloques(posiniX,posiniY,largoBloq,altoBloq) 

            #Cambia el valor de total (total de metros recorridos en el movimiento parabolico), 
            # a caracteres para ser mostrado en pantalla

            
            #Escribe los textos correspondientes a cada bloque de datos
            '''ang_ROJO = '''
            DatosEsquinas.textosEsquinas(ang_ROJO,rectTXT1R,Azul,activo1R)
            '''vel_ROJO = '''
            DatosEsquinas.textosEsquinas(vel_ROJO,rectTXT2R,Azul,activo2R)
            
            '''ang_AZUL = '''
            DatosEsquinas.textosEsquinas(ang_AZUL,rectTXT1A,Rojo,activo1A)
            '''vel_AZUL = '''
            DatosEsquinas.textosEsquinas(vel_AZUL,rectTXT2A,Rojo,activo2A)
            
            #Vida Tanque Azul
            Textos.texto_pantalla_rect(str(vidaAzul[0]),Textos.fuentes(None,23),Negro,Pant,X_Tanque_Azul[0],Y_Tanque_Azul[0]-60)
            #Vida Tanque Rojo
            Textos.texto_pantalla_rect(str(vidaRojo[0]),Textos.fuentes(None,23),Negro,Pant,X_Tanque_Rojo[0],Y_Tanque_Rojo[0]-60)

            if Turno[0] == 1:
                Textos.texto_pantalla_rect(str(c105[0]),Textos.fuentes(None,27),Azul,Pant,610,5)
                Textos.texto_pantalla_rect(str(cperforante[0]),Textos.fuentes(None,27),Azul,Pant,645,5)
                Textos.texto_pantalla_rect(str(c60[0]),Textos.fuentes(None,27),Azul,Pant,680,5)
                
            if Turno[0] == 2:
                Textos.texto_pantalla_rect(str(c105[1]),Textos.fuentes(None,27),Rojo,Pant,610,5)
                Textos.texto_pantalla_rect(str(cperforante[1]),Textos.fuentes(None,27),Rojo,Pant,645,5)
                Textos.texto_pantalla_rect(str(c60[1]),Textos.fuentes(None,27),Rojo,Pant,680,5)
            pygame.display.update()

            #Detecta el valor de la variabel aux, 
            #para poder generar el juego solo como imagen o el juego normal
            if aux == False:
                salir =True
            #Ejecuta el juego con normalidad
            else:
                #For loop detecta eventos
                if Partida[0] == 0:
                    for event in pygame.event.get():
                        #Detecta cierre de ventana
                        if event.type==pygame.QUIT:
                            #Termina el while y sale del juego
                            salir=True
                            pygame.quit()
                        #Detecta la redimenNoneon de la pantalla
                        if event.type == VIDEORESIZE:
                            Pant = pygame.display.set_mode((event.w, event.h),
                                                        pygame.RESIZABLE)
                        #Detecta el click del mouse
                        if event.type == pygame.MOUSEBUTTONDOWN:

                            if Turno[0] == 1:
                                #Detecta click en rectangulo angulo azul
                                if rectTXT1A.collidepoint(event.pos):
                                    activo1A= True
                                    activo2A = False
                                    Angulo_Azul[0] = ''
                                #Detecta click en rectangulo velocidad azul
                                elif rectTXT2A.collidepoint(event.pos):
                                    activo2A = True
                                    activo1A = False

                                elif rectTXT1R.collidepoint(event.pos):
                                    print("No se puede, no es su turno")
                                #Detecta click en rectangulo velocidad azul
                                elif rectTXT2R.collidepoint(event.pos):
                                    print("No se puede, no es su turno")
                                #Devuelve el valor falso a las variables en caso de no ser clickeadas
                                elif botonamarillo1.collidepoint(event.pos):
                                    if c105[0] > 0:
                                        a = True
                                        b = False
                                        c = False
                                    
                                    else:
                                        print("No te quedan balas! aaaa")
                                        a = False
                                        b = False
                                        c = False 
                                elif botonnaranja1.collidepoint(event.pos):
                                    if cperforante[0] > 0:
                                        a = False
                                        b = True
                                        c = False

                                    else:
                                        print("No te quedan balas! bbbb")
                                        a = False
                                        b = False
                                        c = False 

                                elif botonmorado1.collidepoint(event.pos):
                                    if c60[0] > 0:
                                        a = False
                                        b = False
                                        c = True

                                    else:
                                        print("No te quedan balas! cccc")
                                        a = False
                                        b = False
                                        c = False 
                                else:
                                    activo1R = False
                                    activo2R = False
                                    activo1A = False
                                    activo2A = False

                            elif Turno[0] == 2:
                                #Detecta click en rectangulo angulo rojo
                                if rectTXT1R.collidepoint(event.pos):
                                    activo1R = True
                                    activo2R = False
                                #Detecta click en rectangulo velocidad rojo
                                elif rectTXT2R.collidepoint(event.pos):
                                    activo2R = True
                                    activo1R = False

                                elif rectTXT1A.collidepoint(event.pos):
                                    print("No se puede, no es su turno")
                                #Detecta click en rectangulo velocidad azul
                                elif rectTXT2A.collidepoint(event.pos):
                                    print("No se puede, no es su turno")
                                #Devuelve el valor falso a las variables en caso de no ser clickeadas
                                elif botonamarillo1.collidepoint(event.pos):
                                    if c105[1] > 0:
                                        a = True
                                        b = False
                                        c = False
                                    
                                    else:
                                        print("No te quedan balas! aaaa")
                                        a = False
                                        b = False
                                        c = False 
                                elif botonnaranja1.collidepoint(event.pos):
                                    if cperforante[1] > 0:
                                        a = False
                                        b = True
                                        c = False

                                    else: 
                                        print("No te quedan balas! aaaa")
                                        a = False
                                        b = False
                                        c = False 

                                elif botonmorado1.collidepoint(event.pos):
                                    if c60[1] > 0:
                                        a = False
                                        b = False
                                        c = True
                                    else:
                                        print("No te quedan balas! bbbb")
                                        a = False
                                        b = False
                                        c = False 
                                else:
                                    activo1R = False
                                    activo2R = False
                                    activo1A = False
                                    activo2A = False

                            
                            
                        #Detecta el teclado
                        if event.type == pygame.KEYDOWN:
                               
                            if Turno[0] == 1:
                            #None se clickeo el rectangulo del angulo azul se activa 
                            # la opción para el ingreso de datos
                                if activo1A == True:
                                    #Detecta la tecla escape para volver al menú
                                    if event.key == K_ESCAPE:
                                        salir=True
                                    #Detecta la telca enter para terminar el ingreso de datos
                                    elif event.key == pygame.K_RETURN:
                                        pygame.display.update()
                                        activo1A = False
                                    #Detecta la tecla retroceso para borrar
                                    # en caso de ser necesario
                                    elif event.key == pygame.K_BACKSPACE:
                                        #Borra un elemento a la vez de los datos ingresados por el ususario 
                                        # en el apartado de angulo azul, al borrar todos los datos el programa cae
                                        ang_AZUL = ang_AZUL[:-1]
                                        DatosEsquinas.generarBloques(posiniX,posiniY,largoBloq,altoBloq)
                                    #En caso de no borrar datos estará constantemente ingresando 
                                    # todas las teclas preNoneonadas en el teclado
                                    elif pygame.K_0 <= event.key <= pygame.K_9:
                                        #Actualiza la variable para el unicode
                                        ang_AZUL=str(ang_AZUL)
                                        #Funciona como un input caracter por caracter, 
                                        # permite ingresar todo tipo de caracter
                                        ang_AZUL += event.unicode

                                        Angulo_Azul[0] = int(ang_AZUL)
                                        #met_AZUL = Textos.texto_pantalla_rect(total2,Textos.fuentes(None,23),Blanco,Pant,rectTXT3A.x,rectTXT3A.y+5)
                                    #Transforma lo ingresado en el unicode en un entero, 
                                    # en caso de ingresar texto (letras o Nonembolos) el programa cae
                                    
                                
                                
                                #None se clickeo el rectangulo del velocidad azul se activa 
                                # la opción para el ingreso de datos   
                                if activo2A == True:
                                    #Detecta la tecla escape para volver al menú
                                    if event.key == K_ESCAPE:
                                        salir=True
                                    #Detecta la telca enter para terminar el ingreso de datos
                                    elif event.key == pygame.K_RETURN:
                                        pygame.display.update()
                                        activo2A = False
                                    #Detecta la tecla retroceso para borrar
                                    # en caso de ser necesario
                                    elif event.key == pygame.K_BACKSPACE:
                                        #Borra un elemento a la vez de los datos ingresados por el ususario 
                                        # en el apartado de angulo azul, al borrar todos los datos el programa cae
                                        vel_AZUL = vel_AZUL[:-1]
                                        DatosEsquinas.generarBloques(posiniX,posiniY,largoBloq,altoBloq)
                                    #En caso de no borrar datos estará constantemente ingresando 
                                    # todas las teclas preNoneonadas en el teclado
                                    
                                    elif pygame.K_0 <= event.key <= pygame.K_9:
                                        #Actualiza la variable para el unicode
                                        vel_AZUL=str(vel_AZUL)
                                        #Funciona como un input caracter por caracter, 
                                        # permite ingresar todo tipo de caracter
                                        vel_AZUL += event.unicode

                                        Velocidad_Azul[0] = int(vel_AZUL)
                                        #met_AZUL = Textos.texto_pantalla_rect(total2,Textos.fuentes(None,23),Blanco,Pant,rectTXT3A.x,rectTXT3A.y+5)
                                    #Transforma lo ingresado en el unicode en un entero, 
                                    # en caso de ingresar texto (letras o Nonembolos) el programa cae
                                    
                                    
                                    #Ejecuta la función para calcular el movimiento parabolico, 
                                    # funciona una vez que el usuario ingresa la velocidad
                                
                            
                                if event.key == K_SPACE:
                                    if a == True or b == True or c == True:
                                        if Velocidad_Azul[0] != str and Angulo_Azul[0] != str:
                                            if Velocidad_Azul[0] > 0 and Velocidad_Azul[0] < 201:
                                                    if Angulo_Azul[0] >= 0 and Angulo_Azul[0] <= 180:
                                                        aux = True
                                                        Proyectil.lanzamiento(a,b,c,aux)
                                                        vel_AZUL = ''
                                                        ang_AZUL = ''
                                                        Angulo_Azul[0] = '0'
                                                        Velocidad_Azul[0] = '0'
                                                        a = False
                                                        b = False
                                                        c = False
                                                    else:
                                                        vel_AZUL = ''
                                                        ang_AZUL = ''
                                                        Angulo_Azul[0] = '0'
                                                        Velocidad_Azul[0] = '0'
                                                    
                                            else:
                                                vel_AZUL = ''
                                                ang_AZUL = ''
                                                Angulo_Azul[0] = '0'
                                                Velocidad_Azul[0] = '0'
                                        else:
                                            vel_AZUL = ''
                                            ang_AZUL = ''
                                            Angulo_Azul[0] = '0'
                                            Velocidad_Azul[0] = '0'
                                    else:
                                        a = False
                                        b = False
                                        c = False
                                        print("por favor elija el color y luego presione espacio")


                                
                                #Otras teclas detectadas
                                else:
                                    #Detecta la tecla escape para volver al menú
                                    if event.key == K_ESCAPE:
                                        salir=True
                                    #Detecta la tecla p para poner en pausa el juego
                                    if event.key == pygame.K_p:
                                        pause = True
                                        salir=OpcionesCat.pausa()

                            elif Turno[0] == 2:
                                #None se clickeo el rectangulo del angulo rojo se activa 
                                # la opción para el ingreso de datos
                                if activo1R == True:
                                    #Detecta la tecla escape para volver al menú
                                    if event.key == K_ESCAPE:
                                        salir=True
                                    #Detecta la telca enter para terminar el ingreso de datos
                                    elif event.key == pygame.K_RETURN:
                                        pygame.display.update()
                                        activo1R = False

                                    #Detecta la tecla retroceso para borrar
                                    # en caso de ser necesario
                                    elif event.key == pygame.K_BACKSPACE:
                                        #Borra un elemento a la vez de los datos ingresados por el ususario 
                                        # en el apartado de angulo rojo, al borrar todos los datos el programa cae
                                        ang_ROJO = ang_ROJO[:-1]
                                        DatosEsquinas.generarBloques(posiniX,posiniY,largoBloq,altoBloq)
                                    #En caso de no borrar datos estará constantemente ingresando 
                                    # todas las teclas preNoneonadas en el teclado
                                    elif pygame.K_0 <= event.key <= pygame.K_9:
                                        #Actualiza la variable para el unicode
                                        
                                        ang_ROJO=str(ang_ROJO)
                                        #Funciona como un input caracter por caracter, 
                                        # permite ingresar todo tipo de caracter
                                        ang_ROJO += event.unicode
                                        Angulo_Rojo[0] = int(ang_ROJO)
                                        
                                        
                                        #met_ROJO = Textos.texto_pantalla_rect(total,Textos.fuentes(None,23),Blanco,Pant,rectTXT3R.x,rectTXT3R.y+5)

                                    
                                    #Transforma lo ingresado en el unicode en un entero, 
                                    # en caso de ingresar texto (letras o Nonembolos) el programa cae

                                    
                                #None se clickeo el rectangulo del velocidad rojo se activa 
                                # la opción para el ingreso de datos   
                                elif activo2R == True:
                                    #Detecta la tecla escape para volver al menú
                                    if event.key == K_ESCAPE:
                                        salir=True
                                    #Detecta la telca enter para terminar el ingreso de datos
                                    elif event.key == pygame.K_RETURN:
                                        pygame.display.update()
                                        activo2R = False
                                    #Detecta la tecla retroceso para borrar
                                    # en caso de ser necesario
                                    elif event.key == pygame.K_BACKSPACE:
                                        #Borra un elemento a la vez de los datos ingresados por el ususario 
                                        # en el apartado de velocidad rojo, al borrar todos los datos el programa cae
                                        vel_ROJO = vel_ROJO[:-1]
                                        DatosEsquinas.generarBloques(posiniX,posiniY,largoBloq,altoBloq)
                                    #En caso de no borrar datos estará constantemente ingresando 
                                    # todas las teclas preNoneonadas en el teclado
                                    elif pygame.K_0 <= event.key <= pygame.K_9:
                                        #Actualiza la variable para el unicode
                                        vel_ROJO=str(vel_ROJO)
                                        #Funciona como un input caracter por caracter, 
                                        # permite ingresar todo tipo de caracter
                                        
                                        vel_ROJO += event.unicode

                                        Velocidad_Rojo[0] = int(vel_ROJO)
                                        #met_ROJO = Textos.texto_pantalla_rect(total,Textos.fuentes(None,23),Blanco,Pant,rectTXT3R.x,rectTXT3R.y+5)

                                    #Transforma lo ingresado en el unicode en un entero, 
                                    # en caso de ingresar texto (letras o Nonembolos) el programa cae
                                elif event.key == K_SPACE:
                                    if a == True or b == True or c == True:
                                        if Velocidad_Rojo[0] != str and Angulo_Rojo[0] != str:
                                            if Velocidad_Rojo[0] > 0 and Velocidad_Rojo[0] < 201:
                                                if Angulo_Rojo[0] > 0 and Angulo_Rojo[0] < 181:
                                                    aux = True
                                                    Proyectil.lanzamiento(a,b,c,aux)
                                                    vel_ROJO = ''
                                                    ang_ROJO = ''
                                                    Angulo_Rojo[0] = '0'
                                                    Velocidad_Rojo[0] = '0'
                                                    break
                                                else:
                                                    vel_ROJO = ''
                                                    ang_ROJO = ''
                                                    Angulo_Rojo[0] = '0'
                                                    Velocidad_Rojo[0] = '0'
                                                
                                            else:
                                                vel_ROJO = ''
                                                ang_ROJO = ''
                                                Angulo_Rojo[0] = '0'
                                                Velocidad_Rojo[0] = '0'
                                        else:
                                            vel_ROJO = ''
                                            ang_ROJO = ''
                                            Angulo_Rojo[0] = '0'
                                            Velocidad_Rojo[0] = '0'
                                    else:
                                        a = False
                                        b = False
                                        c = False
                                        print("por favor elija el color y luego presione espacio")

                                
                                
                                #Otras teclas detectadas
                                else:
                                    #Detecta la tecla escape para volver al menú
                                    if event.key == K_ESCAPE:
                                        salir=True
                                    #Detecta la tecla p para poner en pausa el juego
                                    if event.key == pygame.K_p:
                                        pause = True
                                        salir=OpcionesCat.pausa()

                
                if Partida[0] == 1:
                    pygame.display.update()
                    print("Ganó el Rojo")
                    pygame.time.delay(5000)
                    salir=True
                    
                elif Partida[0] == 2:
                    pygame.display.update()
                    print("Ganó el Azul")
                    pygame.time.delay(5000)
                    salir=True
                    
                #Actualiza la pantalla
            
                #reloj.tick(60)