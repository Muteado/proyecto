import pygame
import random
from .Terreno import Terreno
from .Tanques import *
from .Variables import *
from .Esquinas import *
from .PosicionTanque import posicion
from .Turnos import *
from .movparabolicoacortado import *

class Lanzamiento:
    # ------------------------------
    # Función principal del juego
    # ------------------------------

    def lanzamiento(jugador,botonamarillo,botonnaranja,botonmorado):
        #Se define la letra por defecto
        fuente = Textos.fuentes(None, 50)
        prueba = 0
        mientras = True
                
        Turnos.balasturnos(botonamarillo, botonnaranja,botonmorado,jugador)

        Movimiento.angulos(jugador)
        angulo = jugador.get_Angulo()
        if angulo < 90:
            bala = Proyectil(jugador.get_X()+10, jugador.get_Y(), jugador.get_Angulo(), jugador.get_Velocidad())#velocidad,angulo
            
        if angulo == 90:
            bala = Proyectil(jugador.get_X(), jugador.get_Y()-10, jugador.get_Angulo(), jugador.get_Velocidad())#velocidad,angulo
            
        if angulo > 90:
            bala = Proyectil(jugador.get_X()-10, jugador.get_Y(), jugador.get_Angulo(), jugador.get_Velocidad())#velocidad,angulo
            

        clock = pygame.time.Clock()
        bala.disparar = True
            
                
        # el bucle principal del juego
        while mientras:
            bala.disparar = True
            
            # registramos cuanto ha pasado desde el ultimo ciclo
            tick = clock.tick(60)
            # Posibles entradas del teclado y mouse
                    
            if bala.disparar is True:
                # al tiempo anterior le sumamos lo transcurrido
                #print("debug 8")
                bala.tiempo = bala.tiempo + (tick / 200.0)

            # Actualizar la posición e información
            
            bala.update(bala.xUsar,bala.yUsar)

            if prueba < bala.yreal:
                #print("debug 7")
                prueba = bala.yreal

            if jugador.get_Angulo() >= 90:
                text = "Metros = %d m   Altura = %d m" % (jugador.get_X()-bala.xreal, prueba) ##AQUI OTRO VALOR
            elif jugador.get_Angulo() < 90:
                text = "Metros = %d m   Altura = %d m" % (bala.xreal-jugador.get_X(), prueba)
         
            mensaje = fuente.render(text, 600, Negro)
            
            fuente = pygame.font.Font(None,50)   
            
            if bala.disparar == True:
                if (int(bala.y)+11 >= ancho[0]) or (int(bala.x)+11 >= largo[0]) or (int(bala.y) <= 0) or (int(bala.x) <= 0): #este disparo es cuando choca en un limite superior
                        print("Tu disparo no sirvio")
                        bala.disparar = False
                        Terreno.dibuja_mapa(Pant,mapa)
                        break
                
                #Se ve si la bala de 105 mm impacta contra el terreno
                elif botonamarillo == True:
                    mientras = Movimiento.validaimpactos(10,bala, 50,jugador)
                    

                #Se valida si la bala perforante impactó en el terreno
                elif botonnaranja == True:
                    mientras = Movimiento.validaimpactos(7,bala, 40,jugador)
                    
                
                #Se valida si la bala 60 mm impactó en el terreno
                elif botonmorado == True:
                    mientras = Movimiento.validaimpactos(5,bala,30,jugador)
                                      
            # actualizamos la pantalla
            pygame.display.update()

        if jugador1.get_Estado() == True:
            posicion(jugador1)
        if jugador2.get_Estado() == True:
            posicion(jugador2)
        if jugador3.get_Estado() == True:
            posicion(jugador3)
        if jugador4.get_Estado() == True:
            posicion(jugador4)
        if jugador5.get_Estado() == True:
            posicion(jugador5)
        if jugador6.get_Estado() == True:
            posicion(jugador6)

        Pant.blit(mensaje, ((largo[0]/2)-250, 60))

    def Viento(Validar):
        
        if Validar == True:
            Viento_Movimiento[0] = random.randint(-10,10)
        else:
            Viento_Movimiento[0] = 0




