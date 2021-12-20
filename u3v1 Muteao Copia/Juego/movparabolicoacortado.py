from .Variables import *
from .Proyectil import *
from .Terreno import Terreno
from .Esquinas import *

class Movimiento:
    def angulos(posicionx,posiciony,angulotanque,velocidad):
        angulo = angulotanque[0]
        if angulotanque[0] < 90:
            bala = Proyectil(xtanque[posicionx]+10, ytanque[posiciony], angulotanque[0], velocidad[0])#velocidad,angulo
            print("debug 1")
        if angulotanque[0] == 90:
            bala = Proyectil(xtanque[posicionx], ytanque[posiciony]-10, angulotanque[0], velocidad[0])#velocidad,angulo
            print("debug 2")
        if angulotanque[0] > 90:
            bala = Proyectil(xtanque[posicionx]-10, ytanque[posiciony], angulotanque[0], velocidad[0])#velocidad,angulo
            print("debug 3")
        bala.disparar = aux
        clock = pygame.time.Clock()
        
        print("debug 4")
        
    def validaimpactos(turno,diferencia,bala):
        if mapa[int(bala.y)][int(bala.x)+diferencia] == 2 or mapa[int(bala.y)][int(bala.x)-diferencia] == 2 or mapa[int(bala.y)+diferencia][int(bala.x)] == 2 or mapa[int(bala.y)-diferencia][int(bala.x)] == 2:
            print("cayó en un tanque")
            #Partida[0] = 1
            
            #bala.disparar = False
            #bala = Proyectil(300, 300, angulo, velocidad)#velocidad,angulo
            Terreno.dibuja_mapa(Pant,mapa)
            
            
            if vidaTank[0] > 0:
                if turno == 1:
                    vidaTank[0] = vidaTank[0] - Balaaux[0]
                    #print("La vida del Azul es: ",vidaTank[0])
                    turno = 2
                    
                if turno == 2:
                    vidaTank[0] = vidaTank[0] - Balaaux[0]
                    #print("La vida del Azul es: ",vidaTank[0])
                    turno = 1
                    

        #Valido si la bala impactó con el tanque rojo
        elif mapa[int(bala.y)][int(bala.x)+diferencia] == 3 or mapa[int(bala.y)][int(bala.x)-diferencia] == 3 or mapa[int(bala.y)+diferencia][int(bala.x)] == 3 or mapa[int(bala.y)-diferencia][int(bala.x)] == 3:
            print("cayó en un tanque")
            #Partida[0] = 2
            
            #bala.disparar = False
            #bala = Proyectil(300, 300, angulo, velocidad)#velocidad,angulo
            Terreno.dibuja_mapa(Pant,mapa)
            
            
            if vidaTank[1] > 0:
                if turno == 1:
                    vidaTank[1] = vidaTank[1] - Balaaux[0]
                    #print("La vida del rojo es: ",vidaTank[1])
                    turno = 2
                    
                if turno == 2:
                    vidaTank[1] = vidaTank[1] - Balaaux[0]
                    #print("La vida del rojo es: ",vidaTank[1])
                    turno = 1
                    

        #Se valida que la bala haya impactado en el terreno
        elif mapa[int(bala.y)][int(bala.x)+diferencia] == 1 or mapa[int(bala.y)][int(bala.x)-diferencia] == 1 or mapa[int(bala.y)+diferencia][int(bala.x)] == 1:
            pygame.draw.circle(Pant, Amarillo, (int(bala.x), int(bala.y)), diferencia)
            #se hacen el hoyo de la bala diferencia5
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
            if turno == 1:
                turno = 2
            elif turno == 2:
                turno = 1
            

        #Se valida que la bala vaya por el aire y así siga su trayecto
        elif mapa[int(bala.y)][int(bala.x)+diferencia] == 0 or mapa[int(bala.y)+diferencia][int(bala.x)] == 0 or mapa[int(bala.y)][int(bala.x)-diferencia] == 0:
            pygame.draw.circle(Pant, Amarillo, (int(bala.x), int(bala.y)), diferencia)
            pygame.display.update()


    def ImprimeMetros(turno,bala):
        if turno == 1:   
            
            if Angulo_Azul[0] >= 90:
                text = "Metros = %d m   Altura = %d m" % (
                    XdelTank[0]-bala.xreal, prueba)
            elif Angulo_Azul[0] < 90:
                text = "Metros = %d m   Altura = %d m" % (
                    bala.xreal-XdelTank[0], prueba)
    
            mensaje = Textos.fuentes(None, 50).render(text, 600, Negro)
            
            fuente = pygame.font.Font(None,50)