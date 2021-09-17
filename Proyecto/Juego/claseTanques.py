from Juego.ClassRectangulos import Rectangulos

class Tanque:
    def dibuja_tanques(Pant, color, x, y):
        Rectangulos.dibujaRectangulos(Pant,color,(x,y,1,1),0)

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
