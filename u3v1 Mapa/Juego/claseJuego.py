from .ClassTextos import Textos
from .ClassOpciones import OpcionesCat
from .ClassRectangulos import Rectangulos
from .ClassEsquinas import DatosEsquinas
from .claseMovParabolico import *
from .claseTerreno import Terreno
from .Variables import *
from .ClaseBotones import *

class Juego:
    def juego(Pant,ang_ROJO,vel_ROJO,ang_AZUL,vel_AZUL,mapa):
        #Variables bloques de datos:
        posiniX=0
        posiniY=0
        largoBloq = 200
        altoBloq = 20
        activo1R = False
        activo2R= False
        activo1A= False
        activo2A = False
        botonamarillo = False
        botonnaranja = False
        botonmorado = False  
        x = 0
        
        ##Crea los rectangulos para el ingreso de datos en las esquinas
        rectTXT1R = Rectangulos.rectangulo(Pant.get_width()-largoBloq/2-15, posiniY+1,largoBloq,altoBloq)#Angulo rojo
        rectTXT2R = Rectangulos.rectangulo(Pant.get_width()-largoBloq/2-15, posiniY+22,largoBloq,altoBloq)#Velocidad rojo

        rectTXT1A= Rectangulos.rectangulo(posiniX+largoBloq/2-10, posiniY+1,largoBloq,altoBloq)#Angulo azul
        rectTXT2A= Rectangulos.rectangulo(posiniX+largoBloq/2-10, posiniY+22,largoBloq,altoBloq)#Velocidead azul


        #Auxiliar loop principal
        if x == 0:
            Terreno.dibuja_mapa(Pant,mapa)
            DatosEsquinas.generarBloques(posiniX,posiniY,largoBloq,altoBloq)

            DatosEsquinas.textosEsquinas(ang_ROJO,rectTXT1R,Azul,activo1R)#Angulo AZUL
            DatosEsquinas.textosEsquinas(vel_ROJO,rectTXT2R,Azul,activo2R)#Velocidad AZUL
            
            DatosEsquinas.textosEsquinas(ang_AZUL,rectTXT1A,Rojo,activo1A)#Angulo ROJO
            DatosEsquinas.textosEsquinas(vel_AZUL,rectTXT2A,Rojo,activo2A)#Velocidad ROJO
            

            pygame.display.update()
            Terreno.dibuja_mapa(Pant,mapa)
            DatosEsquinas.generarBloques(posiniX,posiniY,largoBloq,altoBloq)
            x += 1
        salir = False
        while salir!=True:
            DatosEsquinas.generarBloques(posiniX,posiniY,largoBloq,altoBloq)

            #Escribe los textos correspondientes a cada bloque de datos
            DatosEsquinas.textosEsquinas(ang_ROJO,rectTXT1R,Azul,activo1R)#Angulo AZUL
            DatosEsquinas.textosEsquinas(vel_ROJO,rectTXT2R,Azul,activo2R)#Velocidad AZUL

            DatosEsquinas.textosEsquinas(ang_AZUL,rectTXT1A,Rojo,activo1A)#Angulo ROJO
            DatosEsquinas.textosEsquinas(vel_AZUL,rectTXT2A,Rojo,activo2A)#Velocidad ROJO
            
            #Vida Tanque Azul
            Textos.texto_pantalla_rect(str(vidaTank[0]),Textos.fuentes(None,23),Negro,Pant,X_Y_Tanques[0],X_Y_Tanques[1]-60)
            #Vida Tanque Rojo
            Textos.texto_pantalla_rect(str(vidaTank[1]),Textos.fuentes(None,23),Negro,Pant,X_Y_Tanques[2],X_Y_Tanques[3]-60)

            if Turno[0] == 1:
                Textos.texto_pantalla_rect(str(balas[0]),Textos.fuentes(None,27),Azul,Pant,610,5)
                Textos.texto_pantalla_rect(str(balas[1]),Textos.fuentes(None,27),Azul,Pant,645,5)
                Textos.texto_pantalla_rect(str(balas[2]),Textos.fuentes(None,27),Azul,Pant,680,5)
                
            if Turno[0] == 2:
                Textos.texto_pantalla_rect(str(balas[3]),Textos.fuentes(None,27),Rojo,Pant,610,5)
                Textos.texto_pantalla_rect(str(balas[4]),Textos.fuentes(None,27),Rojo,Pant,645,5)
                Textos.texto_pantalla_rect(str(balas[5]),Textos.fuentes(None,27),Rojo,Pant,680,5)


            pygame.display.update()
            if Partida[0] == 0:
                for event in pygame.event.get():
                    #Detecta cierre de ventana
                    if event.type==pygame.QUIT:
                        #Termina el while y sale del juego
                        salir=True
                        pygame.quit()
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
                                if balas[0] > 0:
                                    botonamarillo = True
                                    botonnaranja = False
                                    botonmorado = False
                                
                                else:
                                    print("No te quedan balas! de 105 mm")
                                    botonamarillo = False
                                    botonnaranja = False
                                    botonmorado = False 
                            elif botonnaranja1.collidepoint(event.pos):
                                if balas[1] > 0:   
                                    botonamarillo = False
                                    botonnaranja = True
                                    botonmorado = False

                                else:
                                    print("No te quedan balas! perforantes")
                                    botonamarillo = False
                                    botonnaranja = False
                                    botonmorado = False 

                            elif botonmorado1.collidepoint(event.pos):
                                if balas[2] > 0:
                                    botonamarillo = False
                                    botonnaranja = False
                                    botonmorado = True

                                else:
                                    print("No te quedan balas! de 60 mm")
                                    botonamarillo = False
                                    botonnaranja = False
                                    botonmorado = False 
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
                                if balas[3] > 0:
                                    botonamarillo = True
                                    botonnaranja = False
                                    botonmorado = False
                                
                                else:
                                    print("No te quedan balas! de 105 mm")
                                    botonamarillo = False
                                    botonnaranja = False
                                    botonmorado = False 
                            elif botonnaranja1.collidepoint(event.pos):
                                if balas[4] > 0: 
                                    botonamarillo = False
                                    botonnaranja = True
                                    botonmorado = False

                                else: 
                                    print("No te quedan balas! perforantes")
                                    botonamarillo = False
                                    botonnaranja = False
                                    botonmorado = False 

                            elif botonmorado1.collidepoint(event.pos):
                                if balas[5] > 0:    
                                    botonamarillo = False
                                    botonnaranja = False
                                    botonmorado = True
                                else:
                                    print("No te quedan balas! de 60 mm")
                                    botonamarillo = False
                                    botonnaranja = False
                                    botonmorado = False 
                            else:
                                activo1R = False
                                activo2R = False
                                activo1A = False
                                activo2A = False
  
                    #Detecta el teclado
                    if event.type == pygame.KEYDOWN:    
                        if Turno[0] == 1:
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
                                
                                #Ejecuta la función para calcular el movimiento parabolico, 
                                # funciona una vez que el usuario ingresa la velocidad
                            
                        
                            if event.key == K_SPACE:
                                if botonamarillo == True or botonnaranja == True or botonmorado == True:
                                    if Velocidad_Azul[0] != str and Angulo_Azul[0] != str:
                                        if Velocidad_Azul[0] > 0 and Velocidad_Azul[0] < 201:
                                                if Angulo_Azul[0] >= 0 and Angulo_Azul[0] <= 180:
                                                    aux = True
                                                    Proyectil.lanzamiento(botonamarillo,botonnaranja,botonmorado,aux)
                                                    vel_AZUL = ''
                                                    ang_AZUL = ''
                                                    Angulo_Azul[0] = '0'
                                                    Velocidad_Azul[0] = '0'
                                                    botonamarillo = False
                                                    botonnaranja = False
                                                    botonmorado = False
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
                                    botonamarillo = False
                                    botonnaranja = False
                                    botonmorado = False
                                    Textos.texto_pantalla_rect("Por favor elija el color y luego presione espacio", Textos.fuentes(None, 40), Azul, Pant,350,100)
                                    print("por favor elija el color y luego presione espacio")
 
                            #Otras teclas detectadas
                            else:
                                #Detecta la tecla escape para volver al menú
                                if event.key == K_ESCAPE:
                                    salir=True
                                    #if event.key == K_ESCAPE:
                                    #    salir = False
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
                            elif event.key == K_SPACE:
                                if botonamarillo == True or botonnaranja == True or botonmorado == True:
                                    if Velocidad_Rojo[0] != str and Angulo_Rojo[0] != str:
                                        if Velocidad_Rojo[0] > 0 and Velocidad_Rojo[0] < 201:
                                            if Angulo_Rojo[0] > 0 and Angulo_Rojo[0] < 181:
                                                aux = True
                                                Proyectil.lanzamiento(botonamarillo,botonnaranja,botonmorado,aux)
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
                                    botonamarillo = False
                                    botonnaranja = False
                                    botonmorado = False
                                    Textos.texto_pantalla_rect("Por favor elija el color y luego presione espacio", Textos.fuentes(None, 40), Rojo, Pant,350,100)
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
                Rectangulos.botones(Pant, Amarillo, ((Pant.get_width()/2)-150,300,300,25))
                Textos.texto_pantalla_rect("Ganó el Tanque Rojo!",Textos.fuentes(None,30),Negro,Pant,(Pant.get_width()/2)-100,305)
                
                pygame.display.update()
                pygame.time.delay(5000)
                salir=True
                iniciada = False
                return iniciada
                
            elif Partida[0] == 2:                
                Rectangulos.botones(Pant, Amarillo, ((Pant.get_width()/2)-150,300,300,25))
                Textos.texto_pantalla_rect("Ganó el Tanque Azul!",Textos.fuentes(None,30),Negro,Pant,(Pant.get_width()/2)-100,305)
                
                pygame.display.update()
                pygame.time.delay(5000)
                salir=True
                iniciada = False
                return iniciada
