from .Textos import Textos
from .Rectangulos import Rectangulos
from .Variables import *
from .Tanques import *

class OpcionesCat: 
    def opciones(iniciada):
        #Variables auxiliares fuera del while
        click = False
        corriendo = True
        aboton1 = 0 
        aboton2 = 0
        aboton3 = 0
        #Variables juego defecto
        global balas105
        global balasperforante
        global balas60
        global Pant
        largoAntiguo = largo[0]
        anchoAntiguo = ancho[0]
        viento = "NO" #"NORMAL"
        #CICLO PRINCIPAL
        while corriendo:
            #Da fondo a la pantalla
            Pant.fill(Negro)
            #Genera el titulo Menu
            Textos.texto_pantalla_rect('OPCIONES', Textos.fuentes(None,80),Blanco,Pant,(Pant.get_width()/2)-155, 20)
            #Detecta posicion mouse
            mousex, mousey = pygame.mouse.get_pos()
            #Crea 4 rectangulos para los botones 1, 2, 3 y 4 correspondientemente
            #(Pant.get_width()/2)-
            boton1 = Rectangulos.rectangulo(400, 150, 50, 50) #jugadores[0] IA
            boton2 = Rectangulos.rectangulo(750, 150, 50, 50) #jugadores[0] IA
            boton3 = Rectangulos.rectangulo(830, 150, 50, 50) #jugadores[0] IA
            boton4 = Rectangulos.rectangulo(1080, 150, 50, 50) #jugadores[0] IA
            boton5 = Rectangulos.rectangulo(400, 250, 50, 50) #Balas
            boton6 = Rectangulos.rectangulo(750, 250, 50, 50) #Balas
            boton7 = Rectangulos.rectangulo(830, 250, 50, 50) #Balas
            boton8 = Rectangulos.rectangulo(1080, 250, 50, 50) #Balas
            boton9 = Rectangulos.rectangulo(400, 350, 50, 50) #Pantalla -
            boton10 = Rectangulos.rectangulo(650, 350, 50, 50) #Pantalla +
            boton11 = Rectangulos.rectangulo(830, 350, 50, 50) #Pantalla -
            boton12 = Rectangulos.rectangulo(1080, 350, 50, 50) #Pantalla +
            boton13= Rectangulos.rectangulo(400, 450, 50, 50) #Entorno
            boton14= Rectangulos.rectangulo(750, 450, 50, 50) #Entorno   
            boton15 = Rectangulos.rectangulo(830, 450, 50, 50) #Entorno
            boton16 = Rectangulos.rectangulo(1080, 450, 50, 50) #Entorno
            
            botonNuevo = Rectangulos.rectangulo(largoaux[0]-150, 20, 100, 50) 
            Rectangulos.dibujaRectangulos(Pantaux, Amarillo, botonNuevo,0)
            Textos.texto_pantalla_rect('Jugar', Textos.fuentes(None,40), Negro, Pant, largoaux[0]-140, 30)
            
            #Dibuja los rectangulos de los botones
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton1,0)#jugadores[0] IA
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton2,0)#jugadores[0] IA
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton3,0)#jugadores[0] IA
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton4,0)#jugadores[0] IA
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton5,0)#Balas
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton6,0)#Balas
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton7,0)#Balas
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton8,0)#Balas  
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton9,0)#Pantalla
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton10,0)#Pantalla
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton11,0)#Pantalla
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton12,0)#Pantalla
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton13,0)#Entorno
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton14,0)#Entorno
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton15,0)#Entorno
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton16,0)#Entorno

            #Dibuja los rectangulos de los textos
            
            Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo((Pant.get_width()/2)-550, 150, 250, 50),0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo((Pant.get_width()/2)-550, 250, 250, 50),0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo((Pant.get_width()/2)-550, 350, 250, 50),0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo((Pant.get_width()/2)-550, 450, 250, 50),0)
            
            Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo(470, 150, 250, 50),0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo(470, 250, 250, 50),0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo(470, 350, 150, 50),0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo(470, 450, 250, 50),0)

            
            Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo(910, 150, 150, 50),0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo(910, 250, 150, 50),0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo(910, 350, 150, 50),0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo(910, 450, 150, 50),0)

            #Detecta el click en el boton1, jugadores[0] IA <
            if botonNuevo.collidepoint((mousex, mousey)):
                if click:
                    iniciada = True
                    return iniciada
            if boton1.collidepoint((mousex, mousey)):
                if click:
                    #Numero de jugadores[0]
                    if(aboton1 == 0):
                        aboton1 = 1
                    else:
                        aboton1 = 0
            #Detecta el click en el boton2, jugadores[0] IA >
            if boton2.collidepoint((mousex, mousey)):
                if click:
                    if(aboton1 == 1):
                        aboton1 = 0
                    else:
                        aboton1 = 1
            #Detecta el click en el boton3, jugadores[0] IA -
            if boton3.collidepoint((mousex, mousey)):
                if click:
                    if(aboton1 == 0):
                        if(jugadores[0]+IAR[0] <= 2):
                            if(jugadores[0]<=0):
                                Rectangulos.dibujaRectangulos(Pant, Rojo, boton3,0)#jugadores[0] IA
                            else:
                                jugadores[0]-=1
                                IAR[0] +=1  
                        if(jugadores[0]+IAR[0]>2):
                            jugadores[0]-=1
                    else:
                        if(jugadores[0]+IAR[0] <= 2):
                            if(IAR[0]<=0):
                                Rectangulos.dibujaRectangulos(Pant, Rojo, boton3,0)#jugadores[0] IA
                            else:
                                jugadores[0]+=1
                                IAR[0] -=1   
                        if(jugadores[0]+IAR[0]>2):
                            IAR[0]-=1
            #Detecta el click en el boton4, jugadores[0] IA +
            if boton4.collidepoint((mousex, mousey)):
                if click:
                    if(aboton1 == 0):
                        if(jugadores[0]+IAR[0]==6 and IAR[0]<=0):
                            Rectangulos.dibujaRectangulos(Pant, Rojo, boton4,0)#jugadores[0] IA
                        elif(jugadores[0]+IAR[0]==6 and IAR[0]>0):
                            jugadores[0]+=1
                            IAR[0]-=1
                        elif(jugadores[0]+IAR[0]<6):
                            jugadores[0]+=1
                    else:
                        if(jugadores[0]+IAR[0]==6 and jugadores[0]<=0):
                            Rectangulos.dibujaRectangulos(Pant, Rojo, boton4,0)#jugadores[0] IA
                        elif(jugadores[0]+IAR[0]==6 and jugadores[0]>0):
                            jugadores[0]-=1
                            IAR[0]+=1
                        elif(jugadores[0]+IAR[0]<6):
                            IAR[0]+=1
            #Detecta el click en el boton5, Balas <
            if boton5.collidepoint((mousex, mousey)):
                if click:
                    if(aboton2 == 0):
                        aboton2 = 1
                    elif(aboton2 == 1):
                        aboton2 = 2
                    else: 
                        aboton2 = 0
            #Detecta el click en el boton6, balas >
            if boton6.collidepoint((mousex, mousey)):
                if click:
                    if(aboton2 == 0):
                        aboton2 = 2
                    elif(aboton2 == 1):
                        aboton2 = 0
                    else: 
                        aboton2 = 1
            #Detecta el click en el boton7, balas -
            if boton7.collidepoint((mousex, mousey)):
                if click:
    
                    if(aboton2 == 0):
                        if(balas105<=10):
                            Rectangulos.dibujaRectangulos(Pant, Rojo, boton7,0)#Balas
                        else:
                            balas105-=1
                    if(aboton2 == 1):
                        #balas105
                        if(balasperforante<=10):
                            Rectangulos.dibujaRectangulos(Pant, Rojo, boton7,0)#Balas
                        else:
                            balasperforante-=1
                    if(aboton2 == 2):
                        #balas105
                        if(balas60<=10):
                            Rectangulos.dibujaRectangulos(Pant, Rojo, boton7,0)#Balas
                        else:
                            balas60-=1
                
            #Detecta el click en el boton8, balas +
            if boton8.collidepoint((mousex, mousey)):
                if click:
                    if(aboton2 == 0):
                        if(balas105>=30):
                            Rectangulos.dibujaRectangulos(Pant, Rojo, boton8,0)#Balas
                        else:
                            balas105+=1
                    if(aboton2 == 1):
                        if(balasperforante>=30):
                            Rectangulos.dibujaRectangulos(Pant, Rojo, boton8,0)#Balas
                        else:
                            balasperforante+=1
                    if(aboton2 == 2):
                        if(balas60>=30):
                            Rectangulos.dibujaRectangulos(Pant, Rojo, boton8,0)#Balas
                        else:
                            balas60+=1
            #Detecta el click en el boton9, Pantalla - 1  
            if boton9.collidepoint((mousex, mousey)):
                if click:
                    if(largo[0]<=800):
                        Rectangulos.dibujaRectangulos(Pant, Rojo, boton9,0)#Pantalla
                    else:
                        largo[0]-=10
            #Detecta el click en el boton10, Pantalla + 1  
            if boton10.collidepoint((mousex, mousey)):
                if click:
                    if(largo[0]>=1600):
                        Rectangulos.dibujaRectangulos(Pant, Rojo, boton10,0)#Pantalla
                    else:
                        largo[0]+=10
            #Detecta el click en el boton11, Pantalla - 2  
            if boton11.collidepoint((mousex, mousey)):
                if click:
                    if(ancho[0]<=800):
                        Rectangulos.dibujaRectangulos(Pant, Rojo, boton11,0)#Pantalla
                    else:
                        ancho[0]-=10
            #Detecta el click en el boton12, Pantalla + 2  
            if boton12.collidepoint((mousex, mousey)):
                if click:
                    if(ancho[0]>=1600):
                        Rectangulos.dibujaRectangulos(Pant, Rojo, boton12,0)#Pantalla
                    else:
                        ancho[0]+=10
            #Detecta el click en el boton13, Entorno <
            if boton13.collidepoint((mousex, mousey)):
                if click:
                    if(aboton3 == 0):
                        aboton3 = 1
                    else:
                        aboton3 = 0
            #Detecta el click en el boton14, Entorno >
            if boton14.collidepoint((mousex, mousey)):
                if click:
                    if(aboton3 == 1):
                        aboton3 = 0
                    else:
                        aboton3 = 1
            #Detecta el click en el boton15, Entorno -
            if boton15.collidepoint((mousex, mousey)):
                if click:
                    if(aboton3 == 0):
                        if(Gravedad[0]<=2):
                            Rectangulos.dibujaRectangulos(Pant, Rojo, boton15,0)#Entorno
                        else:
                            Gravedad[0]-=1
                    else:
                        if(viento == "NO"):
                            viento = "SI"
                            Viento_Movimiento[0] = True
                        else:
                            viento = "NO"
                            Viento_Movimiento[0] = False
            #Detecta el click en el boton16, Entorno +
            if boton16.collidepoint((mousex, mousey)):
                if click:
                    if(aboton3 == 0):
                        if(Gravedad[0]>=20):
                            Rectangulos.dibujaRectangulos(Pant, Rojo, boton16,0)#Entorno
                        else:
                            Gravedad[0]+=1
                    else:
                        if(viento == "SI"):
                            viento = "NO"
                            Viento_Movimiento[0] = False
                        else:
                            viento = "SI"
                            Viento_Movimiento[0] = True
            if(aboton1 == 0):
                Textos.texto_pantalla_rect('JUGADOR', Textos.fuentes(None,50), Negro, Pant, 510, 160)
                Textos.texto_pantalla_rect(str(jugadores[0]), Textos.fuentes(None,50), Negro, Pant, 950, 160)
                for i in range(jugadores[0]+IAR[0]):
                    if i == 1:
                        jugador3.set_Estado(False)
                        jugador4.set_Estado(False)
                        jugador5.set_Estado(False)
                        jugador6.set_Estado(False)
                    if i == 2:
                        jugador3.set_Estado(True)
                        jugador4.set_Estado(False)
                        jugador5.set_Estado(False)
                        jugador6.set_Estado(False)
                    if i == 3:
                        jugador4.set_Estado(True)
                        jugador5.set_Estado(False)
                        jugador6.set_Estado(False)
                    if i == 4:
                        jugador5.set_Estado(True)
                        jugador6.set_Estado(False)
                    if i == 5:
                        jugador6.set_Estado(True)
                
                for i in range(IAR[0]):
                    #todos IA
                    if jugadores[0] == 0:
                        if i == 0:
                            jugador1.IA = True
                        if i == 1:
                            jugador2.IA = True
                        if i == 2:
                            jugador3.IA = True
                        if i == 3:
                            jugador4.IA = True
                        if i == 4:
                            jugador5.IA = True
                        if i == 5:
                            jugador6.IA = True
                    #5 IA
                    if jugadores[0] == 1:
                        if i == 0:
                            jugador2.IA = True
                        if i == 1:
                            jugador3.IA = True
                        if i == 2:
                            jugador4.IA = True
                        if i == 3:
                            jugador5.IA = True
                        if i == 4:
                            jugador6.IA = True
                    #4 IA
                    if jugadores[0] == 2:
                        if i == 0:
                            jugador3.IA = True
                        if i == 1:
                            jugador4.IA = True
                        if i == 2:
                            jugador5.IA = True
                        if i == 3:
                            jugador6.IA = True
                    #3 IA
                    if jugadores[0] == 3:
                        if i == 0:
                            jugador4.IA = True
                        if i == 1:
                            jugador5.IA = True
                        if i == 2:
                            jugador6.IA = True
                    #2 IA
                    if jugadores[0] == 4:
                        if i == 0:
                            jugador5.IA = True
                        if i == 1:
                            jugador6.IA = True
                    #1 IA
                    if jugadores[0] == 5:
                        if i == 0:
                            jugador6.IA = True

                
            else:
                Textos.texto_pantalla_rect('IA', Textos.fuentes(None,50), Negro, Pant, 570, 160)
                Textos.texto_pantalla_rect(str(IAR[0]), Textos.fuentes(None,50), Negro, Pant, 950, 160)
                for i in range(jugadores[0]+IAR[0]):
                    if i == 1:
                        jugador3.set_Estado(False)
                        jugador4.set_Estado(False)
                        jugador5.set_Estado(False)
                        jugador6.set_Estado(False)
                    if i == 2:
                        jugador3.set_Estado(True)
                        jugador4.set_Estado(False)
                        jugador5.set_Estado(False)
                        jugador6.set_Estado(False)
                    if i == 3:
                        jugador4.set_Estado(True)
                        jugador5.set_Estado(False)
                        jugador6.set_Estado(False)
                    if i == 4:
                        jugador5.set_Estado(True)
                        jugador6.set_Estado(False)
                    if i == 5:
                        jugador6.set_Estado(True)
                
                for i in range(IAR[0]):
                    #todos IA
                    if jugadores[0] == 0:
                        if i == 0:
                            jugador1.IA = True
                        if i == 1:
                            jugador2.IA = True
                        if i == 2:
                            jugador3.IA = True
                        if i == 3:
                            jugador4.IA = True
                        if i == 4:
                            jugador5.IA = True
                        if i == 5:
                            jugador6.IA = True
                    #5 IA
                    if jugadores[0] == 1:
                        if i == 0:
                            jugador2.IA = True
                        if i == 1:
                            jugador3.IA = True
                        if i == 2:
                            jugador4.IA = True
                        if i == 3:
                            jugador5.IA = True
                        if i == 4:
                            jugador6.IA = True
                    #4 IA
                    if jugadores[0] == 2:
                        if i == 0:
                            jugador3.IA = True
                        if i == 1:
                            jugador4.IA = True
                        if i == 2:
                            jugador5.IA = True
                        if i == 3:
                            jugador6.IA = True
                    #3 IA
                    if jugadores[0] == 3:
                        if i == 0:
                            jugador4.IA = True
                        if i == 1:
                            jugador5.IA = True
                        if i == 2:
                            jugador6.IA = True
                    #2 IA
                    if jugadores[0] == 4:
                        if i == 0:
                            jugador5.IA = True
                        if i == 1:
                            jugador6.IA = True
                    #1 IA
                    if jugadores[0] == 5:
                        if i == 0:
                            jugador6.IA = True
            
            if(aboton2 == 0):
                Textos.texto_pantalla_rect('105mm', Textos.fuentes(None,50), Negro, Pant, 535, 260)
                Textos.texto_pantalla_rect(str(balas105), Textos.fuentes(None,50), Negro, Pant, 950, 260)
            elif(aboton2 == 1):
                Textos.texto_pantalla_rect('Perforante', Textos.fuentes(None,50), Negro, Pant, 510, 260)
                Textos.texto_pantalla_rect(str(balasperforante), Textos.fuentes(None,50), Negro, Pant, 950, 260)
            else:
                Textos.texto_pantalla_rect('60mm', Textos.fuentes(None,50), Negro, Pant, 545, 260)
                Textos.texto_pantalla_rect(str(balas60), Textos.fuentes(None,50), Negro, Pant, 950, 260)
            #Define la cantidad de balas
            jugador1.set_Balas(balas105,balasperforante,balas60)
            jugador2.set_Balas(balas105,balasperforante,balas60)
            jugador3.set_Balas(balas105,balasperforante,balas60)
            jugador4.set_Balas(balas105,balasperforante,balas60)
            jugador5.set_Balas(balas105,balasperforante,balas60)
            jugador6.set_Balas(balas105,balasperforante,balas60)
             
            Textos.texto_pantalla_rect(str(largo[0]), Textos.fuentes(None,50), Negro, Pant, 510, 360)
            Textos.texto_pantalla_rect(str(ancho[0]), Textos.fuentes(None,50), Negro, Pant, 950, 360)
            #if(largo[0] != largoAntiguo or ancho[0] != anchoAntiguo):
            #    Pant = pygame.display.set_mode([largo[0],ancho[0]])
            if(aboton3 == 0):
                Textos.texto_pantalla_rect('GRAVEDAD', Textos.fuentes(None,50), Negro, Pant, 500, 460)
                Textos.texto_pantalla_rect(str(Gravedad[0]), Textos.fuentes(None,50), Negro, Pant, 950, 460)
            else:
                Textos.texto_pantalla_rect('VIENTO', Textos.fuentes(None,50), Negro, Pant, 530, 460)
                Textos.texto_pantalla_rect(viento, Textos.fuentes(None,50), Negro, Pant, 950, 460)
            
            Textos.texto_pantalla_rect('JUGADORES', Textos.fuentes(None,50), Negro, Pant, (Pant.get_width()/2)-533, 160)
            Textos.texto_pantalla_rect('BALAS', Textos.fuentes(None,50), Negro, Pant, (Pant.get_width()/2)-480, 260)
            Textos.texto_pantalla_rect('PANTALLA', Textos.fuentes(None,50), Negro, Pant, (Pant.get_width()/2)-515, 360)
            Textos.texto_pantalla_rect('ENTORNO', Textos.fuentes(None,50), Negro, Pant, (Pant.get_width()/2)-515, 460)
            #Botones
            Textos.texto_pantalla_rect('<', Textos.fuentes(None,50), Negro, Pant, 415, 155)#Jugador IA 1
            Textos.texto_pantalla_rect('>', Textos.fuentes(None,50), Negro, Pant, 765, 155)#Jugador IA 1
            Textos.texto_pantalla_rect('-', Textos.fuentes(None,50), Negro, Pant, 850, 160)#Jugador IA 2
            Textos.texto_pantalla_rect('+', Textos.fuentes(None,50), Negro, Pant, 1095, 155)#Jugador IA 2
            Textos.texto_pantalla_rect('<', Textos.fuentes(None,50), Negro, Pant, 415, 255)#Balas
            Textos.texto_pantalla_rect('>', Textos.fuentes(None,50), Negro, Pant, 765, 255)#Balas
            Textos.texto_pantalla_rect('-', Textos.fuentes(None,50), Negro, Pant, 850, 260)#Balas 2
            Textos.texto_pantalla_rect('+', Textos.fuentes(None,50), Negro, Pant, 1095, 255)#Balas 2
            Textos.texto_pantalla_rect('-', Textos.fuentes(None,50), Negro, Pant, 420, 360)#Pantalla
            Textos.texto_pantalla_rect('+', Textos.fuentes(None,50), Negro, Pant, 665, 355)#Pantalla
            Textos.texto_pantalla_rect('x', Textos.fuentes(None,50), Blanco, Pant, 755, 355)#Pantalla
            Textos.texto_pantalla_rect('-', Textos.fuentes(None,50), Negro, Pant, 850, 360)#Pantalla 2
            Textos.texto_pantalla_rect('+', Textos.fuentes(None,50), Negro, Pant, 1095, 355)#Pantalla 2
            Textos.texto_pantalla_rect('<', Textos.fuentes(None,50), Negro, Pant, 415, 455)#Entorno
            Textos.texto_pantalla_rect('>', Textos.fuentes(None,50), Negro, Pant, 765, 455)#Entorno
            Textos.texto_pantalla_rect('-', Textos.fuentes(None,50), Negro, Pant, 850, 460)#Entorno 2
            Textos.texto_pantalla_rect('+', Textos.fuentes(None,50), Negro, Pant, 1095, 455)#Entorno 2
            

            #Actualiza la variable click
            click = False
            #Foor loop detecta eventos
            for event in pygame.event.get():
                #Detecta cierre de ventana
                if event.type == QUIT:
                    #Cierra el juego
                    pygame.quit()
                    sys.exit()
                #Detecta los click del mouse     
                if event.type == MOUSEBUTTONDOWN:
                    #Detecta click en el boton
                    if event.button == 1:
                        click = True     
            #Actualiza la pantalla
            pygame.display.update()
            
            
    #Funcion para mostrar las instrucciones del juego
    def instrucciones():
        #Variables auxiliares fuera del while
        instruc = True
        #Ciclo principal
        while instruc:
            #Agrega texto en el boton
            Textos.texto_pantalla_rect('INSTRUCCIONES', Textos.fuentes(None,80),Blanco,Pant,(Pant.get_width()/2)-200, 20)
            #Agrega texto informativo a la pantalla
            Textos.texto_pantalla_rect('El primer jugador ingresa el angulo y velocidad,', 
                                        Textos.fuentes(None,50),Blanco,
                                        Pant, 80, 200)
            Textos.texto_pantalla_rect('confirma los datos y elige su tipo de bala,', 
                                        Textos.fuentes(None,50),Blanco,
                                        Pant, 80, 250)
            Textos.texto_pantalla_rect('presione     espacio para lanzar.', 
                                        Textos.fuentes(None,50),Blanco,
                                        Pant, 80, 300)
            Textos.texto_pantalla_rect('Siguiente jugador realice los mismos pasos.', 
                                        Textos.fuentes(None,50),Blanco,
                                        Pant,80, 350)
            Textos.texto_pantalla_rect('Gana quien quede con vida o sobre el terreno.', 
                                        Textos.fuentes(None,50),Blanco,
                                        Pant,80, 400)
            Textos.texto_pantalla_rect('Una vez apreta boton "Opciones" no puede regresar.', 
                                        Textos.fuentes(None,50),Blanco,
                                        Pant,80, 500)
            Textos.texto_pantalla_rect('Aprete boton "Jugar" para empezar su juego ', 
                                        Textos.fuentes(None,50),Blanco,
                                        Pant,80, 550)
            Textos.texto_pantalla_rect('desde el menu de opciones.', 
                                        Textos.fuentes(None,50),Blanco,
                                        Pant,80, 600)

            #For loop principal detecta eventos
            for event in pygame.event.get():
                #Detecta cierre de ventana
                if event.type == pygame.QUIT:
                    #Cierra el juego
                    pygame.quit()
                    quit()
                #Detecta el teclado
                if event.type == pygame.KEYDOWN:
                    #Detecta tecla escape
                    if event.key == K_ESCAPE:
                        #Termina while y vuelve al menu
                        instruc = False
            #Actualiza la pantalla
            pygame.display.update()