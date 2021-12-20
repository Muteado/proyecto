from .ClassRectangulos import Rectangulos
from .Variables import *

class Tanque:
    #Dibuja lo visual de los tanques
    def dibuja_tanques(Pant, color, x, y):
        Rectangulos.dibujaRectangulos(Pant,color,(x,y,1,1),0)

    #Posiciona los tanques
    def hacer_tanques(mapa, x, estado):
        y = 420
        Aux = 1
        while mapa[y+29][x] == 1 and mapa[y+30][x] == 1:
            y -= 1
        while mapa[y+30][x] == 0:
            y += 1
        contx = x
        conty = y
        while y < conty+15:
            Define_color = contx
            while x < contx+15:
                while (Define_color+Aux) > contx:
                    mapa[y][Define_color+Aux] = estado
                    mapa[y][Define_color] = estado
                    Define_color -= 1
                x += 1
            y += 1
            Aux += 1
            x = contx
        while y < conty+30:
            Define_color = contx
            while x < contx+30:
                while (Define_color+Aux) > contx:
                    mapa[y][Define_color+Aux] = estado
                    mapa[y][Define_color] = estado
                    Define_color -= 1
                x += 1
            y += 1
            Aux -= 1
            x = contx
        if x < 500:
            X_Y_Tanques[0] = x
            X_Y_Tanques[1] = y
        if x > 700:
            X_Y_Tanques[2] = x
            X_Y_Tanques[3] = y
