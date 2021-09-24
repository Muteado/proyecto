from Juego.ClassRectangulos import Rectangulos
import pygame
import random 
from .Variables import Azul, Rojo, Pant


class Tanque:
    def dibujar_tanque_Rojo(Pant,x,y):
        Rectangulos.dibujaRectangulos(Pant,Rojo,(x,y,1,1),0)

    def dibujar_tanque_Azul(Pant,x,y):
        Rectangulos.dibujaRectangulos(Pant,Azul,(x,y,1,1),0)
    
    #define la posicion del tanque azul
    def hacer_Tanque_Azul(mapa):
        x = random.randint(40,426)
        y = 420
        Aux = 1
        while mapa[y+29][x] == 1 and mapa[y+30][x] == 1:
            y -= 1
        while mapa[y+30][x] == 0:
            y += 1
        contx = x
        conty = y
        while y < conty+15:
            Define_colorAzul = contx
            while x < contx+15:
                while (Define_colorAzul+Aux) > contx:
                    mapa[y][Define_colorAzul+Aux] = 2
                    mapa[y][Define_colorAzul] = 2
                    Define_colorAzul -= 1
                x += 1
            y += 1
            Aux += 1
            x = contx
        while y < conty+30:
            Define_colorAzul = contx
            while x < contx+30:
                while (Define_colorAzul+Aux) > contx:
                    mapa[y][Define_colorAzul+Aux] = 2
                    mapa[y][Define_colorAzul] = 2
                    Define_colorAzul -= 1
                x += 1
            y += 1
            Aux -= 1
            x = contx

    #define la posicion del tanque rojo
    def hacer_Tanque_Rojo(mapa):
        x = random.randint(800,1240)
        y = 420
        Aux = 1
        while mapa[y+29][x] == 1 and mapa[y+30][x] == 1:
            y -= 1
        while mapa[y+30][x] == 0:
            y += 1
        contx = x
        conty = y
        while y < conty+15:
            Define_colorRojo = contx
            while x < contx+15:
                while (Define_colorRojo+Aux) > contx:
                    mapa[y][Define_colorRojo+Aux] = 3
                    mapa[y][Define_colorRojo] = 3
                    Define_colorRojo -= 1
                x += 1
            y += 1
            Aux += 1
            x = contx
        while y < conty+30:
            Define_colorRojo = contx
            while x < contx+30:
                while (Define_colorRojo+Aux) > contx:
                    mapa[y][Define_colorRojo+Aux] = 3
                    mapa[y][Define_colorRojo] = 3
                    Define_colorRojo -= 1      
                x += 1
            y += 1
            Aux -= 1
            x = contx