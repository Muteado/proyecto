from .Textos import Textos
from .Rectangulos import Rectangulos
from .Variables import *

class OpcionesCat:
    def opciones():
        #Variables auxiliares fuera del while
        click = False
        aboton1 = 0 
        aboton2 = 0
        aboton3 = 0
        #CICLO PRINCIPAL
        while True:
            #Da fondo a la pantalla
            Pant.fill(Negro)
            #Genera el titulo Menu
            Textos.texto_pantalla_rect('OPCIONES', Textos.fuentes(None,80),Blanco,Pant,(Pant.get_width()/2)-155, 20)
            #Detecta posicion mouse
            mousex, mousey = pygame.mouse.get_pos()
            #Crea 4 rectangulos para los botones 1, 2, 3 y 4 correspondientemente
            #(Pant.get_width()/2)-
            boton1 = Rectangulos.rectangulo(400, 150, 50, 50) #
            boton2 = Rectangulos.rectangulo(500, 150, 50, 50) #
            boton3 = Rectangulos.rectangulo(400, 250, 50, 50) #
            boton5 = Rectangulos.rectangulo(400, 350, 50, 50) #
            boton4 = Rectangulos.rectangulo(500, 250, 50, 50) # 
            boton7 = Rectangulos.rectangulo(400, 450, 50, 50) #  
            boton6 = Rectangulos.rectangulo(500, 350, 50, 50) # 
            boton8 = Rectangulos.rectangulo(500, 450, 50, 50) #
            boton9 = Rectangulos.rectangulo(900, 450, 50, 50) #SALIR PROVISORIO
            #Dibuja los rectangulos de los botones
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton1,0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton2,0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton3,0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton4,0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton5,0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton6,0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton7,0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton8,0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton9,0)

            #Dibuja los rectangulos de los textos
            Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo((Pant.get_width()/2)-550, 150, 250, 50),0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo((Pant.get_width()/2)-550, 250, 250, 50),0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo((Pant.get_width()/2)-550, 350, 250, 50),0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo((Pant.get_width()/2)-550, 450, 250, 50),0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo((Pant.get_width()/2), 150, 250, 50),0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo((Pant.get_width()/2), 250, 250, 50),0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo((Pant.get_width()/2), 350, 250, 50),0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo((Pant.get_width()/2), 450, 250, 50),0)
            #Detecta el click en el boton1
            if boton1.collidepoint((mousex, mousey)):
                if click:
                    #Numero de jugadores
                    if(aboton1 == 0):
                        aboton1 = 1
                    else:
                        aboton1 = 0
            #Detecta el click en el boton2
            if boton2.collidepoint((mousex, mousey)):
                if click:
                    if(aboton1 == 1):
                        aboton1 = 0
                    else:
                        aboton1 = 1
            #Detecta el click en el boton3
            if boton3.collidepoint((mousex, mousey)):
                if click:
                    if(aboton2 == 0):
                        aboton2 = 2
                    elif(aboton2 == 1):
                        aboton2 = 0
                    else:
                        aboton2 = 1
            #Detecta el click en el boton4
            if boton4.collidepoint((mousex, mousey)):
                if click:
                    if(aboton2 == 1):
                        aboton2 = 2
                    elif(aboton2 == 2):
                        aboton2 = 0
                    else:
                        aboton2 = 1
            if boton7.collidepoint((mousex, mousey)):
                if click:
                    if(aboton3 == 1):
                        aboton3 = 0
                    else:
                        aboton3 = 1
            if boton8.collidepoint((mousex, mousey)):
                if click:
                    if(aboton3 == 0):
                        aboton3 = 1
                    else:
                        aboton3 = 0
            if boton9.collidepoint((mousex, mousey)):
                if click:
                    #Cierra el juego
                    pygame.quit()
                    sys.exit()
            if(aboton1 == 1):
                Textos.texto_pantalla_rect('JUGADORES', Textos.fuentes(None,50), Negro, Pant, Pant.get_width()/2+20, 160)
            else:
                Textos.texto_pantalla_rect('IA', Textos.fuentes(None,50), Negro, Pant, Pant.get_width()/2+100, 160)
            
            if(aboton2 == 1):
                Textos.texto_pantalla_rect('105mm', Textos.fuentes(None,50), Negro, Pant, Pant.get_width()/2+20, 260)
            elif(aboton2 == 2):
                Textos.texto_pantalla_rect('Perforante', Textos.fuentes(None,50), Negro, Pant, Pant.get_width()/2+20, 260)
            else:
                Textos.texto_pantalla_rect('60mm', Textos.fuentes(None,50), Negro, Pant, Pant.get_width()/2+100, 260)
            
            if(aboton3 == 1):
                Textos.texto_pantalla_rect('GRAVEDAD', Textos.fuentes(None,50), Negro, Pant, Pant.get_width()/2+20, 460)
            else:
                Textos.texto_pantalla_rect('VIENTO', Textos.fuentes(None,50), Negro, Pant, Pant.get_width()/2+100, 460)
            
            Textos.texto_pantalla_rect('JUGADORES', Textos.fuentes(None,50), Negro, Pant, (Pant.get_width()/2)-533, 160)
            Textos.texto_pantalla_rect('BALAS', Textos.fuentes(None,50), Negro, Pant, (Pant.get_width()/2)-480, 260)
            Textos.texto_pantalla_rect('PANTALLA', Textos.fuentes(None,50), Negro, Pant, (Pant.get_width()/2)-515, 360)
            Textos.texto_pantalla_rect('ENTORNO', Textos.fuentes(None,50), Negro, Pant, (Pant.get_width()/2)-515, 460)
            #Botones
            Textos.texto_pantalla_rect('<', Textos.fuentes(None,50), Negro, Pant, 415, 155)
            Textos.texto_pantalla_rect('>', Textos.fuentes(None,50), Negro, Pant, 515, 155)
            Textos.texto_pantalla_rect('<', Textos.fuentes(None,50), Negro, Pant, 415, 255)
            Textos.texto_pantalla_rect('>', Textos.fuentes(None,50), Negro, Pant, 515, 255)
            Textos.texto_pantalla_rect('<', Textos.fuentes(None,50), Negro, Pant, 415, 355)
            Textos.texto_pantalla_rect('>', Textos.fuentes(None,50), Negro, Pant, 515, 355)
            Textos.texto_pantalla_rect('<', Textos.fuentes(None,50), Negro, Pant, 415, 455)
            Textos.texto_pantalla_rect('>', Textos.fuentes(None,50), Negro, Pant, 515, 455)
            
            Textos.texto_pantalla_rect('X', Textos.fuentes(None,50), Negro, Pant, 915, 455)
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
                        break
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
        click = False 
        #Ciclo principal
        while instruc:
            #Detecta la posicion del mouse
            mousex, mousey = pygame.mouse.get_pos() #Crea el rectangulo del boton
            boton = Rectangulos.rectangulo((Pant.get_width()/2)-100, 70, 200, 50)
           
            #Ejecuta la acción correspondiente al click en el boton
            if boton.collidepoint((mousex, mousey)):
                if click:
                    #Termina while y sale de la funcion
                    instruc = False
            #Vuelve el estado original a click
            click = False
            #Dibuja el Boton en pantalla
            Rectangulos.dibujaRectangulos(Pant,Amarillo,boton,0)
            #Agrega texto en el boton
            Textos.texto_pantalla_rect('MENU ', Textos.fuentes(None,50), Negro, Pant, (Pant.get_width()/2)-50, 80)
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
                    #Detecta el clic del mouse
                if event.type == MOUSEBUTTONDOWN:
                    #Detecta el click en el boton
                    if event.button == 1:
                        click = True
            #Actualiza la pantalla
            pygame.display.update()