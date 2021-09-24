from Juego.ClassOpciones import OpcionesCat
from Juego.claseTerreno import Terreno
from Juego.claseTanques import *
from .claseTanques import *
from pygame import *
import math,pygame,sys
from .Variables import XdeTankA, largo, ancho, Pant, mapa, Celeste, X_Tanque_Rojo, Y_Tanque_Rojo, X_Tanque_Azul, Y_Tanque_Azul, Turno, Partida, Velocidad_Azul, Angulo_Azul, Velocidad_Rojo, Angulo_Rojo

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

        # si sale de la pantalla reiniciar la posición (a inferior izq.)
        '''if (self.y > ancho) or (self.x > largo) or (self.y < 0) or (self.x < 0):
            self.x = 300
            self.y = 300
            self.tiempo = 0
            self.disparar = False
            print("Proyectil fuera de la pantalla. Tiro perdido.")'''

    # ------------------------------
    # Función principal del juego
    # ------------------------------

    def lanzamiento(aux):
        # se define la letra por defecto
        fuente = pygame.font.Font(None, 20)
        # se crea un proyectil a lanzar
        if Turno[0] == 1:
            #Tanque Azul
            angulo = Angulo_Azul[0]
            if angulo < 90:
                bala = Proyectil(X_Tanque_Azul[0]+20, Y_Tanque_Azul[0], Angulo_Azul[0], Velocidad_Azul[0])#velocidad,angulo
            if angulo == 90:
                bala = Proyectil(X_Tanque_Azul[0], Y_Tanque_Azul[0]-10, Angulo_Azul[0], Velocidad_Azul[0])#velocidad,angulo
            if angulo > 90:
                bala = Proyectil(X_Tanque_Azul[0]-20, Y_Tanque_Azul[0], Angulo_Azul[0], Velocidad_Azul[0])#velocidad,angulo

            pygame.key.set_repeat(1, 80)  # Activa repetición de teclas
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
                
            pygame.key.set_repeat(1, 80)  # Activa repetición de teclas
            clock = pygame.time.Clock()
            bala.disparar = aux
        # el bucle principal del juego
        while True:
            # registramos cuanto ha pasado desde el ultimo ciclo
            tick = clock.tick(60)
            # Posibles entradas del teclado y mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:
                        bala.disparar = True
                    if event.key == K_p:
                        OpcionesCat.pausa()
                    if event.key == K_ESCAPE:
                        salir=True
                        return salir
                        break
                    

            if bala.disparar is True:
                # al tiempo anterior le sumamos lo transcurrido
                bala.tiempo = bala.tiempo + (tick / 400.0)

            # Actualizar la posición e información
            bala.update(bala.xUsar,bala.yUsar)
            '''text = "Velocidad: %3d (m/s)   Angulo: %d   x=%d m   y=%d m" % (
                bala.veloc, bala.angulo, bala.xreal, bala.yreal)
            mensaje = fuente.render(text, 1, (255, 255, 255))

            # Re dibujar los elementos en pantalla
            Pant.blit(mensaje, (15, 5))
            pygame.draw.line(Pant, (255, 255, 255), (0, 25), (640, 25), 2)'''
            
            if bala.disparar == True:
                
                
                if (int(bala.y) == ancho) or (int(bala.x) == largo-1) or (int(bala.y) == 0) or (int(bala.x) == 0):
                        print("Tu disparo no sirvio")
                        bala.disparar = False
                        Terreno.dibuja_mapa(Pant,mapa)
                        if Turno[0] == 1:
                            Turno[0] = 2
                        elif Turno[0] == 2:
                            Turno[0] = 1
                        break

                elif mapa[int(bala.y)][int(bala.x)] == 0:
                    pygame.draw.circle(Pant, (0, 0, 0), (int(bala.x), int(bala.y)), 10)
                
                elif mapa[int(bala.y)+10][int(bala.x)] == 1 or mapa[int(bala.y)-10][int(bala.x)] == 1 or mapa[int(bala.y)][int(bala.x)+10] == 1 or mapa[int(bala.y)][int(bala.x)-10] == 1 or mapa[int(bala.y)+10][int(bala.x)+10] == 1 or mapa[int(bala.y)-10][int(bala.x)+10] == 1 or mapa[int(bala.y)-10][int(bala.x)-10] == 1 or mapa[int(bala.y)+10][int(bala.x)-10] == 1:

                    #########
                    if int(bala.y)+50 > ancho:

                        puta = ancho - int(bala.y)
                        print("Tu disparo no sirvio suma y")
                        bala.disparar = False
                        if mapa[int(bala.y)][int(bala.x)] == 1:
                            peo = int(bala.y)
                            pilin = int(bala.x)
                            while peo < int(bala.y)+40:
                                pilin = int(bala.x)
                                while pilin < int(bala.x)+80:
                                    if mapa[peo-40][pilin-40] == 2:
                                        #Si es 1 gana el rojo
                                        Partida[0] = 1
                                    elif mapa[peo-40][pilin-40] == 3:
                                        #Si es 2 gana el azul
                                        Partida[0] = 2
                                    mapa[peo-40][pilin-40] = 0
                                    pilin += 1
                                peo += 1


                            while peo < int(bala.y)+puta:
                                pilin = int(bala.x)
                                while pilin < int(bala.x)+80:
                                    mapa[peo-puta][pilin-40] = 0
                                    if mapa[peo-puta][pilin-40] == 2:
                                        #Si es 1 gana el rojo
                                        Partida[0] = 1
                                    elif mapa[peo-puta][pilin-40] == 3:
                                        #Si es 2 gana el azul
                                        Partida[0] = 2
                                    pilin += 1
                                peo += 1

                            bala.disparar = False

                            #bala = Proyectil(300, 300, angulo, velocidad)#velocidad,angulo
                            Terreno.dibuja_mapa(Pant,mapa)
                        if Turno[0] == 1:
                            Turno[0] = 2
                        elif Turno[0] == 2:
                            Turno[0] = 1
                        break
                    
                    ######
                    elif int(bala.x) + 50 > largo:
                        puta = largo - int(bala.x)
                        print("Tu disparo no sirvio suma x")
                        bala.disparar = False
                        if mapa[int(bala.y)][int(bala.x)] == 1:
                            peo = int(bala.y)
                            pilin = int(bala.x)
                            while peo < int(bala.y)+80:
                                pilin = int(bala.x)
                                while pilin < int(bala.x)+puta:
                                    
                                    mapa[peo-40][pilin-puta] = 0
                                    if mapa[peo-40][pilin-puta] == 2:
                                        #Si es 1 gana el rojo
                                        Partida[0] = 1
                                    elif mapa[peo-40][pilin-puta] == 3:
                                        #Si es 2 gana el azul
                                        Partida[0] = 2

                                    pilin += 1
                                peo += 1

                            bala.disparar = False
                            Terreno.dibuja_mapa(Pant,mapa)
                        if Turno[0] == 1:
                            Turno[0] = 2
                        elif Turno[0] == 2:
                            Turno[0] = 1
                        break

                    ###############
                    elif int(bala.y)-50 < 0:
                        puta = 0 - int(bala.y)
                        print("Tu disparo no sirvio resta y")
                        bala.disparar = False
                        if mapa[int(bala.y)][int(bala.x)] == 1:
                            peo = int(bala.y)
                            pilin = int(bala.x)
                            while peo < int(bala.y)+40:
                                pilin = int(bala.x)
                                while pilin < int(bala.x)+80:
                                    
                                    mapa[peo-40][pilin-40] = 0
                                    if mapa[peo-40][pilin-40] == 2:
                                        #Si es 1 gana el rojo
                                        Partida[0] = 1
                                    elif mapa[peo-40][pilin-40] == 3:
                                        #Si es 2 gana el azul
                                        Partida[0] = 2

                                    pilin += 1
                                peo += 1


                            while peo < int(bala.y)+puta:
                                pilin = int(bala.x)
                                while pilin < int(bala.x)+80:
                                    
                                    mapa[peo-puta][pilin-40] = 0
                                    if mapa[peo-puta][pilin-40] == 2:
                                        #Si es 1 gana el rojo
                                        Partida[0] = 1
                                    elif mapa[peo-puta][pilin-40] == 3:
                                        #Si es 2 gana el azul
                                        Partida[0] = 2

                                    pilin += 1
                                    
                                if mapa[peo-puta][pilin-40] == 2:
                                        break
                                elif mapa[peo-puta][pilin-40] == 3:
                                    break
                                peo += 1

                            bala.disparar = False

                            #bala = Proyectil(300, 300, angulo, velocidad)#velocidad,angulo
                            Terreno.dibuja_mapa(Pant,mapa)
                        if Turno[0] == 1:
                            Turno[0] = 2
                        elif Turno[0] == 2:
                            Turno[0] = 1
                        break

                    ##############
                    elif int(bala.x)-50 < 0:
                        puta = 0 - int(bala.x)
                        print("Tu disparo no sirvio resta x")
                        bala.disparar = False
                        if mapa[int(bala.y)][int(bala.x)] == 1:
                            peo = int(bala.y)
                            pilin = int(bala.x)
                            while peo < int(bala.y)+80:
                                pilin = int(bala.x)
                                while pilin < int(bala.x)-puta:

                                    if mapa[peo-40][pilin+puta] == 2:
                                        #Si es 1 gana el rojo
                                        Partida[0] = 1
                                    elif mapa[peo-40][pilin+puta] == 3:
                                        #Si es 2 gana el azul
                                        Partida[0] = 2

                                    mapa[peo-40][pilin+puta] = 0

                                    if mapa[peo-40][pilin-20] == 2:
                                        #Si es 1 gana el rojo
                                        Partida[0] = 1
                                    elif mapa[peo-40][pilin-20] == 3:
                                        #Si es 2 gana el azul
                                        Partida[0] = 2

                                    mapa[peo-40][pilin-20] = 0
                                    pilin += 1

                                if mapa[peo-40][pilin+puta] == 2:
                                    break
                                elif mapa[peo-40][pilin+puta] == 3:
                                    break
                                elif mapa[peo-40][pilin-20] == 2:
                                    break
                                elif mapa[peo-40][pilin-20] == 3:
                                    break
                                peo += 1

                            bala.disparar = False
                        if Turno[0] == 1:
                            Turno[0] = 2
                        elif Turno[0] == 2:
                            Turno[0] = 1
                        break


                    else:
                        pygame.draw.circle(Pant, Celeste, (int(bala.x), int(bala.y)), 10)
                        if mapa[int(bala.y)][int(bala.x)] == 1:
                            peo = int(bala.y)
                            pilin = int(bala.x)
                            while peo < int(bala.y)+80:
                                pilin = int(bala.x)
                                while pilin < int(bala.x)+80:
                                    if mapa[peo-40][pilin-40] == 2:
                                        #Si es 1 gana el rojo
                                        Partida[0] = 1
                                    elif mapa[peo-40][pilin-40] == 3:
                                        #Si es 2 gana el azul
                                        Partida[0] = 2
                                    mapa[peo-40][pilin-40] = 0
                                    pilin += 1
                                if mapa[peo-40][pilin-40] == 2:
                                    break
                                elif mapa[peo-40][pilin-40] == 3:
                                    break
                                peo += 1
                            
                            bala.disparar = False
                            #bala = Proyectil(300, 300, angulo, velocidad)#velocidad,angulo
                            Terreno.dibuja_mapa(Pant,mapa)
                            if Turno[0] == 1:
                                Turno[0] = 2
                            elif Turno[0] == 2:
                                Turno[0] = 1
                            break
            # actualizamos la pantalla
            pygame.display.flip()
