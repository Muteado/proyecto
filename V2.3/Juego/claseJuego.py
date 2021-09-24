import pygame
from pygame import *
from .ClassTextos import Textos
from .ClassOpciones import OpcionesCat
from .ClassRectangulos import Rectangulos
from .ClassEsquinas import DatosEsquinas
from .claseMovParabolico import Parabolico
from .claseTanques import Tanque
from .claseTerreno import Terreno
from .Variables import Azul, Blanco, Celeste, Rojo


class Juego:
    def juego(Pant,aux,ang_ROJO,vel_ROJO,ang_AZUL,vel_AZUL):
        #Variables bloques de datos:
        posIniX=0
        posIniY=0
        largoBloq = 200
        altoBloq = 20
        activo1R = False
        activo2R= False
        activo1A= False
        activo2A = False
        
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
        salir = False
        while salir!=True:
            #Divide la pantalla en 42 partes para posicionar elemntos proporcionalmente
            posicion = Pant.get_width()/42
            Pant.fill(Celeste) #Cielo
            #Genera terreno, tanques y agrega los recuadros de las esquinas
            Terreno.generar_terreno(posicion)
            Tanque.generar_tanques(posicion)
            DatosEsquinas.generarBloques(posIniX,posIniY,largoBloq,altoBloq)

            #Cambia el valor de total (total de metros recorridos en el movimiento parabolico), 
            # a caracteres para ser mostrado en pantalla
            total = str(total)
            total2 = str(total2)
            
            #Escribe los textos correspondientes a cada bloque de datos
            ang_ROJO = DatosEsquinas.textosEsquinas(ang_ROJO,rectTXT1R,Azul,activo1R)
            vel_ROJO = DatosEsquinas.textosEsquinas(vel_ROJO,rectTXT2R,Azul,activo2R)
            met_ROJO = Textos.texto_pantalla_rect(total,Textos.fuentes(None,23),Blanco,Pant,rectTXT3R.x,rectTXT3R.y+5)

            ang_AZUL = DatosEsquinas.textosEsquinas(ang_AZUL,rectTXT1A,Rojo,activo1A)
            vel_AZUL = DatosEsquinas.textosEsquinas(vel_AZUL,rectTXT2A,Rojo,activo2A)
            met_AZUL = Textos.texto_pantalla_rect(total2,Textos.fuentes(None,23),Blanco,Pant,rectTXT3A.x,rectTXT3A.y+5)

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
                        #Detecta click en rectangulo velocidad rojo
                        elif rectTXT2R.collidepoint(event.pos):
                            activo2R = True
                        #Detecta click en rectangulo angulo azul
                        elif rectTXT1A.collidepoint(event.pos):
                            activo1A= True
                        #Detecta click en rectangulo velocidad azul
                        elif rectTXT2A.collidepoint(event.pos):
                            activo2A = True
                        #Devuelve el valor falso a las variables en caso de no ser clickeadas
                        else:
                            activo1R = False
                            activo2R = False
                            activo1A = False
                            activo2A = False
                    #Detecta el teclado
                    if event.type == KEYDOWN:
                        #Si se clickeo el rectangulo del angulo rojo se activa 
                        # la opción para el ingreso de datos
                        if activo1R == True:
                            #Detecta la tecla escape para volver al menú
                            if event.key == K_ESCAPE:
                                salir=True
                            #Detecta la telca enter para terminar el ingreso de datos
                            elif event.key == pygame.K_RETURN:
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
                            #Transforma lo ingresado en el unicode en un entero, 
                            # en caso de ingresar texto (letras o simbolos) el programa cae
                            angulo_ROJO = int(ang_ROJO)
                        #Si se clickeo el rectangulo del velocidad rojo se activa 
                        # la opción para el ingreso de datos   
                        elif activo2R == True:
                            #Detecta la tecla escape para volver al menú
                            if event.key == K_ESCAPE:
                                salir=True
                            #Detecta la telca enter para terminar el ingreso de datos
                            elif event.key == pygame.K_RETURN:
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
                            #Transforma lo ingresado en el unicode en un entero, 
                            # en caso de ingresar texto (letras o simbolos) el programa cae
                            velocidad_ROJO = int(vel_ROJO)
                            #Ejecuta la función para calcular el movimiento parabolico, 
                            # funciona una vez que el usuario ingresa la velocidad
                            total = Parabolico.calculofuturo(angulo_ROJO, velocidad_ROJO)

                        #Si se clickeo el rectangulo del angulo azul se activa 
                        # la opción para el ingreso de datos
                        elif activo1A == True:
                            #Detecta la tecla escape para volver al menú
                            if event.key == K_ESCAPE:
                                salir=True
                            #Detecta la telca enter para terminar el ingreso de datos
                            elif event.key == pygame.K_RETURN:
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
                                print("Pico")
                                ang_AZUL=str(ang_AZUL)
                                #Funciona como un input caracter por caracter, 
                                # permite ingresar todo tipo de caracter
                                ang_AZUL += event.unicode
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
                            #Transforma lo ingresado en el unicode en un entero, 
                            # en caso de ingresar texto (letras o simbolos) el programa cae
                            
                            #Ejecuta la función para calcular el movimiento parabolico, 
                            # funciona una vez que el usuario ingresa la velocidad
                        
                        
                        #Otras teclas detectadas
                        else:
                            #Detecta la tecla escape para volver al menú
                            if event.key == K_ESCAPE:
                                salir=True
                            #Detecta la tecla p para poner en pausa el juego
                            if event.key == pygame.K_p:
                                pause = True
                                salir=OpcionesCat.pausa()
                        
                        angulo_AZUL = int(ang_AZUL)
                        velocidad_AZUL = int(vel_AZUL)
                        total2 = Parabolico.calculofuturo(angulo_AZUL, velocidad_AZUL)
                #Actualiza la pantalla
                pygame.display.update()
                #reloj.tick(60)