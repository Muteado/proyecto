from .Variables import *
from .Tanques import *
from .Botones import *
from .Esquinas import *
from .Terreno import Terreno

#Función para la destruccion del terreno
def posicion():
    #Se valida la posicion del tanque Rojo luego de la destruccion de terreno
    if X_Y_Tanques[3]+1 < ancho:
        if mapa[(X_Y_Tanques[3])+1][X_Y_Tanques[2]] == 0 or mapa[(X_Y_Tanques[3])+2][X_Y_Tanques[2]] == 0:
            estado = 0
            Aux = 1
            X_Y_Tanques[3] -= 30
            contx = X_Y_Tanques[2]
            conty = X_Y_Tanques[3]

            while X_Y_Tanques[3] < conty+15:
                Define_color = contx
                while X_Y_Tanques[2] < contx+15:
                    while (Define_color+Aux) > contx:
                        mapa[X_Y_Tanques[3]][Define_color+Aux] = estado
                        mapa[X_Y_Tanques[3]][Define_color] = estado
                        Define_color -= 1
                    X_Y_Tanques[2] += 1
                X_Y_Tanques[3] += 1
                Aux += 1
                X_Y_Tanques[2] = contx

            while X_Y_Tanques[3]< conty+30:
                Define_color = contx
                while X_Y_Tanques[2] < contx+30:
                    while (Define_color+Aux) > contx:
                        mapa[X_Y_Tanques[3]][Define_color+Aux] = estado
                        mapa[X_Y_Tanques[3]][Define_color] = estado
                        Define_color -= 1
                    X_Y_Tanques[2] += 1
                X_Y_Tanques[3] += 1
                Aux -= 1
                X_Y_Tanques[2] = contx

            if X_Y_Tanques[2] > 700:
                X_Y_Tanques[2] = X_Y_Tanques[2]
                X_Y_Tanques[3] = X_Y_Tanques[3]

            y = X_Y_Tanques[3]
            x = X_Y_Tanques[2]
            Aux = 1
            Ver = False

            if y+30 >= ancho:
                Ver = True

            if Ver == False:
                while mapa[y+30][x] == 0:
                    y += 1
                    if y+30 > ancho:
                        Ver = True
                        break

            if Ver == False:
                contx = x
                conty = y
                while y < conty+15:
                    Define_color = contx
                    while x < contx+15:
                        while (Define_color+Aux) > contx:
                            mapa[y][Define_color+Aux] = 3
                            mapa[y][Define_color] = 3
                            Define_color -= 1
                        x += 1
                    y += 1
                    Aux += 1
                    x = contx
                while y < conty+30:
                    Define_color = contx
                    while x < contx+30:
                        while (Define_color+Aux) > contx:
                            mapa[y][Define_color+Aux] = 3
                            mapa[y][Define_color] = 3
                            Define_color -= 1
                        x += 1
                    y += 1
                    Aux -= 1
                    x = contx


                X_Y_Tanques[2] = x
                X_Y_Tanques[3] = y

                #Actualiza la pantalla
                Terreno.dibuja_mapa(Pant,mapa)
                pygame.display.update()

            #Si el tanque rojo cae pierde la partida
            else:
                vidaTank[1] = 0
                Terreno.dibuja_mapa(Pant,mapa)
                pygame.display.update()
    

    #Se valida la posicion del tanque Azul luego de la destruccion del terreno
    if X_Y_Tanques[1]+1 < ancho:
        if mapa[(X_Y_Tanques[1])+1][X_Y_Tanques[0]] == 0 or mapa[(X_Y_Tanques[1])+2][X_Y_Tanques[0]] == 0:

            estado = 0
            Aux = 1
            X_Y_Tanques[1] -= 30
            contx = X_Y_Tanques[0]
            conty = X_Y_Tanques[1]

            while X_Y_Tanques[1] < conty+15:
                Define_color = contx
                while X_Y_Tanques[0] < contx+15:
                    while (Define_color+Aux) > contx:
                        mapa[X_Y_Tanques[1]][Define_color+Aux] = estado
                        mapa[X_Y_Tanques[1]][Define_color] = estado
                        Define_color -= 1
                    X_Y_Tanques[0] += 1
                X_Y_Tanques[1] += 1
                Aux += 1
                X_Y_Tanques[0] = contx

            while X_Y_Tanques[1] < conty+30:
                Define_color = contx
                while X_Y_Tanques[0] < contx+30:
                    while (Define_color+Aux) > contx:
                        mapa[X_Y_Tanques[1]][Define_color+Aux] = estado
                        mapa[X_Y_Tanques[1]][Define_color] = estado
                        Define_color -= 1
                    X_Y_Tanques[0] += 1
                X_Y_Tanques[1] += 1
                Aux -= 1
                X_Y_Tanques[0] = contx

            if X_Y_Tanques[2] > 700:
                X_Y_Tanques[0] = X_Y_Tanques[0]
                X_Y_Tanques[1] = X_Y_Tanques[1]
            

            
            y = X_Y_Tanques[1]
            x = X_Y_Tanques[0]
            Aux = 1
            Ver = False

            if y+30 >= ancho:
                Ver = True

            if Ver == False:
                while mapa[y+30][x] == 0:
                    y += 1
                    if y+30 > ancho:
                        Ver = True
                        break

            if Ver == False:
                contx = x
                conty = y
                while y < conty+15:
                    Define_color = contx
                    while x < contx+15:
                        while (Define_color+Aux) > contx:
                            mapa[y][Define_color+Aux] = 2
                            mapa[y][Define_color] = 2
                            Define_color -= 1
                        x += 1
                    y += 1
                    Aux += 1
                    x = contx
                while y < conty+30:
                    Define_color = contx
                    while x < contx+30:
                        while (Define_color+Aux) > contx:
                            mapa[y][Define_color+Aux] = 2
                            mapa[y][Define_color] = 2
                            Define_color -= 1
                        x += 1
                    y += 1
                    Aux -= 1
                    x = contx


                X_Y_Tanques[0] = x
                X_Y_Tanques[1] = y

                #Actualiza la pantalla
                Terreno.dibuja_mapa(Pant,mapa)
                pygame.display.update()
            
            #Si el tanque azul cae este pierde la partida
            else:
                vidaTank[1] = 0
                Terreno.dibuja_mapa(Pant,mapa)
                pygame.display.update()