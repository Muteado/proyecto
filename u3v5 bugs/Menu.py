import sys
from Juego.Tanques import *
from Juego.Variables import *
from Juego.Juego import Juego
from Juego.Textos import Textos
from Juego.Terreno import Terreno
from Juego.Opciones import OpcionesCat
from Juego.Rectangulos import Rectangulos
from Juego.PosicionTanque import posicion_aparicion
from Juego.Turnos import Turnos



class Menus:
    def main_menu(mapa):
        #VARIABLES DATOS INGRESADOS
        Pantaux = pygame.display.set_mode([(largoaux[0]),(anchoaux[0])])
        angulo_Jugador = ''
        velocidad_Jugador = ''
        #VARIABLES INCIO DEL JUEGO
        turnoJugador = 0
        Partida[0] = 0
        #OTRAS VARIABLES
        click = False
        iniciada = False
        
        #CICLO PRINCIPAL
        while True:
            #Da fondo a la pantalla
            Pantaux.fill(Negro)
            #Genera el titulo Menu
            Textos.texto_pantalla_rect('Menú', Textos.fuentes(None,80),Blanco,Pantaux,(Pantaux.get_width()/2)-75, 20)
            #Detecta posicion mouse
            mousex, mousey = pygame.mouse.get_pos()
            #Crea 3 rectangulos para los botones 1, 2 y 3 correspondientemente
            boton1 = Rectangulos.rectangulo((Pantaux.get_width()/2)-150, 100, 300, 50) #NUEVA PARTIDA #x #y #ancho #alto
            boton2 = Rectangulos.rectangulo((Pantaux.get_width()/2)-150, 200, 300, 50) #INSTRUCCIONES
            boton3 = Rectangulos.rectangulo((Pantaux.get_width()/2)-150, 300, 300, 50) #OPCIONES
            boton4 = Rectangulos.rectangulo((Pantaux.get_width()/2)-150, 400, 300, 50) #SALIR    
            #Detecta el click en el boton1
            if boton1.collidepoint((mousex, mousey)):
                if click:
                    #Reinicia todas las variables para la nueva partida
                    Pant = pygame.display.set_mode([(largo[0]),(ancho[0])])
                    angulo_Jugador = ''
                    velocidad_Jugador = ''
                    turnoJugador = 0
                    Partida[0] = 0
                    click = False
                    jugador1.reinicio(0,0)
                    jugador2.reinicio(0,0)
                    jugador3.reinicio(0,0)
                    jugador4.reinicio(0,0)
                    jugador5.reinicio(0,0)
                    jugador6.reinicio(0,0)
                    #Genera el nuevo mapa
                    Turnos.Turno_Tanque()
                    posicion_aparicion()
                    mapa = Terreno.run(mapa)
                    iniciada = Juego.juego(Pant,angulo_Jugador,velocidad_Jugador, mapa,turnoJugador)
                    #Variable auxiliar para reconocer una partida nueva
                    iniciada=True
            #Detecta el click en el boton2
            if boton2.collidepoint((mousex, mousey)):
                if click:
                    #Muestra las instrucciones
                    Pantaux.fill(Negro)
                    OpcionesCat.instrucciones()                         
            #Detecta el click en el boton3
            if boton3.collidepoint((mousex, mousey)):
                if click:
                    #Muestra las opciones
                    Pantaux.fill(Negro)
                    jugador1.reinicio(0,0)
                    jugador2.reinicio(0,0)
                    jugador3.reinicio(0,0)
                    jugador4.reinicio(0,0)
                    jugador5.reinicio(0,0)
                    jugador6.reinicio(0,0)
                    iniciada = OpcionesCat.opciones(iniciada)
                    if iniciada == True:
                        #Reinicia todas las variables para la nueva partida
                        Pant = pygame.display.set_mode([(largo[0]),(ancho[0])])
                        angulo_Jugador = ''
                        velocidad_Jugador = ''
                        turnoJugador = 0
                        Partida[0] = 0
                        click = False
                        Turnos.Turno_Tanque()
                        posicion_aparicion()
                        #Genera el nuevo mapa
                        mapa = Terreno.run(mapa)
                        
                        iniciada = Juego.juego(Pant,angulo_Jugador,velocidad_Jugador, mapa,turnoJugador)
                        #Variable auxiliar para reconocer una partida nueva
                        iniciada=True
            if boton4.collidepoint((mousex, mousey)):
                if click:
                    #Cierra el juego
                    pygame.quit()
                    sys.exit()
            #Dibuja los rectangulos de los botones
            Rectangulos.dibujaRectangulos(Pantaux, Amarillo, boton1,0)
            Rectangulos.dibujaRectangulos(Pantaux, Amarillo, boton2,0)
            Rectangulos.dibujaRectangulos(Pantaux, Amarillo, boton3,0)
            Rectangulos.dibujaRectangulos(Pantaux, Amarillo, boton4,0)
            #Genera los textos de los botones
            if iniciada == False:
                #En caso de ser primera partida
                Textos.texto_pantalla_rect('JUGAR', Textos.fuentes(None,50), Negro, Pantaux, (Pantaux.get_width()/2)-60, 110)
            if iniciada == True:
                #En caso de ser una partida ya en juego
                Textos.texto_pantalla_rect('NUEVA PARTIDA', Textos.fuentes(None,50), Negro, Pantaux, (Pantaux.get_width()/2)-140, 110)
            Textos.texto_pantalla_rect('INSTRUCCIONES', Textos.fuentes(None,50), Negro, Pantaux, (Pantaux.get_width()/2)-145, 210)
            Textos.texto_pantalla_rect('OPCIONES', Textos.fuentes(None,50), Negro, Pantaux, (Pantaux.get_width()/2)-90, 310)
            Textos.texto_pantalla_rect('SALIR', Textos.fuentes(None,50), Negro, Pantaux, (Pantaux.get_width()/2)-50, 410)
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
                        Pant = pygame.display.set_mode([(largo[0]),(ancho[0])])
                        if iniciada == True:
                            
                            iniciada = Juego.juego(Pant,angulo_Jugador,velocidad_Jugador, mapa,turnoJugador)    
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