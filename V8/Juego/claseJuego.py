import pygame
from pygame import *
import sys
from .ClassTextos import Textos
from .ClassOpciones import OpcionesCat
from .ClassRectangulos import Rectangulos
from .ClassEsquinas import DatosEsquinas
from .claseMovParabolico import Proyectil
from .claseTanques import Tanque
from .claseTerreno import Terreno
from .Variables import Azul, Blanco, Celeste, Rojo, Turno, Partida, Angulo_Azul, Angulo_Rojo, Velocidad_Rojo, Velocidad_Azul


class Juego:
    def juego(Pant,aux,ang_ROJO,vel_ROJO,ang_AZUL,vel_AZUL,mapa):
        #Variables bloques de datos:
        posIniX=0
        posIniY=0
        largoBloq = 200
        altoBloq = 20
        activo1R = False
        activo2R= False
        activo1A= False
        activo2A = False
        x = 0
        si = ''
        
        total = 0
        total2 = 0
        
        
        ##Crea los rectangulos para el ingreso de datos en las esquinas
        rectTXT1R = Rectangulos.rectangulo(Pant.get_width()-largoBloq/2-15, posIniY+1,largoBloq,altoBloq)#Angulo rojo
        rectTXT2R = Rectangulos.rectangulo(Pant.get_width()-largoBloq/2-15, posIniY+22,largoBloq,altoBloq)#Velocidad rojo
        rectTXT3R = Rectangulos.rectangulo(Pant.get_width()-largoBloq/2-15, posIniY+43,largoBloq,altoBloq)#Metros rojo

        rectTXT1A= Rectangulos.rectangulo(posIniX+largoBloq/2-15, posIniY+1,largoBloq,altoBloq)#Angulo azul
        rectTXT2A= Rectangulos.rectangulo(posIniX+largoBloq/2-15, posIniY+22,largoBloq,altoBloq)#Velocidead azul
        rectTXT3A= Rectangulos.rectangulo(posIniX+largoBloq/2-15, posIniY+43,largoBloq,altoBloq)#Metros azul

        #Auxiliar loop principal
        if x == 0:
            Terreno.dibuja_mapa(Pant,mapa)
            DatosEsquinas.generarBloques(posIniX,posIniY,largoBloq,altoBloq)
            total = str(total)
            total2 = str(total2)

            DatosEsquinas.textosEsquinas(ang_ROJO,rectTXT1R,Azul,activo1R)
            '''vel_ROJO = '''
            DatosEsquinas.textosEsquinas(vel_ROJO,rectTXT2R,Azul,activo2R)
            met_ROJO = Textos.texto_pantalla_rect(total,Textos.fuentes(si,23),Blanco,Pant,rectTXT3R.x,rectTXT3R.y+5)
            
            '''ang_AZUL = '''
            DatosEsquinas.textosEsquinas(ang_AZUL,rectTXT1A,Rojo,activo1A)
            '''vel_AZUL = '''
            DatosEsquinas.textosEsquinas(vel_AZUL,rectTXT2A,Rojo,activo2A)
            met_AZUL = Textos.texto_pantalla_rect(total2,Textos.fuentes(si,23),Blanco,Pant,rectTXT3A.x,rectTXT3A.y+5)
            

            pygame.display.update()
            Terreno.dibuja_mapa(Pant,mapa)
            DatosEsquinas.generarBloques(posIniX,posIniY,largoBloq,altoBloq)
            x += 1
        salir = False
        while salir!=True:
            #Divide la pantalla en 42 partes para posicionar elemntos proporcionalmente
            #Pant.fill(Celeste) #Cielo
            #Genera terreno, tanques y agrega los recuadros de las esquinas
            
            

            #Cambia el valor de total (total de metros recorridos en el movimiento parabolico), 
            # a caracteres para ser mostrado en pantalla
            total = str(total)
            total2 = str(total2)

            
            #Escribe los textos correspondientes a cada bloque de datos
            '''ang_ROJO = '''
            DatosEsquinas.textosEsquinas(ang_ROJO,rectTXT1R,Azul,activo1R)
            '''vel_ROJO = '''
            DatosEsquinas.textosEsquinas(vel_ROJO,rectTXT2R,Azul,activo2R)
            met_ROJO = Textos.texto_pantalla_rect(total,Textos.fuentes(si,23),Blanco,Pant,rectTXT3R.x,rectTXT3R.y+5)
            
            '''ang_AZUL = '''
            DatosEsquinas.textosEsquinas(ang_AZUL,rectTXT1A,Rojo,activo1A)
            '''vel_AZUL = '''
            DatosEsquinas.textosEsquinas(vel_AZUL,rectTXT2A,Rojo,activo2A)
            met_AZUL = Textos.texto_pantalla_rect(total2,Textos.fuentes(si,23),Blanco,Pant,rectTXT3A.x,rectTXT3A.y+5)
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
                        #Detecta la redimension de la pantalla
                        if event.type == VIDEORESIZE:
                            Pant = pygame.display.set_mode((event.w, event.h),
                                                        pygame.RESIZABLE)
                        #Detecta el click del mouse
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if Turno[0] == 2:
                                #Detecta click en rectangulo angulo rojo
                                if rectTXT1R.collidepoint(event.pos):
                                    activo1R = True
                                #Detecta click en rectangulo velocidad rojo
                                elif rectTXT2R.collidepoint(event.pos):
                                    activo2R = True

                                elif rectTXT1A.collidepoint(event.pos):
                                    print("No se puede, no es su turno")
                                #Detecta click en rectangulo velocidad azul
                                elif rectTXT2A.collidepoint(event.pos):
                                    print("No se puede, no es su turno")
                                #Devuelve el valor falso a las variables en caso de no ser clickeadas
                                else:
                                    activo1R = False
                                    activo2R = False
                                    activo1A = False
                                    activo2A = False
                            elif Turno[0] == 1:
                                #Detecta click en rectangulo angulo azul
                                if rectTXT1A.collidepoint(event.pos):
                                    activo1A= True
                                #Detecta click en rectangulo velocidad azul
                                elif rectTXT2A.collidepoint(event.pos):
                                    activo2A = True

                                elif rectTXT1R.collidepoint(event.pos):
                                    print("No se puede, no es su turno")
                                #Detecta click en rectangulo velocidad azul
                                elif rectTXT2R.collidepoint(event.pos):
                                    print("No se puede, no es su turno")
                                #Devuelve el valor falso a las variables en caso de no ser clickeadas
                                else:
                                    activo1R = False
                                    activo2R = False
                                    activo1A = False
                                    activo2A = False
                            
                        #Detecta el teclado
                        if event.type == KEYDOWN:
                            if Turno[0] == 2:
                                #Si se clickeo el rectangulo del angulo rojo se activa 
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
                                    #En caso de no borrar datos estará constantemente ingresando 
                                    # todas las teclas presionadas en el teclado
                                    else:
                                        #Actualiza la variable para el unicode
                                        
                                        ang_ROJO=str(ang_ROJO)
                                        #Funciona como un input caracter por caracter, 
                                        # permite ingresar todo tipo de caracter
                                        ang_ROJO += event.unicode
                                        Angulo_Rojo[0] = int(ang_ROJO)
                                        
                                        met_ROJO = Textos.texto_pantalla_rect(total,Textos.fuentes(si,23),Blanco,Pant,rectTXT3R.x,rectTXT3R.y+5)

                                    
                                    #Transforma lo ingresado en el unicode en un entero, 
                                    # en caso de ingresar texto (letras o simbolos) el programa cae

                                    
                                #Si se clickeo el rectangulo del velocidad rojo se activa 
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
                                    #En caso de no borrar datos estará constantemente ingresando 
                                    # todas las teclas presionadas en el teclado
                                    else:
                                        #Actualiza la variable para el unicode
                                        vel_ROJO=str(vel_ROJO)
                                        #Funciona como un input caracter por caracter, 
                                        # permite ingresar todo tipo de caracter
                                        vel_ROJO += event.unicode

                                        Velocidad_Rojo[0] = int(vel_ROJO)
                                        met_ROJO = Textos.texto_pantalla_rect(total,Textos.fuentes(si,23),Blanco,Pant,rectTXT3R.x,rectTXT3R.y+5)

                                    #Transforma lo ingresado en el unicode en un entero, 
                                    # en caso de ingresar texto (letras o simbolos) el programa cae
                                elif event.key == K_SPACE:
                                    if Velocidad_Rojo[0] != str and Angulo_Rojo[0] != int:
                                            if Velocidad_Rojo[0] > 0 and Velocidad_Rojo[0] < 201:
                                                if Angulo_Rojo[0] > 0 and Angulo_Rojo[0] < 181:
                                                    aux = True
                                                    salir=Proyectil.lanzamiento(aux)
                                                    Velocidad_Rojo[0] = 0
                                                    Angulo_Rojo[0] = 0
                                                    vel_ROJO = ''
                                                    ang_ROJO = ''
                                                else:
                                                    Velocidad_Rojo[0] = 0
                                                    Angulo_Rojo[0] = 0
                                                    vel_ROJO = ''
                                                    ang_ROJO = ''
                                                
                                            else:
                                                Velocidad_Rojo[0] = 0
                                                Angulo_Rojo[0] = 0
                                                vel_ROJO = ''
                                                ang_ROJO = ''
                                    else:
                                        Velocidad_Rojo[0] = 0
                                        Angulo_Rojo[0] = 0
                                        vel_ROJO = ''
                                        ang_ROJO = ''

                                
                                
                                #Otras teclas detectadas
                                else:
                                    #Detecta la tecla escape para volver al menú
                                    if event.key == K_ESCAPE:
                                        salir=True
                                    #Detecta la tecla p para poner en pausa el juego
                                    if event.key == pygame.K_p:
                                        pause = True
                                        salir=OpcionesCat.pausa()
                                
                            elif Turno[0] == 1:
                            #Si se clickeo el rectangulo del angulo azul se activa 
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
                                    #En caso de no borrar datos estará constantemente ingresando 
                                    # todas las teclas presionadas en el teclado
                                    else:
                                        #Actualiza la variable para el unicode
                                        ang_AZUL=str(ang_AZUL)
                                        #Funciona como un input caracter por caracter, 
                                        # permite ingresar todo tipo de caracter
                                        ang_AZUL += event.unicode

                                        Angulo_Azul[0] = int(ang_AZUL)
                                        met_AZUL = Textos.texto_pantalla_rect(total2,Textos.fuentes(si,23),Blanco,Pant,rectTXT3A.x,rectTXT3A.y+5)
                                    #Transforma lo ingresado en el unicode en un entero, 
                                    # en caso de ingresar texto (letras o simbolos) el programa cae
                                    
                                
                                
                                #Si se clickeo el rectangulo del velocidad azul se activa 
                                # la opción para el ingreso de datos   
                                elif activo2A == True:
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
                                    #En caso de no borrar datos estará constantemente ingresando 
                                    # todas las teclas presionadas en el teclado
                                    
                                    else:
                                        #Actualiza la variable para el unicode
                                        vel_AZUL=str(vel_AZUL)
                                        #Funciona como un input caracter por caracter, 
                                        # permite ingresar todo tipo de caracter
                                        vel_AZUL += event.unicode

                                        Velocidad_Azul[0] = int(vel_AZUL)
                                        met_AZUL = Textos.texto_pantalla_rect(total2,Textos.fuentes(si,23),Blanco,Pant,rectTXT3A.x,rectTXT3A.y+5)
                                    #Transforma lo ingresado en el unicode en un entero, 
                                    # en caso de ingresar texto (letras o simbolos) el programa cae
                                    
                                    
                                    #Ejecuta la función para calcular el movimiento parabolico, 
                                    # funciona una vez que el usuario ingresa la velocidad
                                elif event.key == K_SPACE:
                                    if Velocidad_Azul[0] != str and Angulo_Azul[0] != str:
                                        if Velocidad_Azul[0] > 0 and Velocidad_Azul[0] < 201:
                                                if Angulo_Azul[0] > 0 and Angulo_Azul[0] < 181:
                                                    aux = True
                                                    salir=Proyectil.lanzamiento(aux)
                                                    Velocidad_Azul[0] = 0
                                                    Angulo_Azul[0] = 0
                                                    vel_AZUL = ''
                                                    ang_AZUL = ''
                                                else:
                                                    Velocidad_Azul[0] = 0
                                                    Angulo_Azul[0] = 0
                                                    vel_Azul = ''
                                                    ang_Azul = ''
                                                
                                        else:
                                            Velocidad_Azul[0] = 0
                                            Angulo_Azul[0] = 0
                                            vel_Azul = ''
                                            ang_Azul = ''
                                    else:
                                        print("weon tonto no funcina asi")
                                        Velocidad_Azul[0] = 0
                                        Angulo_Azul[0] = 0
                                        vel_Azul = ''
                                        ang_Azul = ''
                                
                                
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
                    pygame.quit()
                    sys.exit()
                    break
                elif Partida[0] == 2:
                    pygame.display.update()
                    print("Ganó el Azul")
                    pygame.time.delay(5000)
                    pygame.quit()
                    sys.exit()
                    break
                #Actualiza la pantalla
            
                #reloj.tick(60)