import sys, math
import pygame
from pygame import *
from .Variables import Pant, Negro


class Entrada ():
    def __init__(self,Pant,):
        self.lineas = 0
        self.numeros = ['.',]
        self.fuente = pygame.font.Font(None, 20)

        self.distancia = 15
        self.posX =0
        self.posY=0
        self.largoBloq = 200
        self.altoBloq = 20
        def teclas(self, Pant):
            
            #se recorre con la accion de la lista de eventos
            for event in pygame.event.get():
                for accion in event:
                    #se ve que la tecla sea igual a la presionada
                    if accion.type == KEYDOWN:
                        # se ve el valor que retorna
                        if accion.key == K_RETURN:
                            #se almacena en mi lista lineas
                            self.numeros.append('')
                            self.lineas += 1
                        #tecla para salir (debo colocar que se guarde con esto)
                        elif accion.key == K_ESCAPE:
                            sys.exit()
                        #se borra el texto con la tecla borrar
                        elif accion.key == K_BACKSPACE:
                            if self.numeros[self.lineas]== '' and self.lineas>0:
                                self.numeros = self.numeros[0:-1]
                                self.lineas -=1
                            #
                            else:
                                self.numeros[self.lineas]=self.numeros[self.lineas][0:-1]
                        #aqui se deja estatico
                        else:
                            self.numeros[self.lineas] = str(self.numeros[self.lineas] + accion.unicode)
            
        def mensaje (self,Pant ):
            for self.lineas in range(len(self.numeros)):
                Img_letra = self.fuente.render(self.numeros[self.lineas], True,(Negro))
                Pant.blit(Img_letra,(self.posX+self.largoBloq/2-15, self.posY+1))






"faltante"
"posicionarlo en las esquinas" "esta posicionado para rojo"
"retornar los valores a mov parabolico"
"dejar implementado el codigo para dos lineas y con enter los datos se retornen"
"falta implementar esta clase con los turno, otraS IDEAS para implementar los turnos"
