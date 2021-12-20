import sys
from Juego.ClaseBotones import *
from Juego.claseJuego import Juego
from Juego.ClassTextos import Textos
from Juego.claseTerreno import Terreno
from Juego.ClassOpciones import OpcionesCat
from Juego.ClassRectangulos import Rectangulos
from Juego.Variables import *

class Menus:
    def main_menu(mapa):
        #VARIABLES DATOS INGRESADOS
        angu_ROJO = ''
        velo_ROJO = ''
        angu_AZUL = ''
        velo_AZUL = ''
        #VARIABLES INCIO DEL JUEGO
        Turno[0] = 1
        Partida[0] = 0
        #OTRAS VARIABLES
        click = False
        iniciada = False
        #CREA EL MAPA
        mapa = Terreno.run(mapa)
        #CICLO PRINCIPAL
        while True:
            #Da fondo a la pantalla
            Pant.fill(Negro)
            #Genera el titulo Menu
            Textos.texto_pantalla_rect('Menú', Textos.fuentes(None,80),Blanco,Pant,(Pant.get_width()/2)-75, 20)
            #Detecta posicion mouse
            mousex, mousey = pygame.mouse.get_pos()
            #Crea 3 rectangulos para los botones 1, 2 y 3 correspondientemente
            boton1 = Rectangulos.rectangulo((Pant.get_width()/2)-150, 200, 300, 50) #NUEVA PARTIDA
            boton2 = Rectangulos.rectangulo((Pant.get_width()/2)-150, 300, 300, 50) #INSTRUCCIONES
            boton3 = Rectangulos.rectangulo((Pant.get_width()/2)-150, 400, 300, 50) #SALIR    
            #Detecta el click en el boton1
            if boton1.collidepoint((mousex, mousey)):
                if click:
                    #Reinicia todas las variables para la nueva partida
                    angu_ROJO = ''
                    velo_ROJO = ''
                    angu_AZUL = ''
                    velo_AZUL = ''
                    Turno[0] = 1
                    Partida[0] = 0
                    click = False
                    Partida[0] = 0
                    #Genera el nuevo mapa
                    mapa = Terreno.run(mapa)
                    iniciada = Juego.juego(Pant,angu_ROJO,velo_ROJO,angu_AZUL,velo_AZUL, mapa)
                    #Variable auxiliar para reconocer una partida nueva
                    iniciada=True
            #Detecta el click en el boton2
            if boton2.collidepoint((mousex, mousey)):
                if click:
                    #Muestra las instrucciones
                    Pant.fill(Negro)
                    OpcionesCat.instrucciones()
            #Detecta el click en el boton3
            if boton3.collidepoint((mousex, mousey)):
                if click:
                    #Cierra el juego
                    pygame.quit()
                    sys.exit()
            #Dibuja los rectangulos de los botones
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton1,0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton2,0)
            Rectangulos.dibujaRectangulos(Pant, Amarillo, boton3,0)
            #Genera los textos de los botones
            if iniciada == False:
                #En caso de ser primera partida
                Textos.texto_pantalla_rect('JUGAR', Textos.fuentes(None,50), Negro, Pant, (Pant.get_width()/2)-60, 210)
            if iniciada == True:
                #En caso de ser una partida ya en juego
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
                        #Ejecuta el juego
                        iniciada =  Juego.juego(Pant,angu_ROJO,velo_ROJO,angu_AZUL,velo_AZUL, mapa)       
                #Detecta los click del mouse     
                if event.type == MOUSEBUTTONDOWN:
                    #Detecta click en el boton
                    if event.button == 1:
                        click = True    
            #Actualiza la pantalla
            pygame.display.update()
            
#Ejecuta el programa
if __name__ == '__main__':
    Menus.main_menu(mapa)