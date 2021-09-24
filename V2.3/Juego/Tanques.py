import pygame
import random as r
from Variables import Azul, Rojo, Pant

mapa=[]
class Tanque:
    
    
    def __init__(self,posicionazul,posicionrojo,tanqueazul,tanquerojo):
        self.posicionazul=posicionazul
        self.posicionrojo=posicionrojo
        self.tanqueazul=tanqueazul
        self.tanquerojo=tanquerojo

    #posicionazul = r.randint(2,14) #Determina la posicion del tanque AZUL
    #posicionrojo = r.randint(28,40) #Determina la posicion del tanque ROJO
    
    
    def hacer_Tanque_Rojo():
        x = r.randint(40,426)
        y = 420
        peo = 1
        while mapa[y+29][x] == 1 and mapa[y+30][x] == 1:
            y -= 1
        while mapa[y+30][x] == 0:
            y += 1

        contx = x
        conty = y
        
        while y < conty+15:
            Define_colorRojo = contx
            while x < contx+15:

                while (Define_colorRojo+peo) > contx:
                    mapa[y][Define_colorRojo+peo] = 2
                    mapa[y][Define_colorRojo] = 2
                    Define_colorRojo -= 1

                x += 1
            y += 1
            peo += 1
            x = contx

        while y < conty+30:
            Define_colorRojo = contx
            while x < contx+30:

                while (Define_colorRojo+peo) > contx:
                    mapa[y][Define_colorRojo+peo] = 2
                    mapa[y][Define_colorRojo] = 2
                    Define_colorRojo -= 1

                x += 1
            y += 1
            peo -= 1
            x = contx


    def hacer_Tanque_Azul():
        x = r.randint(800,1240)
        y = 420
        peo = 1
        while mapa[y+29][x] == 1 and mapa[y+30][x] == 1:
            y -= 1
        while mapa[y+30][x] == 0:
            y += 1

        contx = x
        conty = y
        
        while y < conty+15:
            Define_colorAzul = contx
            while x < contx+15:

                while (Define_colorAzul+peo) > contx:
                    mapa[y][Define_colorAzul+peo] = 3
                    mapa[y][Define_colorAzul] = 3
                    Define_colorAzul -= 1

                x += 1
            y += 1
            peo += 1
            x = contx

        while y < conty+30:
            Define_colorAzul = contx
            while x < contx+30:

                while (Define_colorAzul+peo) > contx:
                    mapa[y][Define_colorAzul+peo] = 3
                    mapa[y][Define_colorAzul] = 3
                    Define_colorAzul -= 1
                    
                x += 1
            y += 1
            peo -= 1
            x = contx
