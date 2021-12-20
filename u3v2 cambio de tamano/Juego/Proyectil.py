import math
from .Variables import *
class Proyectil():
    """Clase que representa el proyectil lanzado"""
    def __init__(self, x, y, ang, velo):
        self.angulo = ang#angulo
        self.veloc = velo#velocidad
        self.tiempo = 0
        self.x = x+35
        self.xUsar = x
        self.y = y-35
        self.disparar = False
        self.xreal = x
        self.yreal = ancho - self.y
        self.yUsar = ancho - self.y

    def update(self,x,y):
        "actualizar la posición del proyectil"
        self.velocx = self.veloc * math.cos(math.radians(self.angulo))
        self.velocy = self.veloc * math.sin(math.radians(self.angulo))

        if self.disparar is True:
            # esta en movimiento, hay que actualizar la posición
            '''
            Lo "normal" sería false?
            if viento = true:
                x + la cant de viento
            '''
            self.xreal = (x + self.velocx * self.tiempo)
            '''
            Lo "normal sería 0?"
            if gravedad = true:
                y + o - la cant de gravedad
            '''
            self.yreal = (y + self.velocy * self.tiempo +
                          (-9.8 * (self.tiempo ** 2)) / 2)
            # Corregir la posición en el eje vertical
            self.x = self.xreal
            self.y = ancho - self.yreal
        else:
            # se mantiene sin disparar, por lo cual no se hace nada
            pass
