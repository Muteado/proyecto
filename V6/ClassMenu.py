from Juego.claseTerreno import Terreno
from Juego.claseJuego import Juego
import pygame, sys
import sys
from pygame import *
from Juego.ClassOpciones import OpcionesCat
from Juego.ClassRectangulos import Rectangulos
from Juego.ClassTextos import Textos
from Juego.Variables import Amarillo, Blanco, Negro, Pant, mapa, Turno, Partida

class Menus:
    def main_menu(mapa):
        #Variable auxiliar fuera del while
        angu_ROJO = ''
        velo_ROJO = ''
        angu_AZUL = ''
        velo_AZUL = ''
        Turno[0] = 1
        Partida[0] = 0
        aux = False
        click = False
        mapa = Terreno.run(mapa)
        while True:
            ##Genera el juego sin comenzarlo##
            #Variable auxiliar
            aux=False
            #Juego.juego(Pant,aux,angu_ROJO,velo_ROJO,angu_AZUL,velo_AZUL, mapa)
            Pant.fill(Negro)
            #Genera el titulo Menu
            Textos.texto_pantalla_rect('Menú', Textos.fuentes(None,80),Blanco,Pant,(Pant.get_width()/2)-75, 20)
            #Detecta posicion mouse
            mousex, mousey = pygame.mouse.get_pos()
            #Crea 2 rectangulos para los botones 1 y 2 correspondientemente
            boton1 = Rectangulos.rectangulo((Pant.get_width()/2)-100, 100, 200, 50) #JUGAR
            boton2 = Rectangulos.rectangulo((Pant.get_width()/2)-100, 200, 200, 50) #OPCIONES
            #Detecta el click en el boton1
            if boton1.collidepoint((mousex, mousey)):
                if click:
                    #Actualiza la variable auxiliar
                    aux=True
                    #Ejecuta el juego
                    Juego.juego(Pant,aux,angu_ROJO,velo_ROJO,angu_AZUL,velo_AZUL, mapa)
                    #juego(Pant,aux,ang_ROJO,vel_ROJO,ang_AZUL,vel_AZUL)
            #Detecta el click en el boton2
            if boton2.collidepoint((mousex, mousey)):
                if click:
                    #Ejecuta la sección opciones
                    OpcionesCat.opciones()
            #Dibuja los rectangulos de los botones 1 y 2 correspondientemente
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton1,0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton2,0)
            #Genera los textos de ambos botones
            Textos.texto_pantalla_rect('JUEGO', Textos.fuentes(None,50), Blanco, Pant, (Pant.get_width()/2)-60, 110)
            Textos.texto_pantalla_rect('OPCIONES', Textos.fuentes(None,50), Blanco, Pant, (Pant.get_width()/2)-90, 210)
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



'''
Generalizar clase tanque @Mute
Construir imagenes, en vez de un cuadrado que sea una imagen .PNG @Paz
Que la bala salga del tanque @conan
que registre datos la bala @Mari

Implementar bien los turnos
Validar tiros fuera del rango



'''