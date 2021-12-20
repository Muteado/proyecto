from .Variables import *
from .Rectangulos import *


#Tanque 1
balaspj1[0] = 3
balaspj1[1] = 10
balaspj1[2] = 3

#Tanque 2
balaspj2[0] = 3
balaspj2[1] = 10
balaspj2[2] = 3

#Tanque 3
balaspj3[0] = 3
balaspj3[1] = 10
balaspj3[2] = 3

#Tanque 4
balaspj4[0] = 3
balaspj4[1] = 10
balaspj4[2] = 3


#Vida Tanques
vidaTank[0] = 100
vidaTank[1] = 100

# Detecta la posicion del mouse
mousex1, mousey1 = pygame.mouse.get_pos()
#Detecta la posicion del mouse encima del rectangulo de los colores
botonamarillo1 = Rectangulos.rectangulo(605,5,30,20)
botonnaranja1 = Rectangulos.rectangulo(640,5,30,20)
botonmorado1 = Rectangulos.rectangulo(675,5,30,20)
