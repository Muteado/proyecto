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
        if mapa[int(bala.y)][int(bala.x)+diferencia] == jugador1.color or mapa[int(bala.y)][int(bala.x)-diferencia] == jugador1.color or mapa[int(bala.y)+diferencia][int(bala.x)] == jugador1.color or mapa[int(bala.y)-diferencia][int(bala.x)] == jugador1.color:
 
            Terreno.dibuja_mapa(Pant,mapa)
            
            if jugador1.get_Vida() > 0:
                jugador1.set_Vida(jugador1.get_Vida() - balaaux)
            else:
                if(jugador == jugador1):
                    jugador.set_Kill(-1)
                else:
                    jugador.set_Kill(1)
            return(False)

        elif mapa[int(bala.y)][int(bala.x)+diferencia] == jugador2.color or mapa[int(bala.y)][int(bala.x)-diferencia] == jugador2.color or mapa[int(bala.y)+diferencia][int(bala.x)] == jugador2.color or mapa[int(bala.y)-diferencia][int(bala.x)] == jugador2.color:
     
            Terreno.dibuja_mapa(Pant,mapa)
            
            if jugador2.get_Vida() > 0:
                jugador2.set_Vida(jugador2.get_Vida() - balaaux)
            else:
                if(jugador == jugador2):
                    jugador.set_Kill(-1)
                else:
                    jugador.set_Kill(1)
            return(False)
        
        elif mapa[int(bala.y)][int(bala.x)+diferencia] == jugador3.color or mapa[int(bala.y)][int(bala.x)-diferencia] == jugador3.color or mapa[int(bala.y)+diferencia][int(bala.x)] == jugador3.color or mapa[int(bala.y)-diferencia][int(bala.x)] == jugador3.color:
         
            Terreno.dibuja_mapa(Pant,mapa)
            
            if jugador3.get_Vida() > 0:
                jugador3.set_Vida(jugador3.get_Vida() - balaaux)
            else:
                if(jugador == jugador3):
                    jugador.set_Kill(-1)
                else:
                    jugador.set_Kill(1)
            return(False)

        elif mapa[int(bala.y)][int(bala.x)+diferencia] == jugador4.color or mapa[int(bala.y)][int(bala.x)-diferencia] == jugador4.color or mapa[int(bala.y)+diferencia][int(bala.x)] == jugador4.color or mapa[int(bala.y)-diferencia][int(bala.x)] == jugador4.color:
             
            Terreno.dibuja_mapa(Pant,mapa)
            
            if jugador4.get_Vida() > 0:
                jugador4.set_Vida(jugador4.get_Vida() - balaaux)
            else:
                if(jugador == jugador4):
                    jugador.set_Kill(-1)
                else:
                    jugador.set_Kill(1)
            return(False)
        
        elif mapa[int(bala.y)][int(bala.x)+diferencia] == jugador5.color or mapa[int(bala.y)][int(bala.x)-diferencia] == jugador5.color or mapa[int(bala.y)+diferencia][int(bala.x)] == jugador5.color or mapa[int(bala.y)-diferencia][int(bala.x)] == jugador5.color:
             
            Terreno.dibuja_mapa(Pant,mapa)
            
            if jugador5.get_Vida() > 0:
                jugador5.set_Vida(jugador5.get_Vida() - balaaux)
            else:
                if(jugador == jugador5):
                    jugador.set_Kill(-1)
                else:
                    jugador.set_Kill(1)
            return(False)

        elif mapa[int(bala.y)][int(bala.x)+diferencia] == jugador6.color or mapa[int(bala.y)][int(bala.x)-diferencia] == jugador6.color or mapa[int(bala.y)+diferencia][int(bala.x)] == jugador6.color or mapa[int(bala.y)-diferencia][int(bala.x)] == jugador6.color:
             
            Terreno.dibuja_mapa(Pant,mapa)
            
            if jugador6.get_Vida() > 0:
                jugador6.set_Vida(jugador6.get_Vida() - balaaux)
            else:
                if(jugador == jugador6):
                    jugador.set_Kill(-1)
                else:
                    jugador.set_Kill(1)
            return(False)

        #Se valida que la bala haya impactado en el terreno
        elif mapa[int(bala.y)][int(bala.x)+diferencia] == 1 or mapa[int(bala.y)][int(bala.x)-diferencia] == 1 or mapa[int(bala.y)+diferencia][int(bala.x)] == 1:
            pygame.draw.circle(Pant, Amarillo, (int(bala.x), int(bala.y)), diferencia)
            #se hacen el hoyo de la bala diferencia
            aux2 = -2
            aux1 = -2

            while aux1 <= 50:
                while aux2 <= 40:
                    if (int(bala.y)+aux1) < ancho[0]:
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