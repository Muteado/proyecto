from Juego.ClassOpciones import OpcionesCat
from Juego.claseTerreno import Terreno
from pygame import *
import math,pygame,sys
from .Variables import largo, ancho, Pant, mapa, Celeste

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
        if (self.y > ancho) or (self.x > largo) or (self.y < 0) or (self.x < 0):
            self.x = 0
            self.y = ancho
            self.tiempo = 0
            self.disparar = False
            print("Proyectil fuera de la pantalla. Tiro perdido.")

    # ------------------------------
    # Función principal del juego
    # ------------------------------

    def lanzamiento(aux):
        # se define la letra por defecto
        fuente = pygame.font.Font(None, 20)
        # se crea un proyectil a lanzar
        angulo = int(input('Ingrese angulo bala: '))
        velocidad = int(input('Ingrese velocidad bala: '))
        bala = Proyectil(100, 300, angulo, velocidad)#velocidad,angulo
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
                bala.tiempo = bala.tiempo + (tick / 250.0)

            # Actualizar la posición e información
            bala.update(100,bala.yUsar)
            '''text = "Velocidad: %3d (m/s)   Angulo: %d   x=%d m   y=%d m" % (
                bala.veloc, bala.angulo, bala.xreal, bala.yreal)
            mensaje = fuente.render(text, 1, (255, 255, 255))

            # Re dibujar los elementos en pantalla
            Pant.blit(mensaje, (15, 5))
            pygame.draw.line(Pant, (255, 255, 255), (0, 25), (640, 25), 2)'''
            
            if bala.disparar == True:
                if mapa[int(bala.y)][int(bala.x)] == 0:
                    pygame.draw.circle(Pant, (0, 0, 0), (int(bala.x), int(bala.y)), 10)
                
                elif (bala.y > ancho) or (bala.x > largo) or (bala.y < 0) or (bala.x < 0):
                        print("Tu disparo no sirvio")
                        bala.disparar = False
                
                elif mapa[int(bala.y)+10][int(bala.x)] == 1 or mapa[int(bala.y)-10][int(bala.x)] == 1 or mapa[int(bala.y)][int(bala.x)+10] == 1 or mapa[int(bala.y)][int(bala.x)-10] == 1:
                    if bala.y+50 > ancho:
                        print("Tu disparo no sirvio")
                        bala.disparar = False
                    if bala.x + 50 > largo:
                        print("Tu disparo no sirvio")
                        bala.disparar = False
                    else:
                        pygame.draw.circle(Pant, Celeste, (int(bala.x), int(bala.y)), 10)
                        if mapa[int(bala.y)][int(bala.x)] == 1:
                            peo = int(bala.y)
                            pilin = int(bala.x)
                            while peo < int(bala.y)+80:
                                pilin = int(bala.x)
                                while pilin < int(bala.x)+80:
                                    mapa[peo-40][pilin-40] = 0
                                    pilin += 1
                                peo += 1
                            bala.disparar = False
                            #bala = Proyectil(300, 300, angulo, velocidad)#velocidad,angulo
                            Terreno.dibuja_mapa(Pant,mapa)
            # actualizamos la pantalla
            pygame.display.flip()
