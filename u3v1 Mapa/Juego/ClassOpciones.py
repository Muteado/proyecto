from .ClassTextos import Textos
from .ClassRectangulos import Rectangulos
from .Variables import *

class OpcionesCat:
    #Funcion para mostrar las instrucciones del juego
    def instrucciones():
        #Variables auxiliares fuera del while
        instruc = True
        click = False 
        #Ciclo principal
        while instruc:
            #Crea el rectangulo del boton
            boton = Rectangulos.rectangulo((Pant.get_width()/2)-100, 70, 200, 50)
            #Detecta la posicion del mouse
            mousex, mousey = pygame.mouse.get_pos()
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
            Textos.texto_pantalla_rect('MENU ', Textos.fuentes(None,50), Blanco, Pant, (Pant.get_width()/2)-50, 80)
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