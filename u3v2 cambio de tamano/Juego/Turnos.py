from .Textos import *
from .Variables import *
from pygame import event
from .Proyectil import *


class Turnos:
    print()
    def stockbalas(balasJugador, colorardo):
        Textos.texto_pantalla_rect(str(balasJugador[0]),Textos.fuentes(None,27),colorardo,Pant,610,5)
        Textos.texto_pantalla_rect(str(balasJugador[1]),Textos.fuentes(None,27),colorardo,Pant,645,5)
        Textos.texto_pantalla_rect(str(balasJugador[2]),Textos.fuentes(None,27),colorardo,Pant,680,5)

    def balasturnos(botonamarillo,botonnaranja,botonmorado,jugador):
        bala105,balaperfo,bala60 = jugador.get_Balas()
        if botonamarillo == True and bala105 > 0:
            bala = Proyectil(X_Y_Tanques[0]+20, X_Y_Tanques[1], Angulo_Jugador[0], Velocidad_Jugador[0])#velocidad,angulo
            Balaaux[0] = 50
            jugador.set_Balas(bala105-1,balaperfo,bala60)
            clock = pygame.time.Clock()
            bala.disparar = True
            
            
        if botonnaranja == True and balaperfo > 0:
            bala = Proyectil(X_Y_Tanques[0]+20, X_Y_Tanques[1], Angulo_Jugador[0], Velocidad_Jugador[0])#velocidad,angulo

            Balaaux[0] = 40
            jugador.set_Balas(bala105,balaperfo-1,bala60)
            #print("Balas perforantes : ", balas)
            #Turno[0] = 2
            clock = pygame.time.Clock()
            bala.disparar = True
            

        if botonmorado == True and bala60 > 0:
            bala = Proyectil(X_Y_Tanques[0]+20, X_Y_Tanques[1], Angulo_Jugador[0], Velocidad_Jugador[0])#velocidad,angulo

            Balaaux[0] = 30
            jugador.set_Balas(bala105,balaperfo,bala60-1)
            clock = pygame.time.Clock()
            bala.disparar = True

        if bala105 == 0 and balaperfo == 0 and bala60 == 0:
            Textos.texto_pantalla_rect("Te quedaste sin balas!", Textos.fuentes(None, 40), Azul, Pant,500,50)
            #print("Te quedaste sin balas!")