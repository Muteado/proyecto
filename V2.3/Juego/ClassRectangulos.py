import pygame
class Rectangulos:
    #Genera rectangulos
    def rectangulo(x,y,x1,y1):
        #x = valor de izquierda a derecha
        #y = valor de arriba a abajo
        #x1 = largo rectangulo
        #y1 = alto rectangulo
        rect= pygame.Rect((x,y,x1,y1))
        return rect
    
    def dibujaRectangulos(pantalla, color, rectangulo,borde):
        pygame.draw.rect(pantalla, color, rectangulo,borde)


