import pygame, sys
from pygame import *
from .Variables import Blanco, Celeste, Pant, Amarillo
from .ClassRectangulos import Rectangulos
from .ClassTextos import Textos

class OpcionesCat:
    def pausa():
        #Variables auxiliares fuera del while
        pause = True
        salir = False 
        #Ciclo principal
        while pause:
            #Crea un rect celeste para el fondo del titulo
            fondoCeleste = Rectangulos.rectangulo((Pant.get_width()/2)-125, 20, 300, 60)
            #Dibuja el rect celeste
            Rectangulos.dibujaRectangulos(Pant,Celeste,fondoCeleste,0)
            #Agrega texto TITULO
            Textos.texto_pantalla_rect('Instrucciones', Textos.fuentes(None,80), Blanco, Pant, (Pant.get_width()/2)-125, 20)
            #Agrega texto informativo a la pantalla
            Textos.texto_pantalla_rect('Presione P para volver al juego', 
                                        Textos.fuentes(None,80),Blanco,
                                        Pant, (Pant.get_width()/4)-100, 300)
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
                            #Termina while pause
                            pause == False
                            #Termina while juego
                            salir = True
                            #Retorna variable salir para posterior uso
                            return salir
                    #Detecta la tecla p para terminar la pausa
                    if event.key == pygame.K_p:
                            #Termina while pause
                            pause = False
                            #Retorna variable salir para posterior uso
                            return salir
            #Actualiza la pantalla
            pygame.display.update()


    def instrucciones():
        #Variables auxiliares fuera del while
        instruc = True
        salir = False 
        #Ciclo principal
        while instruc:
            #Crea un rectangulo para el texto
            pauseRect = Rectangulos.rectangulo((Pant.get_width()/2)-100, 100, 200, 70)
            #Dibuja el rect pauseRect
            Rectangulos.dibujaRectangulos(Pant,Amarillo,pauseRect,0)
            #Agrega texto al pauseRect
            Textos.texto_pantalla_rect('Pause', Textos.fuentes(None,80), Blanco, Pant,(Pant.get_width()/2)-80, 110)
            #Agrega texto informativo a la pantalla
            Textos.texto_pantalla_rect('Para iniciar el juego \t ingrese el valor del angulo del usuario que comience\t y luego ingrese la velocidad. \t Después el siguiente jugador repita los pasos, ángulo y luego velocidad.', 
                                        Textos.fuentes(None,80),Blanco,
                                        Pant, (Pant.get_width()/4)-100, 300)
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
                            #Termina while pause
                            instruc == False
            #Actualiza la pantalla
            pygame.display.update()
        
    
    def opciones():
        #Variables auxiliares fuera del while
        corriendo = True
        click = False
        while corriendo:
            #Crea un rect celeste para el fondo del titulo
            fondoCeleste = Rectangulos.rectangulo((Pant.get_width()/2)-125, 20, 300, 60)
            #Dibuja el rect celeste
            Rectangulos.dibujaRectangulos(Pant,Celeste,fondoCeleste,0)
            #Agrega texto TITULO
            Textos.texto_pantalla_rect('Opciones', Textos.fuentes(None,80), Blanco, Pant, (Pant.get_width()/2)-125, 20)

            #Crea el rectangulo del boton1
            boton2 = Rectangulos.rectangulo((Pant.get_width()/2)-100, 200, 200, 50)
            #Dibuja el Boton en pantalla
            Rectangulos.dibujaRectangulos(Pant,Amarillo,boton2,0)
            #Agrega texto en el boton1
            Textos.texto_pantalla_rect('SALIR', Textos.fuentes(None,50), Blanco, Pant, (Pant.get_width()/2)-50, 210)

            #Crea el rectangulo del boton1
            boton1 = Rectangulos.rectangulo((Pant.get_width()/2)-160, 100, 320, 50)
            #Dibuja el Boton en pantalla
            Rectangulos.dibujaRectangulos(Pant,Amarillo,boton1,0)
            #Agrega texto en el boton1
            Textos.texto_pantalla_rect('INSTRUCCIONES', Textos.fuentes(None,50), Blanco, Pant, (Pant.get_width()/2)-145, 110)

            #Detecta la posicion del mouse
            mousex, mousey = pygame.mouse.get_pos()
            #Ejecuta la acción correspondiente al click en el boton
            if boton2.collidepoint((mousex, mousey)):
                if click:
                    #Cierra el juego
                    pygame.quit()
                    sys.exit()
            if boton1.collidepoint((mousex, mousey)):
                if click:
                    #Cierra el juego
                    OpcionesCat.instrucciones()
                    
            #Vuelve el estado original a click
            click = False

            #For loop principal detecta eventos
            for event in pygame.event.get():
                #Detecta cierre de la ventana
                if event.type == QUIT:
                    #Cierra el juego
                    pygame.quit()
                    sys.exit()
                #Detecta el teclado
                if event.type == KEYDOWN:
                    #Detecta tecla escape
                    if event.key == K_ESCAPE:
                        #Para el while y sale al menu
                        corriendo = False
                #Detecta el clic del mouse
                if event.type == MOUSEBUTTONDOWN:
                    #Detecta el click en el boton
                    if event.button == 1:
                        click = True
            #Actualiza la pantalla
            pygame.display.update()