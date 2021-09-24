from Juego.ClassEsquinas import DatosEsquinas
from Juego.claseTanques import Tanque
import pygame
import random
from .Variables import Pant, Celeste, Verde,Azul,Rojo, largo, ancho, cmi, cmd, ccd, cci, XdeTankA,XdeTankR
from .ClassRectangulos import Rectangulos

class Terreno:
    
    def run(mapa):

        mapa=Terreno.iniciar_mapa(mapa)
        mapa=Terreno.construir_terreno(mapa)
        Terreno.construir_monta_iz(mapa,cmi)
        Terreno.construir_monta_de(mapa,cmd)
        Terreno.construir_crater_de(mapa,ccd)
        Terreno.construir_crater_iz(mapa,cci)
        Tanque.hacer_tanques(mapa,XdeTankA,2)
        Tanque.hacer_tanques(mapa,XdeTankR,3)
        return mapa
        
    #dibuja lo que le corresponde por su numero puesto en dibuja_mapa
    def dibuja_terreno(Pant,x,y):
        Rectangulos.dibujaRectangulos(Pant,Verde,(x,y,1,1),0)

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

    #Terreno
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

    #montana izquierda
    def construir_monta_iz(mapa,x):
        y = 250
        cont = x
        conty = 0
        conta = 0
        Aumenta_Derecha = 0
        Aux = 0
        while y < 451:
            Aux_irregularidad = conty
            Define_sueloX = cont
            while x < cont+200:
                if Aumenta_Derecha == 0 and x == cont:
                    mapa[y][x] = 1
                elif conty == conta:
                    #pinta interior montana
                    while (Define_sueloX+Aumenta_Derecha) > cont:
                        mapa[y][Define_sueloX+Aumenta_Derecha] = 1
                        mapa[y][Define_sueloX] = 1
                        Define_sueloX -= 1 
                        #Aumenta_Derecha += 1
                    #pinta irregularidad montana
                    while Aux_irregularidad > 0 or Aux_irregularidad < 0:
                        if conty < 0 and conta < 0:
                            mapa[y][x+Aux_irregularidad+Aumenta_Derecha] = 0
                            mapa[y][x-Aux_irregularidad-Aumenta_Derecha] = 0    
                        else:
                            mapa[y][x+Aux_irregularidad+Aumenta_Derecha] = 1
                            mapa[y][x-Aux_irregularidad-Aumenta_Derecha] = 1
                        if Aux_irregularidad > 0:
                            Aux_irregularidad -= 1
                        if Aux_irregularidad < 0:
                            Aux_irregularidad += 1
                        if conty < 0:    
                            if Aux_irregularidad == 0:
                                mapa[y][x+Aux_irregularidad+Aumenta_Derecha] = 0
                                mapa[y][x-Aux_irregularidad-Aumenta_Derecha] = 0          
                        if conty > 0:
                            if Aux_irregularidad == 0:
                                mapa[y][x+Aux_irregularidad+Aumenta_Derecha] = 1
                                mapa[y][x-Aux_irregularidad-Aumenta_Derecha] = 1
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
            #se le suma a la variable Aumenta_Derecha
            if y % 2 == 0:
                Aumenta_Derecha += 1

    #Montana derecha
    def construir_monta_de(mapa,x):
        y = 250
        cont = x
        conty = 0
        conta = 0
        Aumenta_Derecha = 0
        Aux = 0
        while y < 451:
            Aux_irregularidad = conty
            Define_sueloX = cont
            while x < cont+200:
                if Aumenta_Derecha == 0 and x == cont:
                    mapa[y][x] = 1
                elif conty == conta:
                    #pinta interior montana
                    while (Define_sueloX+Aumenta_Derecha) > cont:
                        mapa[y][Define_sueloX+Aumenta_Derecha] = 1
                        mapa[y][Define_sueloX] = 1
                        Define_sueloX -= 1
                        #Aumenta_Derecha += 1
                    #pinta irregularidad montana
                    while Aux_irregularidad > 0 or Aux_irregularidad < 0:
                        if conty < 0 and conta < 0:
                            mapa[y][x+Aux_irregularidad+Aumenta_Derecha] = 0
                            mapa[y][x-Aux_irregularidad-Aumenta_Derecha] = 0   
                        else:
                            mapa[y][x+Aux_irregularidad+Aumenta_Derecha] = 1
                            mapa[y][x-Aux_irregularidad-Aumenta_Derecha] = 1    
                        if Aux_irregularidad > 0:
                            Aux_irregularidad -= 1
                        if Aux_irregularidad < 0:
                            Aux_irregularidad += 1
                        if conty < 0:    
                            if Aux_irregularidad == 0:
                                mapa[y][x+Aux_irregularidad+Aumenta_Derecha] = 0
                                mapa[y][x-Aux_irregularidad-Aumenta_Derecha] = 0       
                        if conty > 0:
                            if Aux_irregularidad == 0:
                                mapa[y][x+Aux_irregularidad+Aumenta_Derecha] = 1
                                mapa[y][x-Aux_irregularidad-Aumenta_Derecha] = 1
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
            #se le suma a la variable Aumenta_Derecha
            if y % 2 == 0:
                Aumenta_Derecha += 1

    #Crater derecho
    def construir_crater_de(mapa,x):
        y = 450
        if mapa[y-2][x] == 1 or mapa[y-2][x+100] == 1 or mapa[y-2][x-100] == 1:
            while mapa[y-1][x] == 1 or mapa[y-1][x+100] == 1 or mapa[y-1][x-100] == 1:
                x = random.randint(700,1150)
        cont = x
        conty = 0
        conta = 0
        Disminuye_Derecha = 100
        Aux = 0
        while y < 530:
            Aux_irregularidad = conty
            Define_sueloX = cont
            while x < cont+100:
                if Disminuye_Derecha == -1 and x == cont:
                    mapa[y][x] = 1
                elif conty == conta:
                    #pinta interior montana
                    while (Define_sueloX+Disminuye_Derecha) > cont:
                        mapa[y][Define_sueloX+Disminuye_Derecha] = 0
                        mapa[y][Define_sueloX] = 0
                        Define_sueloX -= 1
                        #print("hola")
                        #Aumenta_Derecha += 1
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
            #se le suma a la variable Aumenta_Derecha
            Disminuye_Derecha -= 1

    #Crater izquierda
    def construir_crater_iz(mapa,x):
        y = 450
        if mapa[y-2][x] == 1 or mapa[y-2][x+100] == 1 or mapa[y-2][x-100] == 1:
            while mapa[y-1][x] == 1 or mapa[y-1][x+100] == 1 or mapa[y-1][x-100] == 1:
                x = random.randint(110,550)
        cont = x
        conty = 0
        conta = 0
        Disminuye_Derecha = 100
        Aux = 0
        while y < 530:
            Aux_irregularidad = conty
            Define_sueloX = cont
            while x < cont+100:
                if Disminuye_Derecha == -1 and x == cont:
                    mapa[y][x] = 1
                elif conty == conta:
                    #pinta interior montana
                    while (Define_sueloX+Disminuye_Derecha) > cont:
                        mapa[y][Define_sueloX+Disminuye_Derecha] = 0
                        mapa[y][Define_sueloX] = 0
                        Define_sueloX -= 1
                        #print("hola")
                        #Aumenta_Derecha += 1
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
            #se le suma a la variable Aumenta_Derecha
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
                    Tanque.dibuja_tanques(Pant,Azul,x,y)
                elif base[y][x] == 3:
                    Tanque.dibuja_tanques(Pant,Rojo,x,y)    
                x += 1
            x = 0
            y += 1
        DatosEsquinas.generarBloques(posIniX,posIniY,largoBloq,altoBloq)