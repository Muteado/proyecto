
from .Textos import *
from .Variables import *
from .Botones import *
from pygame import event
from .Proyectil import *
#from .claseJuego import botonamarillo,botonnaranja,botonmorado


class Turnos:
    print()
    
    
    def stockbalas(balas, colorardo):
        Textos.texto_pantalla_rect(str(balas[0]),Textos.fuentes(None,27),colorardo,Pant,610,5)
        Textos.texto_pantalla_rect(str(balas[1]),Textos.fuentes(None,27),colorardo,Pant,645,5)
        Textos.texto_pantalla_rect(str(balas[2]),Textos.fuentes(None,27),colorardo,Pant,680,5)

    def balasturnos(botonamarillo,botonnaranja,botonmorado,jugador):


        if botonamarillo == True and jugador[0] > 0:
            bala = Proyectil(X_Y_Tanques[0]+20, X_Y_Tanques[1], Angulo_Azul[0], Velocidad_Azul[0])#velocidad,angulo
            #pygame.key.set_repeat(1, 80)  # Activa repetición de teclas
            Balaaux[0] = 50
            jugador[0] = jugador[0] -1
            #Turno[0] = 2
            #print("Balas 105mm : ", balas)
            clock = pygame.time.Clock()
            bala.disparar = True
            
            
        if botonnaranja == True and jugador[1] > 0:
            bala = Proyectil(X_Y_Tanques[0]+20, X_Y_Tanques[1], Angulo_Azul[0], Velocidad_Azul[0])#velocidad,angulo
            #pygame.key.set_repeat(1, 80)  # Activa repetición de teclas
            Balaaux[0] = 40
            jugador[1] = jugador[1] - 1
            #print("Balas perforantes : ", balas)
            #Turno[0] = 2
            clock = pygame.time.Clock()
            bala.disparar = True
            

        if botonmorado == True and jugador[2] > 0:
            bala = Proyectil(X_Y_Tanques[0]+20, X_Y_Tanques[1], Angulo_Azul[0], Velocidad_Azul[0])#velocidad,angulo
            #pygame.key.set_repeat(1, 80)  # Activa repetición de teclas
            Balaaux[0] = 30
            jugador[2] = jugador[2] - 1
            #print("Balas 60 mm : ", balas)
            #Turno[0] = 2
            clock = pygame.time.Clock()
            bala.disparar = True

        if jugador[0] == 0 and jugador[1] == 0 and jugador[2] == 0:
            Textos.texto_pantalla_rect("Te quedaste sin balas!", Textos.fuentes(None, 40), Azul, Pant,500,50)
            #print("Te quedaste sin balas!")
            Turno[0] = 2

    # turnos(1, True, False, rectTXT1A,rectTXT2A,Angulo_Azul,balaspj1)
    def turnos(turno, rectTXTvelocidad, rectTXTangulo,angulo, balas,mousex,mousey):
        
        if rectTXTangulo.collidepoint((mousex,mousey)):
            activo1 = True
            activo2 = False
            angulo[turno] = ''
        elif rectTXTvelocidad.collidepoint((mousex,mousey)):
            activo2 = True
            activo1 = False
        elif botonamarillo1.collidepoint((mousex,mousey)):
            if balas[0] > 0:
                botonamarillo = True
                botonnaranja = False
                botonmorado = False
            else:
                print("No te quedan balas! de 105 mm")
                botonamarillo = False
                botonnaranja = False
                botonmorado = False 
        elif botonnaranja1.collidepoint((mousex,mousey)):
            if balas[1] > 0:   
                botonamarillo = False
                botonnaranja = True
                botonmorado = False

            else:
                print("No te quedan balas! perforantes")
                botonamarillo = False
                botonnaranja = False
                botonmorado = False 

        elif botonmorado1.collidepoint((mousex,mousey)):
            if balas[2] > 0:
                botonamarillo = False
                botonnaranja = False
                botonmorado = True

            else:
                print("No te quedan balas! de 60 mm")
                botonamarillo = False
                botonnaranja = False
                botonmorado = False 
        else:
            activo1 = False
            activo2 = False
    