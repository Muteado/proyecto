from .Textos import Textos
from .Opciones import OpcionesCat
from .Rectangulos import Rectangulos
from .Esquinas import DatosEsquinas
from .MovParabolico import *
from .Terreno import Terreno
from .Variables import *
from .Turnos import *
from .Tanques import *

class Juego:
    def juego(Pant,AnguloINPUT,VelocidadINPUT,mapa,turnoJugador):
        #Variables bloques de datos:
        posiniX=0
        posiniY=0
        largoBloq = 200
        altoBloq = 20
        activoAngulo= False
        activoVelocidad = False
        x = 0
        global jugadores
        jugador = jugador1
        rectAngulo= Rectangulos.rectangulo(posiniX+largoBloq/2-10, posiniY+1,largoBloq,altoBloq)#Angulo azul
        rectVelocidad= Rectangulos.rectangulo(posiniX+largoBloq/2-10, posiniY+22,largoBloq,altoBloq)#Velocidead azul
        
        #Auxiliar loop principal
        if x == 0:
            Terreno.dibuja_mapa(Pant,mapa)
            DatosEsquinas.generarBloques(posiniX,posiniY,largoBloq,altoBloq, jugador)


            DatosEsquinas.textosEsquinas(AnguloINPUT,rectAngulo)#Angulo ROJO
            DatosEsquinas.textosEsquinas(VelocidadINPUT,rectVelocidad)#Velocidad ROJO
            

            pygame.display.update()
            Terreno.dibuja_mapa(Pant,mapa)
            DatosEsquinas.generarBloques(posiniX,posiniY,largoBloq,altoBloq, jugador)
            x += 1
        salir = False
        while salir!=True:
            # Dibuja los rectangulos de disparo de los tanques
            botonamarillo1 = Rectangulos.rectangulo(605,5,30,20)
            botonnaranja1 = Rectangulos.rectangulo(640,5,30,20)
            botonmorado1 = Rectangulos.rectangulo(675,5,30,20)
            Rectangulos.dibujaRectangulos(Pant,Amarillo,botonamarillo1,0)
            Rectangulos.dibujaRectangulos(Pant,Naranja,botonnaranja1,0)
            Rectangulos.dibujaRectangulos(Pant,Morado,botonmorado1,0)
            
            if (turnoJugador == 0): 
                jugador = jugador1
            if (turnoJugador == 1):  
                jugador = jugador2
            if (turnoJugador == 2):   
                jugador = jugador3
            if (turnoJugador == 3):  
                jugador = jugador4
            if (turnoJugador == 4):  
                jugador = jugador5
            if (turnoJugador == 5):  
                jugador = jugador6
                
            if Partida[0] == 1:
                Rectangulos.dibujaRectangulos(Pant, Amarillo, ((Pant.get_width()/2)-150,290,300,50),0)
                Textos.texto_pantalla_rect("Ganó el color: ",Textos.fuentes(None,34),Negro,Pant,(Pant.get_width()/2)-100,305)
                colorGanador = Rectangulos.rectangulo((Pant.get_width()/2)+80,300,30,30)
                Rectangulos.dibujaRectangulos(Pant,jugador.color,colorGanador,0)
                pygame.display.update()
                pygame.time.delay(5000)
                salir=True
                iniciada = False
                return iniciada
            Turnos.stockbalas(jugador.get_Balas(),jugador.color)
            DatosEsquinas.generarBloques(posiniX,posiniY,largoBloq,altoBloq,jugador)
            DatosEsquinas.textosEsquinas(AnguloINPUT,rectAngulo)#Angulo
            DatosEsquinas.textosEsquinas(VelocidadINPUT,rectVelocidad)#Velocidad
            
            if(jugador1.get_Estado()==True):
                Textos.texto_pantalla_rect(str(jugador1.get_Vida()),Textos.fuentes(None,23),Negro,Pant,jugador1.get_X(),jugador1.get_Y()-60)
 
            if(jugador2.get_Estado()==True):
                Textos.texto_pantalla_rect(str(jugador2.get_Vida()),Textos.fuentes(None,23),Negro,Pant,jugador2.get_X(),jugador2.get_Y()-60)

            if(jugador3.get_Estado()==True):
                Textos.texto_pantalla_rect(str(jugador3.get_Vida()),Textos.fuentes(None,23),Negro,Pant,jugador3.get_X(),jugador3.get_Y()-60)
 
            if(jugador4.get_Estado()==True):
                Textos.texto_pantalla_rect(str(jugador4.get_Vida()),Textos.fuentes(None,23),Negro,Pant,jugador4.get_X(),jugador4.get_Y()-60)

            if(jugador5.get_Estado()==True):
                Textos.texto_pantalla_rect(str(jugador5.get_Vida()),Textos.fuentes(None,23),Negro,Pant,jugador5.get_X(),jugador5.get_Y()-60)

            if(jugador6.get_Estado()==True):
                Textos.texto_pantalla_rect(str(jugador6.get_Vida()),Textos.fuentes(None,23),Negro,Pant,jugador6.get_X(),jugador6.get_Y()-60)

            
            bala105,balaperfo,bala60 = jugador.get_Balas()
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
                        #For aqui
                        #Detecta click en rectangulo angulo azul
                        if rectAngulo.collidepoint(event.pos):
                            activoAngulo= True
                            activoVelocidad = False
                            Angulo_Jugador[turnoJugador] = ''
                        #Detecta click en rectangulo velocidad azul
                        elif rectVelocidad.collidepoint(event.pos):
                            activoVelocidad = True
                            activoAngulo = False
                        #Devuelve el valor falso a las variables en caso de no ser clickeadas
                        elif botonamarillo1.collidepoint(event.pos):
                            if bala105 > 0:
                                botonamarillo = True
                                botonnaranja = False
                                botonmorado = False
                            else:
                                print("No te quedan balas! de 105 mm")
                                botonamarillo = False
                                botonnaranja = False
                                botonmorado = False 
                        elif botonnaranja1.collidepoint(event.pos):
                            if balaperfo > 0:   
                                botonamarillo= False
                                botonmorado = False
                                botonnaranja = True                                   
                            else:
                                print("No te quedan balas! perforantes")
                                botonamarillo, botonnaranja, botonmorado = False 
                        elif botonmorado1.collidepoint(event.pos):
                            if bala60 > 0:
                                botonamarillo = False
                                botonnaranja = False
                                botonmorado = True
                            else:
                                print("No te quedan balas! de 60 mm")
                                botonamarillo = False
                                botonnaranja = False
                                botonmorado = False  
                        else:
                            activoAngulo = False
                            activoVelocidad = False        
                    #Detecta el teclado
                    if event.type == pygame.KEYDOWN:    
                        #Si se clickeo el rectangulo del angulo azul se activa 
                        # la opción para el ingreso de datos
                        if activoAngulo == True:
                            #Detecta la tecla escape para volver al menú
                            if event.key == K_ESCAPE:
                                salir=True
                                iniciada = True
                                return iniciada
                            #Detecta la telca enter para terminar el ingreso de datos
                            elif event.key == pygame.K_RETURN:
                                pygame.display.update()
                                activoAngulo = False
                            #Detecta la tecla retroceso para borrar
                            # en caso de ser necesario
                            elif event.key == pygame.K_BACKSPACE:
                                #Borra un elemento a la vez de los datos ingresados por el ususario 
                                # en el apartado de angulo azul, al borrar todos los datos el programa cae
                                AnguloINPUT = AnguloINPUT[:-1]
                                DatosEsquinas.generarBloques(posiniX,posiniY,largoBloq,altoBloq, jugador)
                            #En caso de no borrar datos estará constantemente ingresando 
                            # todas las teclas preNoneonadas en el teclado
                            elif pygame.K_0 <= event.key <= pygame.K_9:
                                #Actualiza la variable para el unicode
                                AnguloINPUT=str(AnguloINPUT)
                                #Funciona como un input caracter por caracter, 
                                # permite ingresar todo tipo de caracter
                                AnguloINPUT += event.unicode
                                Angulo_Jugador[turnoJugador] = int(AnguloINPUT)
                        
                        #None se clickeo el rectangulo del velocidad azul se activa 
                        # la opción para el ingreso de datos   
                        if activoVelocidad == True:
                            #Detecta la tecla escape para volver al menú
                            if event.key == K_ESCAPE:
                                salir=True
                                iniciada = True
                                return iniciada
                            #Detecta la telca enter para terminar el ingreso de datos
                            elif event.key == pygame.K_RETURN:
                                pygame.display.update()
                                activoVelocidad = False
                            #Detecta la tecla retroceso para borrar
                            # en caso de ser necesario
                            elif event.key == pygame.K_BACKSPACE:
                                #Borra un elemento a la vez de los datos ingresados por el ususario 
                                # en el apartado de angulo azul, al borrar todos los datos el programa cae
                                VelocidadINPUT = VelocidadINPUT[:-1]
                                DatosEsquinas.generarBloques(posiniX,posiniY,largoBloq,altoBloq,jugador)
                            #En caso de no borrar datos estará constantemente ingresando 
                            # todas las teclas preNoneonadas en el teclado
                            
                            elif pygame.K_0 <= event.key <= pygame.K_9:
                                #Actualiza la variable para el unicode
                                VelocidadINPUT=str(VelocidadINPUT)
                                #Funciona como un input caracter por caracter, 
                                # permite ingresar todo tipo de caracter
                                VelocidadINPUT += event.unicode
                                Velocidad_Jugador[turnoJugador] = int(VelocidadINPUT)

                        
                        if event.key == K_SPACE:
                            if botonamarillo == True or botonnaranja == True or botonmorado == True:
                                if Velocidad_Jugador[turnoJugador] != str and Angulo_Jugador[turnoJugador] != str:
                                    Velocidad_Jugador[turnoJugador] = int(Velocidad_Jugador[turnoJugador])
                                    if Velocidad_Jugador[turnoJugador] > 0 and Velocidad_Jugador[turnoJugador] < 201:
                                        if Angulo_Jugador[turnoJugador] >= 0 and Angulo_Jugador[turnoJugador] <= 180:
                                            jugador.set_Angulo(Angulo_Jugador[turnoJugador])
                                            jugador.set_Velocidad(Velocidad_Jugador[turnoJugador])
                                            Lanzamiento.lanzamiento(jugador,botonamarillo,botonnaranja,botonmorado)
                                            VelocidadINPUT = ''
                                            AnguloINPUT = ''
                                            Angulo_Jugador[turnoJugador] = ''
                                            Velocidad_Jugador[turnoJugador] = ''
                                            botonamarillo = False
                                            botonnaranja = False
                                            botonmorado = False
                                            turnoJugador+=1
                                            if(turnoJugador >= jugadores):
                                                turnoJugador = 0
                                        else:
                                            VelocidadINPUT = ''
                                            AnguloINPUT = ''
                                            Angulo_Jugador[turnoJugador] = ''
                                            Velocidad_Jugador[turnoJugador] = ''
                                            
                                    else:
                                        VelocidadINPUT = ''
                                        AnguloINPUT = ''
                                        Angulo_Jugador[turnoJugador] = ''
                                        Velocidad_Jugador[turnoJugador] = ''
                                else:
                                    VelocidadINPUT = ''
                                    AnguloINPUT = ''
                                    Angulo_Jugador[turnoJugador] = ''
                                    Velocidad_Jugador[turnoJugador] = ''
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
                                iniciada = True
                                return iniciada
            
