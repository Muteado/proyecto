from Juego.ClassRectangulos import Rectangulos
import pygame
import random 
from .Variables import Azul, Rojo, Pant, XdeTankA, XdeTankR, imagen, imagen2, rect, rest, estado


class Tanque:
    def __init__(self):
        self.posxazul = posxazul
        self.posxrojo = posxrojo
        self.imagen = pygame.image.load("tanquem.png") #TANQUE IZQUIERDO
        self.imagen = transform.scale(self.imagen,(60,60))
        self.imagen2 = pygame.image.load("tanquem2.png") #TANQUE DERECHO
        self.imagen2 = transform.scale(self.imagen2,(60,60))
        
        #estado hace mencion al estado de si es player 1 o 2
        self.estado = estado
        estado = 0
        
        #Tanque Izquierdo?
        self.rect=self.imagen.get_rect()
        self.rect.centerx= ancho - 500
        self.rect.centery=420
    
        #Tanque Derecho?
        self.rest=self.imagen2.get_rect()
        self.rest.centerx= ancho+ancho
        self.rest.centery=420
        
        #dibujo de tanque
        Pant.blit(self.imagen,self.rect)
        Pant.blit(self.imagen2,self.rest)
        
    
    def dibujar_tanque(importtanques,centrodetanques):
        Pant.blit(importtanques,centrodetanques)
        print("")
        
    
    def tanque(estado, XdeTankA,XdeTankR,y):
        #dibujar_tanque(Pant,imagen,rect)
        #dibujar_tanque(Pant,imagen2,rest)
        
        if estado == 0: #Tanque Azul
            Aux = 1
            while mapa[y+29][XdeTankA] == 1 and mapa[y+30][XdeTankA] == 1:
                y -= 1
            while mapa[y+30][XdeTankA] == 0:
                y += 1
            contx = XdeTankA
            conty = y
            while y < conty+15:
                Define_colorAzul = contx
                while XdeTankA < contx+15:
                    while (Define_colorAzul+Aux) > contx:
                        mapa[y][Define_colorAzul+Aux] = 2
                        mapa[y][Define_colorAzul] = 2
                        Define_colorAzul -= 1
                    XdeTankA += 1
                y += 1
                Aux += 1
                XdeTankA = contx
            while y < conty+30:
                Define_colorAzul = contx
                while XdeTankA < contx+30:
                    while (Define_colorAzul+Aux) > contx:
                        mapa[y][Define_colorAzul+Aux] = 2
                        mapa[y][Define_colorAzul] = 2
                        Define_colorAzul -= 1
                    XdeTankA += 1
                y += 1
                Aux -= 1
                XdeTankA = contx
            estado = 1
            print("Hola mundo 1")
        
        if estado == 1:
            Aux = 1
            while mapa[y+29][XdeTankR] == 1 and mapa[y+30][XdeTankR] == 1:
                y -= 1
            while mapa[y+30][XdeTankR] == 0:
                y += 1
            contx = XdeTankR
            conty = y
            while y < conty+15:
                Define_colorRojo = contx
                while XdeTankR < contx+15:
                    while (Define_colorRojo+Aux) > contx:
                        mapa[y][Define_colorRojo+Aux] = 3
                        mapa[y][Define_colorRojo] = 3
                        Define_colorRojo -= 1
                    XdeTankR += 1
                y += 1
                Aux += 1
                XdeTankR = contx
            while y < conty+30:
                Define_colorRojo = contx
                while XdeTankR < contx+30:
                    while (Define_colorRojo+Aux) > contx:
                        mapa[y][Define_colorRojo+Aux] = 3
                        mapa[y][Define_colorRojo] = 3
                        Define_colorRojo -= 1      
                    XdeTankR += 1
                y += 1
                Aux -= 1
                XdeTankR = contx
            estado = 2
            print("Hola mundo 2")
        if estado == 2:
            print("Aqui debe ir el sistema de turnos?")
    
'''class Tanque:
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
            
            
            '''