from .Rectangulos import Rectangulos
import random as r

class Tanque:
    def __init__(self,x,y):
        self.vida = 100
        self.balas105 = 10
        self.balasperforantes = 10
        self.balas60 = 10
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidad = 0
        self.color = (r.randint(0,255), r.randint(0,255), r.randint(0,255))
        self.estado = False
        self.IA = False
        self.kill = 0
    
    def reinicio (self,x,y):
        self.vida = 100
        self.balas105 = 10
        self.balasperforantes = 10
        self.balas60 = 10
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidad = 0
        self.color = (r.randint(0,255), r.randint(0,255), r.randint(0,255))
        self.kills = 0
        
    def set_Vida (self, nuevaVida):
        self.vida = nuevaVida
    
    def get_Vida (self):
        return self.vida
    
    def set_Balas (self, balas105,balasPerforante,balas60):
        self.balas105 = balas105
        self.balasperforantes = balasPerforante
        self.balas60 = balas60
    
    def get_Balas (self):
        return self.balas105, self.balasperforantes, self.balas60
    
    def set_X (self, nuevaPosicion):
        self.x = nuevaPosicion
    
    def get_X (self):
        return self.x
    
    def set_Y (self, nuevaPosicion):
        self.y = nuevaPosicion
    
    def get_Y (self):
        return self.y
    
    def set_Angulo (self, nuevoAngulo):
        self.angulo = nuevoAngulo
    
    def get_Angulo (self):
        return self.angulo
    
    def set_Velocidad (self, nuevaVelocidad):
        self.velocidad = nuevaVelocidad
    
    def get_Velocidad (self):
        return self.velocidad

    def set_Estado (self, nuevoEstado):
        self.estado = nuevoEstado
    
    def get_Estado (self):
        return self.estado
    
    #Dibuja lo visual de los tanques
    def dibuja_tanques(Pant, color, x, y):
        Rectangulos.dibujaRectangulos(Pant,color,(x,y,1,1),0)

    #Posiciona los tanques
    def hacer_tanques(mapa, x,jugador):
        y = 420
        Aux = 1
        #Los acomoda segun el limite de los cañones y las montañas
        while mapa[y+29][x] == 1 and mapa[y+30][x] == 1:
            y -= 1
        while mapa[y+30][x] == 0:
            y += 1  
        contx = x
        conty = y
        #Sin esto no dibuja los tankes
        while y < conty+15:
            Define_color = contx
            #Sin esto dibuja la mitad de los tankes
            while x < contx+15:
                while (Define_color+Aux) > contx:
                    mapa[y][Define_color+Aux] = jugador.color
                    mapa[y][Define_color] = jugador.color
                    Define_color -= 1
                x += 1
            y += 1
            Aux += 1
            x = contx
        #Sin esto dibuja solo la mitad de arriba
        while y < conty+30:
            Define_color = contx
            while x < contx+30:
                while (Define_color+Aux) > contx:
                    mapa[y][Define_color+Aux] = jugador.color
                    mapa[y][Define_color] = jugador.color
                    Define_color -= 1
                x += 1
            y += 1
            Aux -= 1
            x = contx
        
        #Sin esto no pone la vida del de la izquierda
        jugador.set_X(x)
        jugador.set_Y(y)