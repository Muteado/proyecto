import pygame, sys
from pygame import *
from Juego.claseJuego import Juego
from Juego.ClassTextos import Textos
from Juego.claseTerreno import Terreno
from Juego.ClassOpciones import OpcionesCat
from Juego.ClassRectangulos import Rectangulos
from Juego.Variables import Amarillo, Blanco, Negro, Pant, mapa, Turno, Partida
from Juego.ClaseBotones import *

class Menus:
    def main_menu(mapa):
        #Variable auxiliar fuera del while
        angu_ROJO = ''
        velo_ROJO = ''
        angu_AZUL = ''
        velo_AZUL = ''
        Turno[0] = 1
        Partida[0] = 0
        click = False
        mapa = Terreno.run(mapa)
        while True:
            ##Genera el juego sin comenzarlo##
            #Variable auxiliar
            aux=True
            #Juego.juego(Pant,aux,angu_ROJO,velo_ROJO,angu_AZUL,velo_AZUL, mapa)
            Pant.fill(Negro)
            #Genera el titulo Menu
            Textos.texto_pantalla_rect('Menú', Textos.fuentes(None,80),Blanco,Pant,(Pant.get_width()/2)-75, 20)
            #Detecta posicion mouse
            mousex, mousey = pygame.mouse.get_pos()
            #Crea 2 rectangulos para los botones 1 y 2 correspondientemente
            boton1 = Rectangulos.rectangulo((Pant.get_width()/2)-150, 100, 300, 50) #JUGAR
            boton2 = Rectangulos.rectangulo((Pant.get_width()/2)-150, 200, 300, 50) #NUEVA PARTIDA
            boton3 = Rectangulos.rectangulo((Pant.get_width()/2)-150, 300, 300, 50) #INSTRUCCIONES
            boton4 = Rectangulos.rectangulo((Pant.get_width()/2)-150, 400, 300, 50) #SALIR
            #Detecta el click en el boton1
            if boton1.collidepoint((mousex, mousey)):
                if click:
                    #Ejecuta el juego
                    Juego.juego(Pant,aux,angu_ROJO,velo_ROJO,angu_AZUL,velo_AZUL, mapa)      
            #Detecta el click en el boton2
            if boton2.collidepoint((mousex, mousey)):
                if click:
                    angu_ROJO = ''
                    velo_ROJO = ''
                    angu_AZUL = ''
                    velo_AZUL = ''
                    Turno[0] = 1
                    Partida[0] = 0
                    click = False
                    #Tanque Azul
                    c105[0] = 3
                    cperforante[0] = 10
                    c60[0] = 3
                    #Tanque Rojo
                    c105[1] = 3
                    cperforante[1] = 10
                    c60[1] = 3
                    #Vida Tanques
                    vidaAzul[0] = 100
                    vidaRojo[0] = 100
                    Partida[0] = 0
                    mapa = Terreno.run(mapa)
                    Juego.juego(Pant,aux,angu_ROJO,velo_ROJO,angu_AZUL,velo_AZUL, mapa)
            if boton3.collidepoint((mousex, mousey)):
                if click:
                    #Muestra las instrucciones
                    Pant.fill(Negro)
                    OpcionesCat.instrucciones()
            if boton4.collidepoint((mousex, mousey)):
                if click:
                    #Cierra el juego
                    pygame.quit()
                    sys.exit()
            #Dibuja los rectangulos de los botones 1 y 2 correspondientemente
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton1,0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton2,0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton3,0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton4,0)
            #Genera los textos de ambos botones
            Textos.texto_pantalla_rect('JUEGO', Textos.fuentes(None,50), Negro, Pant, (Pant.get_width()/2)-60, 110)
            Textos.texto_pantalla_rect('NUEVA PARTIDA', Textos.fuentes(None,50), Negro, Pant, (Pant.get_width()/2)-140, 210)
            Textos.texto_pantalla_rect('INSTRUCCIONES', Textos.fuentes(None,50), Negro, Pant, (Pant.get_width()/2)-145, 310)
            Textos.texto_pantalla_rect('SALIR', Textos.fuentes(None,50), Negro, Pant, (Pant.get_width()/2)-50, 410)
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
                        #Actualiza la variable
                        aux=True
                        #Ejecuta el juego
                        #juego(Pant,aux,ang_ROJO,vel_ROJO,ang_AZUL,vel_AZUL)
                #Detecta los click del mouse     
                if event.type == MOUSEBUTTONDOWN:
                    #Detecta click en el boton
                    if event.button == 1:
                        click = True
                        
            #Actualiza la pantalla
            pygame.display.update()
            

if __name__ == '__main__':
    Menus.main_menu(mapa)