import random
from .Tanques import Tanque
from .Rectangulos import Rectangulos
from .Variables import *

class Terreno:
    #Funcion para crear el mapa
    def run(mapa):
        #Funciones para la construccion del terreno
        mapa=Terreno.iniciar_mapa(mapa)
        mapa=Terreno.construir_terreno(mapa)

        #Variables auxiliares
        contador = 0
        Cont_Monta = 0
        Cont_Crater = 0
        Pocisiones = 150

        #Genera las posiciones de las montañas y los cañones
        while contador < 5:
            variante = random.randint(1,2)
            if variante == 1:
                if Cont_Monta < 3:
                    Terreno.construir_monta(mapa,Pocisiones)
                    Cont_Monta += 1
                    contador += 1
                    Pocisiones += 230
            if variante == 2:
                if Cont_Crater < 2:
                    Terreno.construir_crater(mapa,Pocisiones)
                    Cont_Crater += 1
                    contador += 1
                    Pocisiones += 230

        #Posiciona los tanques
        XdelTank[0] = random.randint(40,426)
        XdelTank[1] = random.randint(800,1240)
        Tanque.hacer_tanques(mapa,XdelTank[0],2)
        Tanque.hacer_tanques(mapa,XdelTank[1],3)
        return mapa
        
    #Dibuja lo que le corresponde por su numero puesto en dibuja_mapa
    def dibuja_terreno(Pant,x,y):
        Rectangulos.dibujaRectangulos(Pant,Verde,(x,y,1,1),0)
    #Dibuja el cielo correspondiente
    def dibuja_cielo(Pant,x,y):
        Rectangulos.dibujaRectangulos(Pant,Celeste,(x,y,1,1),0)

    #iniciar matriz
    def iniciar_mapa(mapa):
        for iniciar in range(ancho):
            mapa.append([0]*largo) 
        for i in range(ancho):
            for j in range(largo):
                mapa[i][j]=0
        return mapa

    #Genera el terreno
    def construir_terreno(mapa):
        x = 0
        y = 450
        while y < 600:
            while x < 1280:
                mapa[y][x] = 1
                x += 1
            x = 0
            y += 1
        return mapa

    #Genera montañas
    def construir_monta(mapa,x):
        y = 230
        cont = x
        conty = 0
        conta = 0
        Aumenta = 0
        Aux = 0
        if mapa[448][cont+80] == 1 or mapa[448][cont-80] == 1 or mapa[448][cont] == 1 or mapa[451][cont-80] == 0:
            while mapa[448][cont+80] == 1 or mapa[448][cont-80] == 1 or mapa[448][cont] == 1:
                cont = cont + 1
            
        while y < 451:
            Aux_irregularidad = conty
            Define_sueloX = cont
            while x < cont+230:
                if Aumenta == 0 and x == cont:
                    mapa[y][x] = 1
                elif conty == conta:
                    #pinta interior montana
                    while (Define_sueloX+Aumenta) > cont:
                        mapa[y][Define_sueloX+Aumenta] = 1
                        mapa[y][Define_sueloX] = 1
                        Define_sueloX -= 1 
                        #Aumenta += 1
                    #pinta irregularidad montana
                    while Aux_irregularidad > 0 or Aux_irregularidad < 0:
                        if conty < 0 and conta < 0:
                            mapa[y][x+Aux_irregularidad+Aumenta] = 0
                            mapa[y][x-Aux_irregularidad-Aumenta] = 0    
                        else:
                            mapa[y][x+Aux_irregularidad+Aumenta] = 1
                            mapa[y][x-Aux_irregularidad-Aumenta] = 1
                        if Aux_irregularidad > 0:
                            Aux_irregularidad -= 1
                        if Aux_irregularidad < 0:
                            Aux_irregularidad += 1
                        if conty < 0:    
                            if Aux_irregularidad == 0:
                                mapa[y][x+Aux_irregularidad+Aumenta] = 0
                                mapa[y][x-Aux_irregularidad-Aumenta] = 0          
                        if conty > 0:
                            if Aux_irregularidad == 0:
                                mapa[y][x+Aux_irregularidad+Aumenta] = 1
                                mapa[y][x-Aux_irregularidad-Aumenta] = 1
                x += 1
            i=0
            #Se crea el random para generar el azar del terreno
            if Aux < 5:
                if Aux > 3:
                    conty += 0
                    conta += 0
                else:
                    conty += 1
                    conta += 1
                Aux += 1
            else:
                while i == 0:
                    j = random.randint(0,2)
                    if j == 0:
                        conty += 0
                        conta += 0
                        i += 1
                    elif j == 1:
                        conty += 1
                        conta += 1
                        i += 1
                    elif j == 2:
                        conty -= 1
                        conta -= 1
                        i += 1
            x = cont
            y += 1
            #se le suma a la variable Aumenta
            if y % 2 == 0:
                Aumenta += 1


    #Genera cañones
    def construir_crater(mapa,x):
        y = 450
        if mapa[y-2][x] == 1 or mapa[y-2][x+80] == 1 or mapa[y-2][x-80] == 1 or mapa[y+2][x] == 0:
            while mapa[y-1][x] == 1 or mapa[y-1][x+80] == 1 or mapa[y-1][x-80] == 1 or mapa[y+2][x] == 0:
                x = x + 1
        cont = x
        conty = 0
        conta = 0
        Disminuye_Derecha = 100
        Aux = 0
        while y < 530:
            Aux_irregularidad = conty
            Define_sueloX = cont
            while x < cont+10:
                if Disminuye_Derecha == -1 and x == cont:
                    mapa[y][x] = 1
                elif conty == conta:
                    #pinta interior montana
                    while (Define_sueloX+Disminuye_Derecha) > cont:
                        mapa[y][Define_sueloX+Disminuye_Derecha] = 0
                        mapa[y][Define_sueloX] = 0
                        Define_sueloX -= 1
                        #print("hola")
                        #Aumenta += 1
                    #pinta irregularidad montana
                    while Aux_irregularidad > 0 or Aux_irregularidad < 0:
                        if conty < 0 and conta < 0:
                            mapa[y][x+Aux_irregularidad+Disminuye_Derecha] = 1
                            mapa[y][x-Aux_irregularidad-Disminuye_Derecha] = 1     
                        else:
                            mapa[y][x+Aux_irregularidad+Disminuye_Derecha] = 0
                            mapa[y][x-Aux_irregularidad-Disminuye_Derecha] = 0    
                        if Aux_irregularidad > 0:
                            Aux_irregularidad -= 1
                        if Aux_irregularidad < 0:
                            Aux_irregularidad += 1
                        if conty < 0:    
                            if Aux_irregularidad == 0:
                                if mapa[y][x+Aux_irregularidad+Disminuye_Derecha+1] == 0:
                                    mapa[y][x+Aux_irregularidad+Disminuye_Derecha] = 0
                                    mapa[y][x-Aux_irregularidad-Disminuye_Derecha] = 0
                                if mapa[y][x+Aux_irregularidad+Disminuye_Derecha-1] == 0:
                                    mapa[y][x+Aux_irregularidad+Disminuye_Derecha] = 0
                                    mapa[y][x-Aux_irregularidad-Disminuye_Derecha] = 0
                                if mapa[y][x+Aux_irregularidad+Disminuye_Derecha+1] == 1:
                                    mapa[y][x+Aux_irregularidad+Disminuye_Derecha] = 1
                                    mapa[y][x-Aux_irregularidad-Disminuye_Derecha] = 1    
                                if mapa[y][x+Aux_irregularidad+Disminuye_Derecha-1] == 1:
                                    mapa[y][x+Aux_irregularidad+Disminuye_Derecha] = 1
                                    mapa[y][x-Aux_irregularidad-Disminuye_Derecha] = 1       
                        if conty > 0:
                            if Aux_irregularidad == 0:
                                if mapa[y][x+Aux_irregularidad+Disminuye_Derecha+1] == 0:
                                    mapa[y][x+Aux_irregularidad+Disminuye_Derecha] = 0
                                    mapa[y][x-Aux_irregularidad-Disminuye_Derecha] = 0
                                if mapa[y][x+Aux_irregularidad+Disminuye_Derecha-1] == 0:
                                    mapa[y][x+Aux_irregularidad+Disminuye_Derecha] = 0
                                    mapa[y][x-Aux_irregularidad-Disminuye_Derecha] = 0
                                if mapa[y][x+Aux_irregularidad+Disminuye_Derecha+1] == 1:
                                    mapa[y][x+Aux_irregularidad+Disminuye_Derecha] = 1
                                    mapa[y][x-Aux_irregularidad-Disminuye_Derecha] = 1  
                                if mapa[y][x+Aux_irregularidad+Disminuye_Derecha-1] == 1:
                                    mapa[y][x+Aux_irregularidad+Disminuye_Derecha] = 1
                                    mapa[y][x-Aux_irregularidad-Disminuye_Derecha] = 1
                x += 1
            i=0
            #Se crea el random para generar el azar del terreno
            if Aux < 5:
                if Aux > 3:
                    conty += 0
                    conta += 0
                else:
                    conty += 1
                    conta += 1
                Aux += 1
            else:
                while i == 0:
                    j = random.randint(0,2)
                    if j == 0:
                        conty += 0
                        conta += 0
                        i += 1
                    elif j == 1:
                        conty += 1
                        conta += 1
                        i += 1
                    elif j == 2:
                        conty -= 1
                        conta -= 1
                        i += 1
            x = cont
            y += 1
            #se le suma a la variable Aumenta
            Disminuye_Derecha -= 1


    #Dibuja el mapa pintando con los colores
    def dibuja_mapa(Pant, base):
        x = 0
        y = 0
        posIniX=0
        posIniY=0
        largoBloq = 200
        altoBloq = 20
        while y < 600:
            while x < 1280:
                if base[y][x] == 0:
                    Terreno.dibuja_cielo(Pant,x,y)  
                elif base[y][x] == 1:
                    Terreno.dibuja_terreno(Pant,x,y)
                elif base[y][x] == 2:
                    Tanque.dibuja_tanques(Pant,color,x,y)
                elif base[y][x] == 3:
                    Tanque.dibuja_tanques(Pant,color2,x,y)    
                x += 1
            x = 0
            y += 1
        