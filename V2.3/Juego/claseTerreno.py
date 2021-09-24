from .Variables import Pant, Verde, Celeste
import pygame
import random as r

class Terreno:
    a = r.randint(2,21) #PUNTA IZQUIERDA
    b = r.randint(21,40) #PUNTA DERECHA
    e = r.randint(2,21) #CAÑON IZQUIERDO
    f = r.randint(21,40) #CAÑON DERECHO
    def generar_terreno(posicion):
        ##TERRENO##
        pygame.draw.rect(Pant,Verde, #Suelo
                        (0,
                        Pant.get_height()/2,
                        Pant.get_width(),
                        Pant.get_height()/2))
        
        pygame.draw.polygon(Pant,Verde, #El poligono mas cercano al azul
                        (((Terreno.a*posicion)+100,100), #arriba FUNCIONA X,Y
                        ((Terreno.a*posicion)+200,Pant.get_height()), #derecha
                        ((Terreno.a*posicion)+100,400), #abajo
                        (Terreno.a*posicion,Pant.get_height()))) #izquierda

        pygame.draw.polygon(Pant,Verde,
                        (((Terreno.b*posicion)+100,100), #arriba
                        ((Terreno.b*posicion)+200,Pant.get_height()), #derecha
                        ((Terreno.b*posicion)+100,400), #abajo
                        (Terreno.b*posicion,Pant.get_height()))) #izquierda
        
        pygame.draw.polygon(Pant,Celeste,
                        (((Terreno.e*posicion)+100,Pant.get_height()/2), #arriba
                        ((Terreno.e*posicion)+200,Pant.get_height()/2), #derecha
                        ((Terreno.e*posicion)+100,400), #abajo
                        (Terreno.e*posicion,Pant.get_height()/2))) #izquierda

        pygame.draw.polygon(Pant,Celeste,
                        (((Terreno.f*posicion)+100,Pant.get_height()/2), #arriba
                        ((Terreno.f*posicion)+200,Pant.get_height()/2), #derecha
                        ((Terreno.f*posicion)+100,400), #abajo
                        (Terreno.f*posicion,Pant.get_height()/2))) #izquierda