import pygame, sys
from pygame.locals import *
from .Tanques import *
#FUNCIONES DE PYGAME
pygame.init()
reloj = pygame.time.Clock()

#PANTALLA
largo = [0]
ancho = [0]
largoaux = [0] 
anchoaux = [0]

largoaux[0]= 1280
anchoaux[0]= 800
largo[0]=800
ancho[0]=800
pygame.display.set_caption("The Battle of the Tanks")
Pant = pygame.display.set_mode([(largo[0]),(ancho[0])])
Pantaux = pygame.display.set_mode([(largoaux[0]),(anchoaux[0])])
mousex, mousey = pygame.mouse.get_pos()

#COLORES
Celeste = (54,203,201)
Verde = (44,177,26)
Azul = (0,0,255)
Blanco = (255,255,255)
#colores que pueden ser para tanques
Amarillo = (255, 255, 0)
Naranja = (253,126,0)
Morado = (105,0,144)
Negro = (0,0,0)
Rojo = (255, 0, 0) 



X_Y_Tanques = [0,1,2,3,4,5,6,7,8,9,10,11] #X1,Y1,X2,Y2,X3,Y3,X4,Y4,X5,Y5,X6,Y6


Angulo_Jugador = [0,1,2,3,4,5]
Velocidad_Jugador = [0,1,2,3,4,5]

posiciones_X = [0,1,2,3,4,5]
corroborar_conteo = [0,1,2,3,4,5]
Lista_Jugadores = [0,1,2,3,4,5]
Lista_Jugadores[0] = -1
Lista_Jugadores[1] = -1
Lista_Jugadores[2] = -1
Lista_Jugadores[3] = -1
Lista_Jugadores[4] = -1
Lista_Jugadores[5] = -1

Lista_Kills = [0,1,2,3,4,5]


#BALAS
Balaaux = [0]

#OTRAS VARIABLES DEL JUEGO

Partida = [0]
aux = False
mapa = []
prueba = 0
text = str

balas105 = 10
balasperforante = 10
balas60 = 10

vida = 100

#Clima
Viento_Movimiento = [0]
Viento_Movimiento[0] = False
Gravedad = [0]
Gravedad[0] = 10

angulo = [0]
velocidad = [0]
botonamarilloIA = [0]
botonnaranjaIA = [0]
botonmoradoIA = [0]
IAR = [0]
IAR[0] = 0
jugadores = [0]
jugadores[0] = 2
jugador1 = Tanque(0,0)
jugador2 = Tanque(0,0)
jugador3 = Tanque(0,0)
jugador4 = Tanque(0,0)
jugador5 = Tanque(0,0)
jugador6 = Tanque(0,0)
jugador1.set_Estado(True)
jugador2.set_Estado(True)
gravedad = 0
viento = 0