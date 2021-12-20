from .Variables import *
from .Proyectil import *
from .Terreno import Terreno
from .Esquinas import *

class Movimiento:
    def angulos(jugador):

        if jugador.get_Angulo() < 90:
            bala = Proyectil(jugador.get_X()+10, jugador.get_Y(), jugador.get_Angulo(), jugador.get_Velocidad())#velocidad,angulo
    
        if jugador.get_Angulo() == 90:
            bala = Proyectil(jugador.get_X(), jugador.get_X()-10, jugador.get_Angulo(), jugador.get_Velocidad())#velocidad,angulo
    
        if jugador.get_Angulo() > 90:
            bala = Proyectil(jugador.get_X()-10, jugador.get_X(), jugador.get_Angulo(), jugador.get_Velocidad())#velocidad,angulo
    
        bala.disparar = aux
        clock = pygame.time.Clock()
        bala.disparar=True
        return bala.disparar

        
    def validaimpactos(diferencia,bala,balaaux,jugador):
        Pant = pygame.display.set_mode([(largo[1]),(ancho[1])])
        if mapa[int(bala.y)][int(bala.x)+diferencia] == jugador.color or mapa[int(bala.y)][int(bala.x)-diferencia] == jugador.color or mapa[int(bala.y)+diferencia][int(bala.x)] == jugador.color or mapa[int(bala.y)-diferencia][int(bala.x)] == jugador.color:
 
            Terreno.dibuja_mapa(Pant,mapa)
             
            if jugador.get_Vida() > 0:
                jugador.set_Vida(jugador.get_Vida() - balaaux)

            return(False)

        #Se valida que la bala haya impactado en el terreno
        elif mapa[int(bala.y)][int(bala.x)+diferencia] == 1 or mapa[int(bala.y)][int(bala.x)-diferencia] == 1 or mapa[int(bala.y)+diferencia][int(bala.x)] == 1:
            pygame.draw.circle(Pant, Amarillo, (int(bala.x), int(bala.y)), diferencia)
            #se hacen el hoyo de la bala diferencia
            aux2 = -2
            aux1 = -2

            while aux1 <= 50:
                while aux2 <= 40:
                    if (int(bala.y)+aux1) < ancho:
                        if (int(bala.x)+aux2 < largo[0]):
                            if mapa[int(bala.y)+aux1][int(bala.x)+aux2] != jugador.color and mapa[int(bala.y)+aux1][int(bala.x)+aux2] != jugador.color:
                                mapa[int(bala.y)+aux1][int(bala.x)+aux2] = 0
                        if (int(bala.x)-aux2 < largo[0]):
                            if mapa[int(bala.y)+aux1][int(bala.x)-aux2] != jugador.color and mapa[int(bala.y)+aux1][int(bala.x)-aux2] != jugador.color:
                                mapa[int(bala.y)+aux1][int(bala.x)-aux2] = 0
                    aux2 += 1

                aux2 = 0
                aux1 += 1

            pygame.display.update()
            print("cayó en el suelo")
            bala.disparar = False
            
            Terreno.dibuja_mapa(Pant,mapa)

            return(False)
            

        #Se valida que la bala vaya por el aire y así siga su trayecto
        elif mapa[int(bala.y)][int(bala.x)+diferencia] == 0 or mapa[int(bala.y)+diferencia][int(bala.x)] == 0 or mapa[int(bala.y)][int(bala.x)-diferencia] == 0:
            pygame.draw.circle(Pant, Amarillo, (int(bala.x), int(bala.y)), diferencia)
            pygame.display.update()
            return(True)