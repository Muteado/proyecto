import math,pygame
from .claseTerreno import Terreno
from .claseTanques import *
from .claseTanques import *
from .Variables import *
from .ClassEsquinas import *
from .ClaseBotones import *
from .PosicionTanque import posicion

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
            '''
            Lo "normal" sería false?
            if viento = true:
                x + la cant de viento
            '''
            self.xreal = (x + self.velocx * self.tiempo)
            '''
            Lo "normal sería 0?"
            if gravedad = true:
                y + o - la cant de gravedad
            '''
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

    def lanzamiento(botonamarillo,botonnaranja,botonmorado,aux):
        # se define la letra por defecto
        fuente = Textos.fuentes(None, 50)
        prueba = 0
        # se crea un proyectil a lanzar


        if Turno[0] == 1:
            #EleccionbalaAzul[0] = int(input("1. 105 mm \n2. perforante \n3. 60 mm \nIngrese su bala: "))
            if botonamarillo == True and balas[0] > 0:
                bala = Proyectil(X_Y_Tanques[0]+20, X_Y_Tanques[1], Angulo_Azul[0], Velocidad_Azul[0])#velocidad,angulo
                #pygame.key.set_repeat(1, 80)  # Activa repetición de teclas
                Balaaux[0] = 50
                balas[0] = balas[0] -1
                #Turno[0] = 2
                #print("Balas 105mm : ", balas)
                clock = pygame.time.Clock()
                bala.disparar = aux
                
                
            if botonnaranja == True and balas[1] > 0:
                bala = Proyectil(X_Y_Tanques[0]+20, X_Y_Tanques[1], Angulo_Azul[0], Velocidad_Azul[0])#velocidad,angulo
                #pygame.key.set_repeat(1, 80)  # Activa repetición de teclas
                Balaaux[0] = 40
                balas[1] = balas[1] - 1
                #print("Balas perforantes : ", balas)
                #Turno[0] = 2
                clock = pygame.time.Clock()
                bala.disparar = aux
                

            if botonmorado == True and balas[2] > 0:
                bala = Proyectil(X_Y_Tanques[0]+20, X_Y_Tanques[1], Angulo_Azul[0], Velocidad_Azul[0])#velocidad,angulo
                #pygame.key.set_repeat(1, 80)  # Activa repetición de teclas
                Balaaux[0] = 30
                balas[2] = balas[2] - 1
                #print("Balas 60 mm : ", balas)
                #Turno[0] = 2
                clock = pygame.time.Clock()
                bala.disparar = aux

            if balas[0] == 0 and balas[1] == 0 and balas[2] == 0:
                Textos.texto_pantalla_rect("Te quedaste sin balas!", Textos.fuentes(None, 40), Azul, Pant,500,50)
                #print("Te quedaste sin balas!")
                Turno[0] = 2

        if Turno[0] == 2:
            #EleccionbalaRojo[0] = int(input("1. 105 mm \n2. perforante \n3. 60 mm \nIngrese su bala: "))
            if botonamarillo == True and balas[3] > 0:
                bala = Proyectil(X_Y_Tanques[0]+20, X_Y_Tanques[1], Angulo_Rojo[0], Velocidad_Rojo[0])#velocidad,angulo
                #pygame.key.set_repeat(1, 80)  # Activa repetición de teclas
                Balaaux[0] = 50
                balas[3] = balas[3] -1
                #print("Balas 105mm : ", balas)
                #Turno[0] = 1
                clock = pygame.time.Clock()
                bala.disparar = aux
                

            if botonnaranja == True and balas[4] > 0:
                bala = Proyectil(X_Y_Tanques[0]+20, X_Y_Tanques[1], Angulo_Rojo[0], Velocidad_Rojo[0])#velocidad,angulo
                #pygame.key.set_repeat(1, 80)  # Activa repetición de teclas
                Balaaux[0] = 40
                balas[4] = balas[4] - 1
                #print("Balas perforantes : ", balas)
                #Turno[0] = 1
                clock = pygame.time.Clock()
                bala.disparar = aux
                

            if botonmorado == True and balas[5] > 0:
                bala = Proyectil(X_Y_Tanques[0]+20, X_Y_Tanques[1], Angulo_Rojo[0], Velocidad_Rojo[0])#velocidad,angulo
                #pygame.key.set_repeat(1, 80)  # Activa repetición de teclas
                Balaaux[0] = 30
                balas[5] = balas[5] - 1
                #print("Balas 60 mm : ", balas)
                #Turno[0] = 1
                clock = pygame.time.Clock()
                bala.disparar = aux
                
            
            if balas[3] == 0 and balas[4] == 0 and balas[5] == 0:
                Textos.texto_pantalla_rect("Te quedaste sin balas!", Textos.fuentes(None, 40), Rojo, Pant,500,50)
                #print("Te quedaste sin balas!")
                Turno[0] = 1


        if Turno[0] == 1:
            #Tanque Azul
            angulo = Angulo_Azul[0]
            if angulo < 90:
                bala = Proyectil(X_Y_Tanques[0]+10, X_Y_Tanques[1], Angulo_Azul[0], Velocidad_Azul[0])#velocidad,angulo
            if angulo == 90:
                bala = Proyectil(X_Y_Tanques[0], X_Y_Tanques[1]-10, Angulo_Azul[0], Velocidad_Azul[0])#velocidad,angulo
            if angulo > 90:
                bala = Proyectil(X_Y_Tanques[0]-10, X_Y_Tanques[1], Angulo_Azul[0], Velocidad_Azul[0])#velocidad,angulo

            clock = pygame.time.Clock()
            bala.disparar = aux
            
        elif Turno[0] == 2:
            #Tanque Rojo
            angulo = Angulo_Rojo[0]
            if angulo < 90:
                bala = Proyectil(X_Y_Tanques[2]+20, X_Y_Tanques[3], Angulo_Rojo[0], Velocidad_Rojo[0])#velocidad,angulo
            if angulo == 90:
                bala = Proyectil(X_Y_Tanques[2], X_Y_Tanques[3]-10, Angulo_Rojo[0], Velocidad_Rojo[0])#velocidad,angulo
            if angulo > 90:
                bala = Proyectil(X_Y_Tanques[2]-20, X_Y_Tanques[3], Angulo_Rojo[0], Velocidad_Rojo[0])#velocidad,angulo
                
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
                    text = "Metros = %d m   Altura = %d m" % (
                        XdelTank[0]-bala.xreal, prueba)
                elif Angulo_Azul[0] < 90:
                    text = "Metros = %d m   Altura = %d m" % (
                        bala.xreal-XdelTank[0], prueba)
            if Turno[0] == 2:
                if Angulo_Rojo[0] >= 90:
                    text = "Metros = %d m   Altura = %d m" % (
                        XdelTank[1]-bala.xreal, prueba)
                elif Angulo_Rojo[0] < 90:
                    text = "Metros = %d m   Altura = %d m" % (
                        bala.xreal-XdelTank[1], prueba)

            mensaje = fuente.render(text, 600, Negro)
            
            fuente = pygame.font.Font(None,50)
            
            
            if bala.disparar == True:
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
                        if mapa[int(bala.y)][int(bala.x)+10] == 2 or mapa[int(bala.y)][int(bala.x)-10] == 2 or mapa[int(bala.y)+10][int(bala.x)] == 2 or mapa[int(bala.y)-10][int(bala.x)] == 2:
                            print("cayó en el tanque azul")
                            #Partida[0] = 1
                            
                            #bala.disparar = False
                            #bala = Proyectil(300, 300, angulo, velocidad)#velocidad,angulo
                            Terreno.dibuja_mapa(Pant,mapa)
                            
                            
                            if vidaTank[0] > 0:
                                if Turno[0] == 1:
                                    vidaTank[0] = vidaTank[0] - Balaaux[0]
                                    #print("La vida del Azul es: ",vidaTank[0])
                                    Turno[0] = 2
                                    break
                                if Turno[0] == 2:
                                    vidaTank[0] = vidaTank[0] - Balaaux[0]
                                    #print("La vida del Azul es: ",vidaTank[0])
                                    Turno[0] = 1
                                    break

                        #Valido si la bala impactó con el tanque rojo
                        elif mapa[int(bala.y)][int(bala.x)+10] == 3 or mapa[int(bala.y)][int(bala.x)-10] == 3 or mapa[int(bala.y)+10][int(bala.x)] == 3 or mapa[int(bala.y)-10][int(bala.x)] == 3:
                            print("cayó en el tanque rojo")
                            #Partida[0] = 2
                            
                            #bala.disparar = False
                            #bala = Proyectil(300, 300, angulo, velocidad)#velocidad,angulo
                            Terreno.dibuja_mapa(Pant,mapa)
                            
                            
                            if vidaTank[1] > 0:
                                if Turno[0] == 1:
                                    vidaTank[1] = vidaTank[1] - Balaaux[0]
                                    #print("La vida del rojo es: ",vidaTank[1])
                                    Turno[0] = 2
                                    break
                                if Turno[0] == 2:
                                    vidaTank[1] = vidaTank[1] - Balaaux[0]
                                    #print("La vida del rojo es: ",vidaTank[1])
                                    Turno[0] = 1
                                    break

                        #Se valida que la bala haya impactado en el terreno
                        elif mapa[int(bala.y)][int(bala.x)+10] == 1 or mapa[int(bala.y)][int(bala.x)-10] == 1 or mapa[int(bala.y)+10][int(bala.x)] == 1:
                            pygame.draw.circle(Pant, Amarillo, (int(bala.x), int(bala.y)), 10)
                            #se hacen el hoyo de la bala 105
                            aux2 = -2
                            aux1 = -2

                            while aux1 <= 50:
                                while aux2 <= 40:
                                    if (int(bala.y)+aux1) < ancho:
                                        if (int(bala.x)+aux2 < largo):
                                            if mapa[int(bala.y)+aux1][int(bala.x)+aux2] != 2 and mapa[int(bala.y)+aux1][int(bala.x)+aux2] != 3:
                                                mapa[int(bala.y)+aux1][int(bala.x)+aux2] = 0
                                        if (int(bala.x)-aux2 < largo):
                                            if mapa[int(bala.y)+aux1][int(bala.x)-aux2] != 2 and mapa[int(bala.y)+aux1][int(bala.x)-aux2] != 3:
                                                mapa[int(bala.y)+aux1][int(bala.x)-aux2] = 0
                                    aux2 += 1

                                aux2 = 0
                                aux1 += 1

                            pygame.display.update()
                            print("cayó en el suelo")
                            bala.disparar = False
                            
                            Terreno.dibuja_mapa(Pant,mapa)
                            if Turno[0] == 1:
                                Turno[0] = 2
                            elif Turno[0] == 2:
                                Turno[0] = 1
                            break

                        #Se valida que la bala vaya por el aire y así siga su trayecto
                        elif mapa[int(bala.y)][int(bala.x)+10] == 0 or mapa[int(bala.y)+10][int(bala.x)] == 0 or mapa[int(bala.y)][int(bala.x)-10] == 0:
                            pygame.draw.circle(Pant, Amarillo, (int(bala.x), int(bala.y)), 10)
                            pygame.display.update()

                    
                    #Es el turno del jugador rojo
                    elif Turno[0] == 2:

                        #Valida si impacta en el tanque azul
                        if mapa[int(bala.y)][int(bala.x)+10] == 2 or mapa[int(bala.y)+10][int(bala.x)] == 2:
                            print("cayó en el tanque azul")
                            #Partida[0] = 1
                            
                            #bala.disparar = False
                            #bala = Proyectil(300, 300, angulo, velocidad)#velocidad,angulo
                            Terreno.dibuja_mapa(Pant,mapa)
                            
                            
                            if vidaTank[0] > 0:
                                if Turno[0] == 1:
                                    vidaTank[0] = vidaTank[0] - Balaaux[0]
                                    #print("La vida del Azul es: ",vidaTank[0])
                                    Turno[0] = 2
                                    break
                                if Turno[0] == 2:
                                    vidaTank[0] = vidaTank[0] - Balaaux[0]
                                    #print("La vida del Azul es: ",vidaTank[0])
                                    Turno[0] = 1
                                    break

                        #Valido si la bala impactó con el tanque rojo
                        elif mapa[int(bala.y)][int(bala.x)+10] == 3 or mapa[int(bala.y)+10][int(bala.x)] == 3:
                            print("cayó en el tanque rojo")
                            #Partida[0] = 2
                            
                            #bala.disparar = False
                            #bala = Proyectil(300, 300, angulo, velocidad)#velocidad,angulo
                            Terreno.dibuja_mapa(Pant,mapa)
                            
                            
                            if vidaTank[1] > 0:
                                if Turno[0] == 1:
                                    vidaTank[1] = vidaTank[1] - Balaaux[0]
                                    #print("La vida del rojo es: ",vidaTank[1])
                                    Turno[0] = 2
                                    break
                                if Turno[0] == 2:
                                    vidaTank[1] = vidaTank[1] - Balaaux[0]
                                    #print("La vida del rojo es: ",vidaTank[1])
                                    Turno[0] = 1
                                    break
                        
                        #Se valida que la bala haya impactado en el terreno
                        elif mapa[int(bala.y)][int(bala.x)+10] == 1 or mapa[int(bala.y)+10][int(bala.x)] == 1 or mapa[int(bala.y)][int(bala.x)-10] == 1: 
                            pygame.draw.circle(Pant, Amarillo, (int(bala.x), int(bala.y)), 10)

                            #se hacen el hoyo de la bala 105
                            aux2 = -2
                            aux1 = -2

                            while aux1 <= 50:
                                while aux2 <= 40:
                                    if (int(bala.y)+aux1) < ancho:
                                        if (int(bala.x)+aux2 < largo):
                                            if mapa[int(bala.y)+aux1][int(bala.x)+aux2] != 2 and mapa[int(bala.y)+aux1][int(bala.x)+aux2] != 3:
                                                mapa[int(bala.y)+aux1][int(bala.x)+aux2] = 0
                                        if (int(bala.x)-aux2 < largo):
                                            if mapa[int(bala.y)+aux1][int(bala.x)-aux2] != 2 and mapa[int(bala.y)+aux1][int(bala.x)-aux2] != 3:
                                                mapa[int(bala.y)+aux1][int(bala.x)-aux2] = 0
                                    aux2 += 1

                                aux2 = 0
                                aux1 += 1

                            pygame.display.update()
                            print("cayó en el suelo")
                            bala.disparar = False
                            
                            Terreno.dibuja_mapa(Pant,mapa)
                            if Turno[0] == 1:
                                Turno[0] = 2
                            elif Turno[0] == 2:
                                Turno[0] = 1
                            break

                        #Se valida que la bala vaya por el aire y así siga su trayecto
                        elif mapa[int(bala.y)][int(bala.x)+10] == 0 or mapa[int(bala.y)+10][int(bala.x)] == 0  or mapa[int(bala.y)][int(bala.x)-10] == 0:
                            pygame.draw.circle(Pant, Amarillo, (int(bala.x), int(bala.y)), 10)
                            pygame.display.update()


                #Se valida si la bala perforante impactó en el terreno
                elif botonnaranja == True:
                    if Turno[0] == 1:

                        #Valida si impacta en el tanque azul
                        if mapa[int(bala.y)][int(bala.x)+7] == 2 or mapa[int(bala.y)+7][int(bala.x)] == 2 or mapa[int(bala.y)][int(bala.x)-7] == 2:
                            print("cayó en el tanque azul")
                            #Partida[0] = 1
                            
                            #bala.disparar = False
                            #bala = Proyectil(300, 300, angulo, velocidad)#velocidad,angulo
                            Terreno.dibuja_mapa(Pant,mapa)
                            
                            
                            if vidaTank[0] > 0:
                                if Turno[0] == 1:
                                    vidaTank[0] = vidaTank[0] - Balaaux[0]
                                    #print("La vida del Azul es: ",vidaTank[0])
                                    Turno[0] = 2
                                    break
                                if Turno[0] == 2:
                                    vidaTank[0] = vidaTank[0] - Balaaux[0]
                                    #print("La vida del Azul es: ",vidaTank[0])
                                    Turno[0] = 1
                                    break

                        #Valido si la bala impactó con el tanque rojo
                        elif mapa[int(bala.y)][int(bala.x)+7] == 3 or mapa[int(bala.y)+7][int(bala.x)] == 3 or mapa[int(bala.y)][int(bala.x)-7] == 3:
                            print("cayó en el tanque rojo")
                            #Partida[0] = 2
                            
                            #bala.disparar = False
                            #bala = Proyectil(300, 300, angulo, velocidad)#velocidad,angulo
                            Terreno.dibuja_mapa(Pant,mapa)
                            
                            
                            if vidaTank[1] > 0:
                                if Turno[0] == 1:
                                    vidaTank[1] = vidaTank[1] - Balaaux[0]
                                    #print("La vida del rojo es: ",vidaTank[1])
                                    Turno[0] = 2
                                    break
                                if Turno[0] == 2:
                                    vidaTank[1] = vidaTank[1] - Balaaux[0]
                                    #print("La vida del rojo es: ",vidaTank[1])
                                    Turno[0] = 1
                                    break

                        #Se valida que la bala haya impactado en el terreno
                        elif mapa[int(bala.y)][int(bala.x)+7] == 1 or mapa[int(bala.y)+7][int(bala.x)] == 1 or mapa[int(bala.y)][int(bala.x)-7] == 1:

                            pygame.draw.circle(Pant, Naranja, (int(bala.x), int(bala.y)), 7)

                            #se hacen el hoyo de la bala perforante
                            aux2 = -2
                            aux1 = -2

                            while aux1 <= 40:
                                while aux2 <= 30:
                                    if (int(bala.y)+aux1) < ancho:
                                        if (int(bala.x)+aux2 < largo):
                                            if mapa[int(bala.y)+aux1][int(bala.x)+aux2] != 2 and mapa[int(bala.y)+aux1][int(bala.x)+aux2] != 3:
                                                mapa[int(bala.y)+aux1][int(bala.x)+aux2] = 0
                                        if (int(bala.x)-aux2 < largo):
                                            if mapa[int(bala.y)+aux1][int(bala.x)-aux2] != 2 and mapa[int(bala.y)+aux1][int(bala.x)-aux2] != 3:
                                                mapa[int(bala.y)+aux1][int(bala.x)-aux2] = 0
                                    aux2 += 1

                                aux2 = 0
                                aux1 += 1

                            pygame.display.update()
                            print("cayó en el suelo")
                            bala.disparar = False
                            
                            Terreno.dibuja_mapa(Pant,mapa)
                            if Turno[0] == 1:
                                Turno[0] = 2
                            elif Turno[0] == 2:
                                Turno[0] = 1
                            break

                            #Se valida que la bala vaya por el aire y así siga su trayecto
                        elif mapa[int(bala.y)][int(bala.x)+7] == 0 or mapa[int(bala.y)+7][int(bala.x)] == 0 or mapa[int(bala.y)][int(bala.x)-7] == 0:
                            pygame.draw.circle(Pant, Naranja, (int(bala.x), int(bala.y)), 7)
                            pygame.display.update()

                    
                    elif Turno[0] == 2:

                        

                        #Valida si impacta en el tanque azul
                        if mapa[int(bala.y)][int(bala.x)+7] == 2 or mapa[int(bala.y)+7][int(bala.x)] == 2 or mapa[int(bala.y)][int(bala.x)-7] == 2:
                            print("cayó en el tanque azul")
                            #Partida[0] = 1
                            
                            #bala.disparar = False
                            #bala = Proyectil(300, 300, angulo, velocidad)#velocidad,angulo
                            Terreno.dibuja_mapa(Pant,mapa)
                            
                            
                            if vidaTank[0] > 0:
                                if Turno[0] == 1:
                                    vidaTank[0] = vidaTank[0] - Balaaux[0]
                                    #print("La vida del Azul es: ",vidaTank[0])
                                    Turno[0] = 2
                                    break
                                if Turno[0] == 2:
                                    vidaTank[0] = vidaTank[0] - Balaaux[0]
                                    #print("La vida del Azul es: ",vidaTank[0])
                                    Turno[0] = 1
                                    break

                        #Valido si la bala impactó con el tanque rojo
                        elif mapa[int(bala.y)][int(bala.x)+7] == 3 or mapa[int(bala.y)+7][int(bala.x)] == 3 or mapa[int(bala.y)][int(bala.x)-7] == 3:
                            print("cayó en el tanque rojo")
                            #Partida[0] = 2
                            
                            #bala.disparar = False
                            #bala = Proyectil(300, 300, angulo, velocidad)#velocidad,angulo
                            Terreno.dibuja_mapa(Pant,mapa)
                            
                            
                            if vidaTank[1] > 0:
                                if Turno[0] == 1:
                                    vidaTank[1] = vidaTank[1] - Balaaux[0]
                                    #print("La vida del rojo es: ",vidaTank[1])
                                    Turno[0] = 2
                                    break
                                if Turno[0] == 2:
                                    vidaTank[1] = vidaTank[1] - Balaaux[0]
                                    #print("La vida del rojo es: ",vidaTank[1])
                                    Turno[0] = 1
                                    break

                        #Se valida que la bala haya impactado en el terreno
                        elif mapa[int(bala.y)][int(bala.x)+7] == 1 or mapa[int(bala.y)+7][int(bala.x)] == 1 or mapa[int(bala.y)][int(bala.x)-7] == 1:
                            pygame.draw.circle(Pant, Naranja, (int(bala.x), int(bala.y)), 7)

                            #se hacen el hoyo de la bala perforante
                            aux2 = -2
                            aux1 = -2

                            while aux1 <= 40:
                                while aux2 <= 30:
                                    if (int(bala.y)+aux1) < ancho:
                                        if (int(bala.x)+aux2 < largo):
                                            if mapa[int(bala.y)+aux1][int(bala.x)+aux2] != 2 and mapa[int(bala.y)+aux1][int(bala.x)+aux2] != 3:
                                                mapa[int(bala.y)+aux1][int(bala.x)+aux2] = 0
                                        if (int(bala.x)-aux2 < largo):
                                            if mapa[int(bala.y)+aux1][int(bala.x)-aux2] != 2 and mapa[int(bala.y)+aux1][int(bala.x)-aux2] != 3:
                                                mapa[int(bala.y)+aux1][int(bala.x)-aux2] = 0
                                    aux2 += 1

                                aux2 = 0
                                aux1 += 1
                            
                            pygame.display.update()
                            print("cayó en el suelo")
                            bala.disparar = False
                            
                            Terreno.dibuja_mapa(Pant,mapa)
                            if Turno[0] == 1:
                                Turno[0] = 2
                            elif Turno[0] == 2:
                                Turno[0] = 1
                            break

                        #Se valida que la bala vaya por el aire y así siga su trayecto
                        elif mapa[int(bala.y)][int(bala.x)+7] == 0 or mapa[int(bala.y)-7][int(bala.x)] == 0 or mapa[int(bala.y)][int(bala.x)-7] == 0:
                            pygame.draw.circle(Pant, Naranja, (int(bala.x), int(bala.y)), 7)
                            pygame.display.update()

                
                #Se valida si la bala 60 mm impactó en el terreno
                elif botonmorado == True:
                    if Turno[0] == 1:

                        #Valida si impacta en el tanque azul
                        if mapa[int(bala.y)][int(bala.x)+5] == 2 or mapa[int(bala.y)+5][int(bala.x)] == 2 or mapa[int(bala.y)][int(bala.x)-5] == 2:
                            print("cayó en el tanque azul")
                            #Partida[0] = 1
                            
                            #bala.disparar = False
                            #bala = Proyectil(300, 300, angulo, velocidad)#velocidad,angulo
                            Terreno.dibuja_mapa(Pant,mapa)
                            
                            
                            if vidaTank[0] > 0:
                                if Turno[0] == 1:
                                    vidaTank[0] = vidaTank[0] - Balaaux[0]
                                    #print("La vida del Azul es: ",vidaTank[0])
                                    Turno[0] = 2
                                    break
                                if Turno[0] == 2:
                                    vidaTank[0] = vidaTank[0] - Balaaux[0]
                                    #print("La vida del Azul es: ",vidaTank[0])
                                    Turno[0] = 1
                                    break
                        
                        #Valido si la bala impactó con el tanque rojo
                        elif mapa[int(bala.y)][int(bala.x)+5] == 3 or mapa[int(bala.y)+5][int(bala.x)] == 3 or mapa[int(bala.y)][int(bala.x)-5] == 3:
                            print("cayó en el tanque rojo")
                            #Partida[0] = 2
                            
                            #bala.disparar = False
                            #bala = Proyectil(300, 300, angulo, velocidad)#velocidad,angulo
                            Terreno.dibuja_mapa(Pant,mapa)
                            
                            
                            if vidaTank[1] > 0:
                                if Turno[0] == 1:
                                    vidaTank[1] = vidaTank[1] - Balaaux[0]
                                    #print("La vida del rojo es: ",vidaTank[1])
                                    Turno[0] = 2
                                    break
                                if Turno[0] == 2:
                                    vidaTank[1] = vidaTank[1] - Balaaux[0]
                                    #print("La vida del rojo es: ",vidaTank[1])
                                    Turno[0] = 1
                                    break

                        #Se valida que la bala haya impactado en el terreno
                        elif mapa[int(bala.y)][int(bala.x)+5] == 1 or mapa[int(bala.y)+5][int(bala.x)] == 1 or mapa[int(bala.y)][int(bala.x)-5] == 1:
                            pygame.draw.circle(Pant, Morado, (int(bala.x), int(bala.y)), 5)

                            #se hacen el hoyo de la bala 60
                            aux2 = -2
                            aux1 = -2

                            while aux1 <= 30:
                                while aux2 <= 20:
                                    if (int(bala.y)+aux1) < ancho:
                                        if (int(bala.x)+aux2 < largo):
                                            if mapa[int(bala.y)+aux1][int(bala.x)+aux2] != 2 and mapa[int(bala.y)+aux1][int(bala.x)+aux2] != 3:
                                                mapa[int(bala.y)+aux1][int(bala.x)+aux2] = 0
                                        if (int(bala.x)-aux2 < largo):
                                            if mapa[int(bala.y)+aux1][int(bala.x)-aux2] != 2 and mapa[int(bala.y)+aux1][int(bala.x)-aux2] != 3:
                                                mapa[int(bala.y)+aux1][int(bala.x)-aux2] = 0
                                    aux2 += 1

                                aux2 = 0
                                aux1 += 1

                            pygame.display.update()
                            print("cayó en el suelo")
                            bala.disparar = False

                            Terreno.dibuja_mapa(Pant,mapa)
                            if Turno[0] == 1:
                                Turno[0] = 2
                            elif Turno[0] == 2:
                                Turno[0] = 1
                            break

                        #Se valida que la bala vaya por el aire y así siga su trayecto
                        elif mapa[int(bala.y)][int(bala.x)+5] == 0 or mapa[int(bala.y)+5][int(bala.x)] == 0 or mapa[int(bala.y)][int(bala.x)-5] == 0:
                            pygame.draw.circle(Pant, Morado, (int(bala.x), int(bala.y)), 5)
                            pygame.display.update()


                    elif Turno[0] == 2:

                            
                        #Valida si impacta en el tanque azul
                        if mapa[int(bala.y)][int(bala.x)+5] == 2 or mapa[int(bala.y)+5][int(bala.x)] == 2 or mapa[int(bala.y)][int(bala.x)-5] == 2:
                            print("cayó en el tanque azul")
                            #Partida[0] = 1
                            
                            #bala.disparar = False
                            #bala = Proyectil(300, 300, angulo, velocidad)#velocidad,angulo
                            Terreno.dibuja_mapa(Pant,mapa)
                            
                            
                            if vidaTank[0] > 0:
                                if Turno[0] == 1:
                                    vidaTank[0] = vidaTank[0] - Balaaux[0]
                                    #print("La vida del Azul es: ",vidaTank[0])
                                    Turno[0] = 2
                                    break
                                if Turno[0] == 2:
                                    vidaTank[0] = vidaTank[0] - Balaaux[0]
                                    #print("La vida del Azul es: ",vidaTank[0])
                                    Turno[0] = 1
                                    break

                        #Valido si la bala impactó con el tanque rojo
                        elif mapa[int(bala.y)][int(bala.x)+5] == 3 or mapa[int(bala.y)+5][int(bala.x)] == 3 or mapa[int(bala.y)][int(bala.x)-5] == 3:
                            print("cayó en el tanque rojo")
                            #Partida[0] = 2
                            
                            #bala.disparar = False
                            #bala = Proyectil(300, 300, angulo, velocidad)#velocidad,angulo
                            Terreno.dibuja_mapa(Pant,mapa)
                            
                            
                            if vidaTank[1] > 0:
                                if Turno[0] == 1:
                                    vidaTank[1] = vidaTank[1] - Balaaux[0]
                                    #print("La vida del rojo es: ",vidaTank[1])
                                    Turno[0] = 2
                                    break
                                if Turno[0] == 2:
                                    vidaTank[1] = vidaTank[1] - Balaaux[0]
                                    #print("La vida del rojo es: ",vidaTank[1])
                                    Turno[0] = 1
                                    break
                        
                        #Se valida que la bala haya impactado en el terreno
                        elif mapa[int(bala.y)][int(bala.x)+5] == 1 or mapa[int(bala.y)+5][int(bala.x)] == 1 or mapa[int(bala.y)][int(bala.x)-5] == 1:
                            pygame.draw.circle(Pant, Morado, (int(bala.x), int(bala.y)), 5)

                            #se hacen el hoyo de la bala 60
                            aux2 = -2
                            aux1 = -2

                            while aux1 <= 30:
                                while aux2 <= 20:
                                    if (int(bala.y)+aux1) < ancho:
                                        if (int(bala.x)+aux2 < largo):
                                            if mapa[int(bala.y)+aux1][int(bala.x)+aux2] != 2 and mapa[int(bala.y)+aux1][int(bala.x)+aux2] != 3:
                                                mapa[int(bala.y)+aux1][int(bala.x)+aux2] = 0
                                        if (int(bala.x)-aux2 < largo):
                                            if mapa[int(bala.y)+aux1][int(bala.x)-aux2] != 2 and mapa[int(bala.y)+aux1][int(bala.x)-aux2] != 3:
                                                mapa[int(bala.y)+aux1][int(bala.x)-aux2] = 0
                                    aux2 += 1

                                aux2 = 0
                                aux1 += 1

                            pygame.display.update()
                            print("cayó en el suelo")
                            bala.disparar = False
                            
                            Terreno.dibuja_mapa(Pant,mapa)
                            if Turno[0] == 1:
                                Turno[0] = 2
                            elif Turno[0] == 2:
                                Turno[0] = 1
                            break

                        #Se valida que la bala vaya por el aire y así siga su trayecto
                        elif mapa[int(bala.y)][int(bala.x)+5] == 0 or mapa[int(bala.y)+5][int(bala.x)] == 0 or mapa[int(bala.y)][int(bala.x)-5] == 0:
                            pygame.draw.circle(Pant, Morado, (int(bala.x), int(bala.y)), 5)
                            pygame.display.update()
    
                       
                    
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
