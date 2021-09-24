import pygame
import random
from .Variables import Pant, Celeste, Verde, largo, ancho

Rojo = (255, 0, 0)
Azul = (0,0,255)
mapa = []


def main():

    iniciar_mapa()
    construir_terreno()
    construir_monta_iz()
    construir_monta_de()
    construir_crater_de()
    construir_crater_iz()
    hacer_Tanque_Rojo()
    hacer_Tanque_Azul()

    dibuja_mapa(Pant,mapa)



#dibuja lo que le corresponde por su numero puesto en dibuja_mapa
def dibuja_terreno(Pant,x,y):
    
    pygame.draw.rect(Pant,Verde,(x,y,1,1))

def dibuja_cielo(Pant,x,y):
    pygame.draw.rect(Pant,Celeste,(x,y,1,1))


##MOVER A TANQUES##
def dibujar_tanque_Rojo(Pant,x,y):
    pygame.draw.rect(Pant,Rojo,(x,y,1,1))

def dibujar_tanque_Azul(Pant,x,y):
    pygame.draw.rect(Pant,Azul,(x,y,1,1))
###################

#iniciar matriz
def iniciar_mapa():

    for iniciar in range(ancho):
        mapa.append([0]*largo)
    
    for i in range(ancho):
        for j in range(largo):
            mapa[i][j]=0

#Terreno
def construir_terreno():

    x = 0
    y = 450

    while y < 600:
        while x < 1280:
            mapa[y][x] = 1
            x += 1
        x = 0
        y += 1

#montana izquierda
def construir_monta_iz():
    x = random.randint(150,520)
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
def construir_monta_de():
    x = random.randint(720,1150)
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

def construir_crater_de():
    x = random.randint(700,1160)
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

def construir_crater_iz():
    x = random.randint(110,550)
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
    holi=0

    while y < 600:
        while x < 1280:
            if base[y][x] == 0:
                dibuja_cielo(Pant,x,y)
               
            elif base[y][x] == 1:
                dibuja_terreno(Pant,x,y)
            
            elif base[y][x] == 2:
                dibujar_tanque_Rojo(Pant,x,y)
            
            elif base[y][x] == 3:
                dibujar_tanque_Azul(Pant,x,y)

                
            x += 1
        x = 0
        y += 1




#define la posicion del tanque rojo
def hacer_Tanque_Rojo():
    x = random.randint(40,426)
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

#define la posicion del tanque azul
def hacer_Tanque_Azul():
    x = random.randint(800,1240)
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
      
main()


            




#def colision():

