import pygame, sys
from pygame import *
from .Variables import Blanco, Celeste, Negro, Pant, Amarillo
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
            fondoAmarillo = Rectangulos.rectangulo((Pant.get_width()/2)-125, 80, 190, 50)
            #Dibuja el rect celeste
            Rectangulos.dibujaRectangulos(Pant,Amarillo,fondoAmarillo,0)
            #Agrega texto TITULO
            Textos.texto_pantalla_rect('Pause', Textos.fuentes(None,80), Blanco, Pant, (Pant.get_width()/2)-115, 80)
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
        click = False 
        #Ciclo principal
        while instruc:
            #Crea el rectangulo del boton2
            boton = Rectangulos.rectangulo((Pant.get_width()/2)-100, 200, 200, 50)
            #Detecta la poNonecion del mouse
            mousex, mousey = pygame.mouse.get_pos()
            #Ejecuta la acción correspondiente al click en el boton
            if boton.collidepoint((mousex, mousey)):
                if click:
                    #Termina while pause
                        instruc = False
            #Vuelve el estado original a click
            click = False
            #Dibuja el Boton en pantalla
            Rectangulos.dibujaRectangulos(Pant,Amarillo,boton,0)
            #Agrega texto en el boton
            Textos.texto_pantalla_rect('MENU ', Textos.fuentes(None,50), Blanco, Pant, (Pant.get_width()/2)-50, 210)
            #Agrega texto informativo a la pantalla
            Textos.texto_pantalla_rect('Para iniciar el juego', 
                                        Textos.fuentes(None,50),Blanco,
                                        Pant, 80, 300)
            Textos.texto_pantalla_rect('ingrese el valor del angulo del usuario que comience', 
                                        Textos.fuentes(None,50),Blanco,
                                        Pant, 80, 350)
            Textos.texto_pantalla_rect('y luego ingrese la velocidad. (PreNoneonando enter para confirmar).', 
                                        Textos.fuentes(None,50),Blanco,
                                        Pant, 80, 400)
            Textos.texto_pantalla_rect('Después el Noneguiente jugador repita los pasos,', 
                                        Textos.fuentes(None,50),Blanco,
                                        Pant,80, 450)
            Textos.texto_pantalla_rect('ángulo y luego velocidad.', 
                                        Textos.fuentes(None,50),Blanco,
                                        Pant,80, 500)

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
                        instruc = False
                    #Detecta el clic del mouse
                if event.type == MOUSEBUTTONDOWN:
                    #Detecta el click en el boton
                    if event.button == 1:
                        click = True
            #Actualiza la pantalla
            pygame.display.update()
        
    
    def opciones():
        #Variables auxiliares fuera del while
        corriendo = True
        click = False
        while corriendo:
            #Crea un rect celeste para el fondo del titulo
            fondoNegro = Rectangulos.rectangulo((Pant.get_width()/2)-125, 20, 300, 60)
            #Dibuja el rect celeste
            Rectangulos.dibujaRectangulos(Pant,Negro,fondoNegro,0)
            #Agrega texto TITULO
            Textos.texto_pantalla_rect('Opciones', Textos.fuentes(None,80), Blanco, Pant, (Pant.get_width()/2)-125, 20)

            #Crea el rectangulo del boton2
            boton2 = Rectangulos.rectangulo((Pant.get_width()/2)-100, 200, 200, 50)
 
            #Crea el rectangulo del boton1
            boton1 = Rectangulos.rectangulo((Pant.get_width()/2)-160, 100, 320, 50)
            
            #Detecta la poNonecion del mouse
            mousex, mousey = pygame.mouse.get_pos()
            #Ejecuta la acción correspondiente al click en el boton
            if boton2.collidepoint((mousex, mousey)):
                if click:
                    #Cierra el juego
                    pygame.quit()
                    sys.exit()
            if boton1.collidepoint((mousex, mousey)):
                if click:
                    #Muestra las instrucciones
                    corriendo = False
                    OpcionesCat.instrucciones()
                    
            #Vuelve el estado original a click
            click = False
            #Dibuja el Boton1 en pantalla
            Rectangulos.dibujaRectangulos(Pant,Amarillo,boton1,0)
            #Agrega texto en el boton1
            Textos.texto_pantalla_rect('INSTRUCCIONES', Textos.fuentes(None,50), Blanco, Pant, (Pant.get_width()/2)-145, 110)
            #Dibuja el Boton2 en pantalla
            Rectangulos.dibujaRectangulos(Pant,Amarillo,boton2,0)
            #Agrega texto en el boton2
            Textos.texto_pantalla_rect('SALIR', Textos.fuentes(None,50), Blanco, Pant, (Pant.get_width()/2)-50, 210)

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