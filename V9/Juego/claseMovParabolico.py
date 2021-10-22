from pygame.time import Clock
from Juego.ClassOpciones import OpcionesCat
from Juego.claseTerreno import Terreno
from Juego.claseTanques import *
from .claseTanques import *
from pygame import *
import math,pygame,sys
from .Variables import *
'''class Parabolico:
    def calculofuturo(β, vi):
        pass
        #return xmax'''

class Proyectil():
    """Clase que representa el proyectil lanzado"""
    def __init__(self, x, y, ang, velo):
        self.angulo = ang#angulo
        self.veloc = velo#velocidad
        self.tiempo = 0
        self.x = x+35
        self.xUsar = x
        self.y = y-35
        self.disparar = False
        self.xreal = x
        self.yreal = ancho - self.y
        self.yUsar = ancho - self.y

    def update(self,x,y):
        "actualizar la posición del proyectil"
        self.velocx = self.veloc * math.cos(math.radians(self.angulo))
        self.velocy = self.veloc * math.sin(math.radians(self.angulo))

        if self.disparar is True:
            # esta en movimiento, hay que actualizar la posición
            self.xreal = (x + self.velocx * self.tiempo)
            self.yreal = (y + self.velocy * self.tiempo +
                          (-9.8 * (self.tiempo ** 2)) / 2)
            # Corregir la posición en el eje vertical
            self.x = self.xreal
            self.y = ancho - self.yreal
        else:
            # se mantiene sin disparar, por lo cual no se hace nada
            pass


    # ------------------------------
    # Función principal del juego
    # ------------------------------

    def lanzamiento(aux):
        # se define la letra por defecto
        fuente = pygame.font.Font(None, 20)
        prueba = 0
        # se crea un proyectil a lanzar

        if Turno[0] == 1:
            EleccionbalaAzul[0] = int(input("1. 105 mm \n2. perforante \n3. 60 mm \nIngrese su bala: "))
            if EleccionbalaAzul[0] == 1 and c105[0] > 0:
                angulo = int(input('Ingrese angulo bala: '))
                velocidad = int(input('Ingrese velocidad bala: '))
                bala = Proyectil(X_Tanque_Azul[0]+20, Y_Tanque_Azul[0], angulo, velocidad)#velocidad,angulo
                #pygame.key.set_repeat(1, 80)  # Activa repetición de teclas
                Balaaux[0] = 50
                c105[0] = c105[0] -1
                #Turno[0] = 2
                clock = pygame.time.Clock()
                bala.disparar = aux
                
                
            if EleccionbalaAzul[0] == 2 and cperforante[0] > 0:
                angulo = int(input('Ingrese angulo bala: '))
                velocidad = int(input('Ingrese velocidad bala: '))
                bala = Proyectil(X_Tanque_Azul[0]+20, Y_Tanque_Azul[0], angulo, velocidad)#velocidad,angulo
                #pygame.key.set_repeat(1, 80)  # Activa repetición de teclas
                Balaaux[0] = 40
                cperforante[0] = cperforante[0] - 1
                #Turno[0] = 2
                clock = pygame.time.Clock()
                bala.disparar = aux
                

            if EleccionbalaAzul[0] == 3 and c60[0] > 0:
                angulo = int(input('Ingrese angulo bala: '))
                velocidad = int(input('Ingrese velocidad bala: '))
                bala = Proyectil(X_Tanque_Azul[0]+20, Y_Tanque_Azul[0], angulo, velocidad)#velocidad,angulo
                #pygame.key.set_repeat(1, 80)  # Activa repetición de teclas
                Balaaux[0] = 30
                c60[0] = c60[0] - 1
                #Turno[0] = 2
                clock = pygame.time.Clock()
                bala.disparar = aux
                

            if c105[0] == 0 or cperforante[0] == 0 or c60[0] == 0:
                print("No te quedan balas!")
                print("")
                Turno[0] = 1
                print("")
            if c105[0] == 0 and cperforante[0] == 0 and c60[0] == 0:
                print("Te quedaste sin balas!")
                Turno[0] = 2

        if Turno[0] == 2:
            EleccionbalaRojo[0] = int(input("1. 105 mm \n2. perforante \n3. 60 mm \nIngrese su bala: "))
            if EleccionbalaRojo[0] == 1 and c105[1] > 0:
                angulo = int(input('Ingrese angulo bala: '))
                velocidad = int(input('Ingrese velocidad bala: '))
                bala = Proyectil(X_Tanque_Azul[0]+20, Y_Tanque_Azul[0], angulo, velocidad)#velocidad,angulo
                #pygame.key.set_repeat(1, 80)  # Activa repetición de teclas
                Balaaux[0] = 50
                c105[1] = c105[1] -1
                #Turno[0] = 1
                clock = pygame.time.Clock()
                bala.disparar = aux
                

            if EleccionbalaRojo[0] == 2 and cperforante[1] > 0:
                angulo = int(input('Ingrese angulo bala: '))
                velocidad = int(input('Ingrese velocidad bala: '))
                bala = Proyectil(X_Tanque_Azul[0]+20, Y_Tanque_Azul[0], angulo, velocidad)#velocidad,angulo
                #pygame.key.set_repeat(1, 80)  # Activa repetición de teclas
                Balaaux[0] = 40
                cperforante[1] = cperforante[1] - 1
                #Turno[0] = 1
                clock = pygame.time.Clock()
                bala.disparar = aux
                

            if EleccionbalaRojo[0] == 3 and c60[1] > 0:
                angulo = int(input('Ingrese angulo bala: '))
                velocidad = int(input('Ingrese velocidad bala: '))
                bala = Proyectil(X_Tanque_Azul[0]+20, Y_Tanque_Azul[0], angulo, velocidad)#velocidad,angulo
                #pygame.key.set_repeat(1, 80)  # Activa repetición de teclas
                Balaaux[0] = 30
                c60[1] = c60[1] - 1
                #Turno[0] = 1
                clock = pygame.time.Clock()
                bala.disparar = aux
                
            
            if c105[1] == 0 or cperforante[1] == 0 or c60[1] == 0:
                print("No te quedan balas!")
                print("")
                Turno[0] = 2
                print("")
            if c105[1] == 0 and cperforante[1] == 0 and c60[1] == 0:
                print("Te quedaste sin balas!")
                Turno[0] = 1


        if Turno[0] == 1:
            #Tanque Azul
            angulo = Angulo_Azul[0]
            if angulo < 90:
                bala = Proyectil(X_Tanque_Azul[0]+10, Y_Tanque_Azul[0], Angulo_Azul[0], Velocidad_Azul[0])#velocidad,angulo
            if angulo == 90:
                bala = Proyectil(X_Tanque_Azul[0], Y_Tanque_Azul[0]-10, Angulo_Azul[0], Velocidad_Azul[0])#velocidad,angulo
            if angulo > 90:
                bala = Proyectil(X_Tanque_Azul[0]-10, Y_Tanque_Azul[0], Angulo_Azul[0], Velocidad_Azul[0])#velocidad,angulo

            clock = pygame.time.Clock()
            bala.disparar = aux
            
        elif Turno[0] == 2:
            #Tanque Rojo
            angulo = Angulo_Rojo[0]
            if angulo < 90:
                bala = Proyectil(X_Tanque_Rojo[0]+20, Y_Tanque_Rojo[0], Angulo_Rojo[0], Velocidad_Rojo[0])#velocidad,angulo
            if angulo == 90:
                bala = Proyectil(X_Tanque_Rojo[0], Y_Tanque_Rojo[0]-10, Angulo_Rojo[0], Velocidad_Rojo[0])#velocidad,angulo
            if angulo > 90:
                bala = Proyectil(X_Tanque_Rojo[0]-20, Y_Tanque_Rojo[0], Angulo_Rojo[0], Velocidad_Rojo[0])#velocidad,angulo
                
            clock = pygame.time.Clock()
            bala.disparar = aux
        # el bucle principal del juego
        while True:
            # registramos cuanto ha pasado desde el ultimo ciclo
            tick = clock.tick(60)
            # Posibles entradas del teclado y mouse
                    

            if bala.disparar is True:
                # al tiempo anterior le sumamos lo transcurrido
                bala.tiempo = bala.tiempo + (tick / 200.0)

            # Actualizar la posición e información
            
            bala.update(bala.xUsar,bala.yUsar)

            if prueba < bala.yreal:
                prueba = bala.yreal
            
            if Turno[0] == 1:
                
                if Angulo_Azul[0] >= 90:
                    text = "x = %d m   y = %d m" % (
                        XdeTankA-bala.xreal, prueba)
                elif Angulo_Azul[0] < 90:
                    text = "x = %d m   y = %d m" % (
                        bala.xreal-XdeTankA, prueba)
            if Turno[0] == 2:

                if Angulo_Rojo[0] >= 90:
                    text = "x = %d m   y = %d m" % (
                        XdeTankR-bala.xreal, prueba)
                elif Angulo_Rojo[0] < 90:
                    text = "x = %d m   y = %d m" % (
                        bala.xreal-XdeTankR, prueba)

            mensaje = fuente.render(text, 600, (255, 255, 255))

            # Re dibujar los elementos en pantalla
            
            
            fuente = pygame.font.Font(None,50)
            
            
            if bala.disparar == True:

                #if vidaAzul[0] >= 0 and vidaRojo[0] >= 0:
                if mapa[int(bala.y)][int(bala.x)] == 3:
                    print("cayó en el tanque rojo")
                    #Partida[0] = 2
                    
                    #bala.disparar = False
                    #bala = Proyectil(300, 300, angulo, velocidad)#velocidad,angulo
                    Terreno.dibuja_mapa(Pant,mapa)
                    
                    
                    if vidaRojo[0] > 0:
                        if Turno[0] == 1:
                            vidaRojo[0] = vidaRojo[0] - Balaaux[0]
                            print("La vida del rojo es: ",vidaRojo[0])
                            Turno[0] = 2
                            break
                        if Turno[0] == 2:
                            vidaRojo[0] = vidaRojo[0] - Balaaux[0]
                            print("La vida del rojo es: ",vidaRojo[0])
                            Turno[0] = 1
                            break

                        
                if mapa[int(bala.y)][int(bala.x)] == 2:
                    print("cayó en el tanque azul")
                    #Partida[0] = 1
                    
                    #bala.disparar = False
                    #bala = Proyectil(300, 300, angulo, velocidad)#velocidad,angulo
                    Terreno.dibuja_mapa(Pant,mapa)
                    
                    
                    if vidaAzul[0] > 0:
                        if Turno[0] == 1:
                            vidaAzul[0] = vidaAzul[0] - Balaaux[0]
                            print("La vida del Azul es: ",vidaAzul[0])
                            Turno[0] = 2
                            break
                        if Turno[0] == 2:
                            vidaAzul[0] = vidaAzul[0] - Balaaux[0]
                            print("La vida del Azul es: ",vidaAzul[0])
                            Turno[0] = 1
                            break
                
                
                if (int(bala.y) >= ancho) or (int(bala.x) >= largo) or (int(bala.y) <= 0) or (int(bala.x) <= 0):
                        print("Tu disparo no sirvio")
                        bala.disparar = False
                        Terreno.dibuja_mapa(Pant,mapa)
                        if Turno[0] == 1:
                            Turno[0] = 2
                        elif Turno[0] == 2:
                            Turno[0] = 1
                        break

                elif mapa[int(bala.y)][int(bala.x)] == 0:
                    if Turno[0] == 1:
                        if EleccionbalaAzul[0] == 1:
                            pygame.draw.circle(Pant, (0, 0, 0), (int(bala.x), int(bala.y)), 5)
                        elif EleccionbalaAzul[0] == 2:
                            pygame.draw.circle(Pant, (0, 0, 0), (int(bala.x), int(bala.y)), 5)
                        elif EleccionbalaAzul[0] == 3:
                            pygame.draw.circle(Pant, (0, 0, 0), (int(bala.x), int(bala.y)), 5)
                    elif Turno[0] == 2:
                        if EleccionbalaRojo[0] == 1:
                            pygame.draw.circle(Pant, (0, 0, 0), (int(bala.x), int(bala.y)), 5)
                        elif EleccionbalaRojo[0] == 2:
                            pygame.draw.circle(Pant, (0, 0, 0), (int(bala.x), int(bala.y)), 5)
                        elif EleccionbalaRojo[0] == 3:
                            pygame.draw.circle(Pant, (0, 0, 0), (int(bala.x), int(bala.y)), 5)

                
                elif mapa[int(bala.y)][int(bala.x)] == 1:
                    if Turno[0] == 1:
                        if EleccionbalaAzul[0] == 1:
                            pygame.draw.circle(Pant, (0, 0, 0), (int(bala.x), int(bala.y)), 5)
                        elif EleccionbalaAzul[0] == 2:
                            pygame.draw.circle(Pant, (0, 0, 0), (int(bala.x), int(bala.y)), 5)
                        elif EleccionbalaAzul[0] == 3:
                            pygame.draw.circle(Pant, (0, 0, 0), (int(bala.x), int(bala.y)), 5)
                    elif Turno[0] == 2:
                        if EleccionbalaRojo[0] == 1:
                            pygame.draw.circle(Pant, (0, 0, 0), (int(bala.x), int(bala.y)), 5)
                        elif EleccionbalaRojo[0] == 2:
                            pygame.draw.circle(Pant, (0, 0, 0), (int(bala.x), int(bala.y)), 5)
                        elif EleccionbalaRojo[0] == 3:
                            pygame.draw.circle(Pant, (0, 0, 0), (int(bala.x), int(bala.y)), 5)
                            
                    pygame.display.update()
                    print("cayó en el suelo")
                    bala.disparar = False
                    
                    Terreno.dibuja_mapa(Pant,mapa)
                    if Turno[0] == 1:
                        Turno[0] = 2
                    elif Turno[0] == 2:
                        Turno[0] = 1
                    break
        

                
            # actualizamos la pantalla
            pygame.display.update()
        if vidaAzul[0] <= 0:
            print("Perdió: Tanque Azul")
            Partida[0] = 1
        if vidaRojo[0] <= 0:
            print("Perdió: Tanque Rojo")
            Partida[0] = 2

        Pant.blit(mensaje, (500, 50))     
