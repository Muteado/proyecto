from .Textos import Textos
from .Rectangulos import Rectangulos
from .Variables import *
from .Tanques import *
from .BotonesOpciones import *

class OpcionesCat: 
    
    

    def opciones(iniciada):
        #Variables auxiliares fuera del while
        click = False
        corriendo = True
        aboton1 = 0 
        aboton2 = 0
        aboton3 = 0
        #Variables juego defecto
        global jugadores
        IA = 0
        global balas105
        global balasperforante
        global balas60
        global Pant
        largoAntiguo = largo[0]
        anchoAntiguo = ancho[0]
        gravedad = 2 #"NORMAL"
        viento = "NO" #"NORMAL"

        #Pant = pygame.display.set_mode([(largo[1]),(ancho[1])])

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
            boton1 = Rectangulos.rectangulo(400, 150, 50, 50) #Jugadores IA
            boton2 = Rectangulos.rectangulo(750, 150, 50, 50) #Jugadores IA
            boton3 = Rectangulos.rectangulo(830, 150, 50, 50) #Jugadores IA
            boton4 = Rectangulos.rectangulo(1080, 150, 50, 50) #Jugadores IA
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
            Rectangulos.dibujaRectangulos(Pant, Amarillo, botonNuevo,0)
            Textos.texto_pantalla_rect('Jugar', Textos.fuentes(None,40), Negro, Pant, largoaux[0]-140, 30)
            
            #Dibuja los rectangulos de los botones
            
            BotonesOpciones.botonesopciones(boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,boton10,boton11,boton12,boton13,boton14,boton15,boton16)

            #Detecta el click en el boton1, Jugadores IA <
            
            if boton1.collidepoint((mousex, mousey)):
                if click:
                    #Numero de jugadores
                    if(aboton1 == 0):
                        aboton1 = 1
                    else:
                        aboton1 = 0
            #Detecta el click en el boton2, Jugadores IA >
            if boton2.collidepoint((mousex, mousey)):
                if click:
                    if(aboton1 == 1):
                        aboton1 = 0
                    else:
                        aboton1 = 1
            #Detecta el click en el boton3, Jugadores IA -
            if boton3.collidepoint((mousex, mousey)):
                if click:
                    if(aboton1 == 0):
                        if(jugadores+IA <= 2):
                            if(jugadores<=0):
                                Rectangulos.dibujaRectangulos(Pant, Rojo, boton3,0)#Jugadores IA
                            else:
                                jugadores-=1
                                IA+=1  
                        if(jugadores+IA>2):
                            jugadores-=1
                    else:
                        if(jugadores+IA <= 2):
                            if(IA<=0):
                                Rectangulos.dibujaRectangulos(Pant, Rojo, boton3,0)#Jugadores IA
                            else:
                                jugadores+=1
                                IA-=1   
                        if(jugadores+IA>2):
                            IA-=1
            #Detecta el click en el boton4, Jugadores IA +
            if boton4.collidepoint((mousex, mousey)):
                if click:
                    if(aboton1 == 0):
                        if(jugadores+IA==6 and IA<=0):
                            Rectangulos.dibujaRectangulos(Pant, Rojo, boton4,0)#Jugadores IA
                        elif(jugadores+IA==6 and IA>0):
                            jugadores+=1
                            IA-=1
                        elif(jugadores+IA<6):
                            jugadores+=1
                    else:
                        if(jugadores+IA==6 and jugadores<=0):
                            Rectangulos.dibujaRectangulos(Pant, Rojo, boton4,0)#Jugadores IA
                        elif(jugadores+IA==6 and jugadores>0):
                            jugadores-=1
                            IA+=1
                        elif(jugadores+IA<6):
                            IA+=1
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
                        pygame.display.update()
            #Detecta el click en el boton10, Pantalla + 1  
            if boton10.collidepoint((mousex, mousey)):
                if click:
                    if(largo[0]>=1600):
                        Rectangulos.dibujaRectangulos(Pant, Rojo, boton10,0)#Pantalla
                        
                    else:
                        largo[0]+=10
                        pygame.display.update()
            #Detecta el click en el boton11, Pantalla - 2  
            if boton11.collidepoint((mousex, mousey)):
                if click:
                    if(ancho[0]<=800):
                        Rectangulos.dibujaRectangulos(Pant, Rojo, boton11,0)#Pantalla
                        
                    else:
                        ancho[0]-=10
                        pygame.display.update()
            #Detecta el click en el boton12, Pantalla + 2  
            if boton12.collidepoint((mousex, mousey)):
                if click:
                    if(ancho[0]>=1600):
                        Rectangulos.dibujaRectangulos(Pant, Rojo, boton12,0)#Pantalla
                        
                    else:
                        ancho[0]+=10
                        pygame.display.update()

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
                        if(gravedad<=2):
                            Rectangulos.dibujaRectangulos(Pant, Rojo, boton15,0)#Entorno
                        else:
                            gravedad-=1
                    else:
                        if(viento == "NO"):
                            viento = "SI"
                        else:
                            viento = "NO"
            #Detecta el click en el boton16, Entorno +
            if boton16.collidepoint((mousex, mousey)):
                if click:
                    if(aboton3 == 0):
                        if(gravedad>=20):
                            Rectangulos.dibujaRectangulos(Pant, Rojo, boton16,0)#Entorno
                        else:
                            gravedad+=1
                    else:
                        if(viento == "SI"):
                            viento = "NO"
                        else:
                            viento = "SI"
            if(aboton1 == 0):
                Textos.texto_pantalla_rect('JUGADOR', Textos.fuentes(None,50), Negro, Pant, 510, 160)
                Textos.texto_pantalla_rect(str(jugadores), Textos.fuentes(None,50), Negro, Pant, 950, 160)
                for i in range(jugadores):
                    if i == 3:
                        jugador3.set_Estado(True)
                    if i == 4:
                        jugador4.set_Estado(True)
                    if i == 5:
                        jugador5.set_Estado(True)
                    if i == 6:
                        jugador6.set_Estado(True)
            else:
                Textos.texto_pantalla_rect('IA', Textos.fuentes(None,50), Negro, Pant, 570, 160)
                Textos.texto_pantalla_rect(str(IA), Textos.fuentes(None,50), Negro, Pant, 950, 160)
            
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
            if botonNuevo.collidepoint((mousex, mousey)):
                if click:
                    iniciada = True
                    #if(largo[0] != largoAntiguo or ancho[0] != anchoAntiguo):
                    Pant = pygame.display.set_mode([largo[0],ancho[0]])
                    #else:
                    #    Pant = pygame.display.set_mode([largo[0],ancho[0]])
                    return iniciada
            if(aboton3 == 0):
                Textos.texto_pantalla_rect('GRAVEDAD', Textos.fuentes(None,50), Negro, Pant, 500, 460)
                Textos.texto_pantalla_rect(str(gravedad), Textos.fuentes(None,50), Negro, Pant, 950, 460)
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
                #Detecta el teclado
                if event.type == KEYDOWN:
                    #Detecta la tecla escape
                    if event.key == K_ESCAPE:
                        corriendo = False
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
            Textos.texto_pantalla_rect('Jugador ROJO repita los mismos pasos.', 
                                        Textos.fuentes(None,50),Blanco,
                                        Pant,80, 350)
            Textos.texto_pantalla_rect('Gana quien quede con vida o sobre el terreno.', 
                                        Textos.fuentes(None,50),Blanco,
                                        Pant,80, 400)

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