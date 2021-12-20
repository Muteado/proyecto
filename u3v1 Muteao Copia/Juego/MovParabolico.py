import pygame
from .Terreno import Terreno
from .Tanques import *
from .Variables import *
from .Esquinas import *
from .Botones import *
from .PosicionTanque import posicion
from .Turnos import *
from .movparabolicoacortado import *


class Lanzamiento:
    # ------------------------------
    # Función principal del juego
    # ------------------------------

    def lanzamiento(botonamarillo,botonnaranja,botonmorado,aux):
        # se define la letra por defecto
        fuente = Textos.fuentes(None, 50)
        prueba = 0
        
        #bala = Proyectil(0,0,0,0)
        #bala = object
        #clock = pygame.time.Clock()
        #clock = pygame.time.Clock()
        # se crea un proyectil a lanzar
        

        if Turno[0] == 1:
            #EleccionbalaAzul[0] = int(input("1. 105 mm \n2. perforante \n3. 60 mm \nIngrese su bala: "))
            Turnos.balasturnos(botonmorado, botonnaranja,botonmorado,balaspj1)

        if Turno[0] == 2:
            #EleccionbalaRojo[0] = int(input("1. 105 mm \n2. perforante \n3. 60 mm \nIngrese su bala: "))
            Turnos.balasturnos(botonmorado, botonnaranja,botonmorado,balaspj2)


        if Turno[0] == 1:
            #Tanque Azul
            print("debug 0")
            #Movimiento.angulos(0,1,Angulo_Azul, Velocidad_Azul)
            angulo = Angulo_Azul[0]
            if angulo < 90:
                bala = Proyectil(X_Y_Tanques[0]+10, X_Y_Tanques[1], Angulo_Azul[0], Velocidad_Azul[0])#velocidad,angulo
                print("debug 1")
            if angulo == 90:
                bala = Proyectil(X_Y_Tanques[0], X_Y_Tanques[1]-10, Angulo_Azul[0], Velocidad_Azul[0])#velocidad,angulo
                print("debug 2")
            if angulo > 90:
                bala = Proyectil(X_Y_Tanques[0]-10, X_Y_Tanques[1], Angulo_Azul[0], Velocidad_Azul[0])#velocidad,angulo
                print("debug 3")

            clock = pygame.time.Clock()
            bala.disparar = True
            
            
            
        elif Turno[0] == 2:
            #Tanque Rojo
            print("debug 5")
            #0Movimiento.angulos(0,1,Angulo_Azul, Velocidad_Azul)
            angulo = Angulo_Azul[0]
            if angulo < 90:
                bala = Proyectil(X_Y_Tanques[2]+10, X_Y_Tanques[3], Angulo_Azul[0], Velocidad_Azul[0])#velocidad,angulo
                print("debug 1")
            if angulo == 90:
                bala = Proyectil(X_Y_Tanques[2], X_Y_Tanques[3]-10, Angulo_Azul[0], Velocidad_Azul[0])#velocidad,angulo
                print("debug 2")
            if angulo > 90:
                bala = Proyectil(X_Y_Tanques[2]-10, X_Y_Tanques[3], Angulo_Azul[0], Velocidad_Azul[0])#velocidad,angulo
                print("debug 3")
            
            clock = pygame.time.Clock()
            bala.disparar = True
            
            
        # el bucle principal del juego
        while True:
            bala.disparar = True
            
            print("debug 6")
            # registramos cuanto ha pasado desde el ultimo ciclo
            tick = clock.tick(60)
            # Posibles entradas del teclado y mouse
                    

            if bala.disparar is True:
                # al tiempo anterior le sumamos lo transcurrido
                print("debug 8")
                bala.tiempo = bala.tiempo + (tick / 200.0)

            # Actualizar la posición e información
            
            bala.update(bala.xUsar,bala.yUsar)

            if prueba < bala.yreal:
                print("debug 7")
                prueba = bala.yreal
            
            if Turno[0] == 1:
                print("debug 9")
                #Movimiento.ImprimeMetros(Turno,bala)
                if Angulo_Azul[0] >= 90:
                    print("entra")
                    text = "Metros = %d m   Altura = %d m" % (
                    XdelTank[0]-bala.xreal, prueba)
                elif Angulo_Azul[0] < 90:
                    print("entra2")
                    text = "Metros = %d m   Altura = %d m" % (
                        bala.xreal-XdelTank[0], prueba)
         

            if Turno[0] == 2:
                #Movimiento.ImprimeMetros(Turno,bala)
                if Angulo_Azul[0] >= 90:
                    text = "Metros = %d m   Altura = %d m" % (
                    XdelTank[0]-bala.xreal, prueba)
                elif Angulo_Azul[0] < 90:
                    text = "Metros = %d m   Altura = %d m" % (
                        bala.xreal-XdelTank[0], prueba)
        
            mensaje = fuente.render(text, 600, Negro)
            
            fuente = pygame.font.Font(None,50)   

            
            print("debug 10")
            
            if bala.disparar == True:
                print("debug 11")
                #if vidaTank[0] >= 0 and vidaTank[1] >= 0:
                if (int(bala.y)+11 >= ancho) or (int(bala.x)+11 >= largo) or (int(bala.y) <= 0) or (int(bala.x) <= 0):
                        print("Tu disparo no sirvio")
                        bala.disparar = False
                        Terreno.dibuja_mapa(Pant,mapa)
                        if Turno[0] == 1:
                            Turno[0] = 2
                        elif Turno[0] == 2:
                            Turno[0] = 1
                        break
                
                #Se ve si la bala de 105 mm impacta contra el terreno
                elif botonamarillo == True:
                    
                    #Es el turno del tanque azul
                    if Turno[0] == 1:
                        #Valida si impacta en el tanque azul
                        print("entra")
                        Movimiento.validaimpactos(Turno, 10,bala)
                        print("SALE")
                    
                    #Es el turno del jugador rojo
                    elif Turno[0] == 2:

                        Movimiento.validaimpactos(Turno, 10,bala)

                #Se valida si la bala perforante impactó en el terreno
                elif botonnaranja == True:
                    
                    if Turno[0] == 1:

                        Movimiento.validaimpactos(Turno, 7,bala)
                    
                    elif Turno[0] == 2:

                        Movimiento.validaimpactos(Turno, 7,bala)
                
                #Se valida si la bala 60 mm impactó en el terreno
                elif botonmorado == True:
                    
                    if Turno[0] == 1:

                        Movimiento.validaimpactos(Turno, 5,bala)

                    elif Turno[0] == 2:

                        Movimiento.validaimpactos(Turno, 5,bala)
                       
                    
            # actualizamos la pantalla
            pygame.display.update()

        posicion()
        if vidaTank[0] <= 0:
            print("Perdió: Tanque Azul")
            Partida[0] = 1
        if vidaTank[1] <= 0:
            print("Perdió: Tanque Rojo")
            Partida[0] = 2


        Pant.blit(mensaje, (400, 50))     



'''
El problema que ocurre es que sucede el lanzamiento, al momento de pasar de turno hay un pequeño delay que no tengo claro el motivo y en x ocasion puede que tambien tire 2 veces durante el mismo turno sin motivo aparente. 
Otro problema que vi es que el contador de balas no esta funcionando, asi como tampoco al momento de impactar las balas en algun tanque.
'''