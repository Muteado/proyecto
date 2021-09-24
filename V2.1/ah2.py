#hola
import pygame
import random

Celeste = (54,203,201)

largo= 1280
ancho= 600
pygame.init()
Verde = (44,177,26)

mapa = []


def main():

    pygame.init()
    Pant = pygame.display.set_mode([largo,ancho])
    pygame.display.set_caption("The Battle of the Tanks")


    iniciar_mapa()
    construir_terreno()
    construir_monta_iz()
    construir_monta_de()
    construir_crater_de()
    construir_crater_iz()


    #construir_monta_iz(base)

    dibui_mapa(Pant,mapa)
    

    salir=False

    #loop principal
    while salir!=True:
    
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir=True
        pygame.display.update()

    pygame.quit()

    
def dibui_terreno(Pant,x,y):
    
    pygame.draw.rect(Pant,Verde,(x,y,1,1))

def dibui_cielo(Pant,x,y):
    pygame.draw.rect(Pant,Celeste,(x,y,1,1))



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
#montana izquierda
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




#Crater izquierda


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
                            mapa[y][x+Aux_irregularidad+Disminuye_Derecha] = 0
                            mapa[y][x-Aux_irregularidad-Disminuye_Derecha] = 0
                            
                    if conty > 0:
                        if Aux_irregularidad == 0:
                            mapa[y][x+Aux_irregularidad+Disminuye_Derecha] = 0
                            mapa[y][x-Aux_irregularidad-Disminuye_Derecha] = 0

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
                            mapa[y][x+Aux_irregularidad+Disminuye_Derecha] = 0
                            mapa[y][x-Aux_irregularidad-Disminuye_Derecha] = 0
                            
                    if conty > 0:
                        if Aux_irregularidad == 0:
                            mapa[y][x+Aux_irregularidad+Disminuye_Derecha] = 0
                            mapa[y][x-Aux_irregularidad-Disminuye_Derecha] = 0

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



def dibui_mapa(Pant, base):

    x = 0
    y = 0
    holi=0

    while y < 600:
        while x < 1280:
            if base[y][x] == 0:
                dibui_cielo(Pant,x,y)
               
            elif base[y][x] == 1:
                dibui_terreno(Pant,x,y)
                
            x += 1
        x = 0
        y += 1

            
main()