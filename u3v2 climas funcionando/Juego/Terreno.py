import random
from .Variables import *
from .Tanques import *
from .Rectangulos import Rectangulos


class Terreno:
    #Funcion para crear el mapa
    def run(mapa):
        #Funciones para la construccion del terreno
        mapa=Terreno.iniciar_mapa(mapa)
        mapa=Terreno.Suelo(mapa)
        mapa=Terreno.irregularidad(mapa)

        #Posiciona los tanques
        Contador = 0
        Aux = random.randint(0,5)
        while Contador != jugadores[0]:

            if Contador > 0:
                Cont = 0
                while Cont < jugadores[0]:
                    if Aux == corroborar_conteo[0] or Aux == corroborar_conteo[1] or Aux == corroborar_conteo[2] or Aux == corroborar_conteo[3] or Aux == corroborar_conteo[4]:
                        Aux = random.randint(0,5)
                    else:
                        Cont += 1
                        break
            
            corroborar_conteo[Contador] = Aux
            if Contador == 0:
                jugador1.set_X(posiciones_X[Aux])
                Tanque.hacer_tanques(mapa,jugador1.get_X(),jugador1)
                Contador += 1
                print(posiciones_X[Aux],"en el caso de la 1")
            elif Contador == 1:
                jugador2.set_X(posiciones_X[Aux])
                Tanque.hacer_tanques(mapa,jugador2.get_X(),jugador2)
                Contador += 1
                print(posiciones_X[Aux],"en el caso de la 2")
            elif Contador == 2:
                jugador3.set_X(posiciones_X[Aux])
                Tanque.hacer_tanques(mapa,jugador3.get_X(),jugador3)
                print(posiciones_X[Aux],"en el caso de la 3")
                Contador += 1
            elif Contador == 3:
                jugador4.set_X(posiciones_X[Aux])
                Tanque.hacer_tanques(mapa,jugador4.get_X(),jugador4)
                print(posiciones_X[Aux],"en el caso de la 4")
                Contador += 1
            elif Contador ==4:
                jugador5.set_X(posiciones_X[Aux])
                Tanque.hacer_tanques(mapa,jugador5.get_X(),jugador5)
                print(posiciones_X[Aux],"en el caso de la 5")
                Contador += 1
            elif Contador ==5:
                jugador6.set_X(posiciones_X[Aux])
                Tanque.hacer_tanques(mapa,jugador6.get_X(),jugador6)
                print(posiciones_X[Aux],"en el caso de la 6")
                Contador += 1
            
        
        
        return mapa
        
    #Dibuja lo que le corresponde por su numero puesto en dibuja_mapa
    def dibuja_terreno(Pant,x,y):
        Rectangulos.dibujaRectangulos(Pant,Verde,(x,y,1,1),0)
    #Dibuja el cielo correspondiente
    def dibuja_cielo(Pant,x,y):
        Rectangulos.dibujaRectangulos(Pant,Celeste,(x,y,1,1),0)

    #iniciar matriz
    def iniciar_mapa(mapa):
        for iniciar in range(ancho[0]):
            mapa.append([0]*largo[0]) 
        for i in range(ancho[0]):
            for j in range(largo[0]):
                mapa[i][j]=0
        return mapa

    #Se crean las montañas y los cráteres numero
    def Suelo(mapa):

        i = 0
        #se divide el alto de la pantalla y se divide en 4 y al multiplicarlo por 3 se define la posicion desde donde partirá el terreno
        result = ((int(ancho[0]//4))*3)
        #se definen los puntos de las montanas y los crateres
        puntos = int(largo[0]//5)
        #se ven los puntos medios de cada montana y crater
        punto_medio = int(puntos//2)
        #se le da el valor del punto medio a una variable para así utilizarlo
        avance = punto_medio
        sube_baja = 100
        crater_monta = random.randint(1,2)
        contador_avance = 0
        Y_Original = result
        X_Original = i
        Y_altura = result
        contador = 0 

        contador_monta = 0
        contador_crater = 0
        
        while(i < largo[0]):
            
            #Si crater_monta es 1 se comienza a crear el crater
            if crater_monta == 1:
                #Se puede hacer un máximo de 2 crateres, por lo tanto se verifica el limite
                if contador_crater <2:
                   
                    #Se calcula la pendiente de la recta hacia abajo
                    pendiente_abajo = ((result+sube_baja) - Y_altura)//((i+punto_medio) - i)

                     #se traza la diagonal para bajar
                    while contador_avance <= avance:
                        #se calcula la Y con la formula de la recta, ya se conoce la pendiente y ahora se busca la Y
                        y = (((pendiente_abajo*i)-(pendiente_abajo*X_Original))+Y_Original)
                        #Se utiliza un ciclo para poder rellenar todo el terreno debajo del punto seleccionado
                        Y_altura = y
                        while y < ancho[0]:
                            #si la y es menor al ancho[0] se pinta en el mapa/matriz
                            if (0 < y < ancho[0]) and (0 < i < largo[0]):
                                mapa[y][i] = 1
                            y += 1

                        contador_avance += 1
                        i += 1
                    #al terminar de hacer un lado del crater se valida que el contador de avance fue mayor o igual al avance
                    if contador_avance >= avance:
                        #se le suma la distancia que debe avanzar ahora el avance 
                        avance += punto_medio

                    #Se calcula la pendiente de la recta hacia arriba
                    pendiente_arriba = (result - Y_altura)//((i+punto_medio) - i)
                    #X_Original pasa a valer i que será la nueva x que se utilizará en la formula
                    X_Original = i
                    
                    

                    #se traza la diagonal para subir
                    while contador_avance <= avance:
                        #se calcula la Y con la formula de la recta, ya se conoce la pendiente y ahora se busca la Y
                        y = (pendiente_arriba*i)-(pendiente_arriba*X_Original)+(Y_Original)
                        #Se utiliza un ciclo para poder rellenar todo el terreno debajo del punto seleccionado
                        Y_altura = y
                        while y < ancho[0]:
                            #si la y es menor al ancho[0] se pinta en el mapa/matriz
                            if (0 < y < ancho[0]) and (0 < i < largo[0]):
                                mapa[y][i] = 1
                            y += 1

                        contador_avance += 1
                        i += 1
                        #al terminar de hacer el crater se valida si i es mayor o igual a 800


                    #al terminar de hacer un lado del crater se valida que el contador de avance fue mayor o igual al avance
                    if contador_avance >= avance:
                        #se le suma la distancia que debe avanzar ahora el avance 
                        avance += punto_medio

                    #se tira un random para ver si se hará una montana o un crater
                    crater_monta = random.randint(1,2)
                    contador += 1
                    contador_crater += 1
                    #X_Original pasa a valer i que será la nueva x que se utilizará en la formula
                    X_Original = i

                else:
                    crater_monta = random.randint(1,2)



            #Si crater_monta es 2 se comienza a crear la montana
            elif crater_monta == 2:
                #Se puede hacer un máximo de 3 montanas, por lo tanto se verifica el limite
                if contador_monta < 3:
                    #Se calcula la pendiente de la recta hacia arriba
                    pendiente_arriba = ((result-sube_baja) - Y_altura)//((i+punto_medio) - i)
                    
                    while contador_avance <= avance:
                        #se calcula la Y con la formula de la recta, ya se conoce la pendiente y ahora se busca la Y
                        y = (pendiente_arriba*i)-(pendiente_arriba*X_Original)+(Y_Original)
                        Y_altura = y
                        #Se utiliza un ciclo para poder rellenar todo el terreno debajo del punto seleccionado
                        while y < ancho[0]:
                            #si la y es menor al ancho[0] se pinta en el mapa/matriz
                            if (0 < y < ancho[0]) and (0 < i < largo[0]):
                                mapa[y][i] = 1
                            y += 1

                        contador_avance += 1
                        i += 1

                    #al terminar de hacer un lado de la montana se valida que el contador de avance fue mayor o igual al avance
                    if contador_avance >= avance:
                        #se le suma la distancia que debe avanzar ahora el avance 
                        avance += punto_medio


                    #Se calcula la pendiente de la recta hacia abajo
                    pendiente_abajo = (result - Y_altura)//((i+punto_medio) - i)
                    #X_Original pasa a valer i que será la nueva x que se utilizará en la formula
                    X_Original = i
                    
                    
                    while contador_avance <= avance:
                        #se calcula la Y con la formula de la recta, ya se conoce la pendiente y ahora se busca la Y
                        y = (pendiente_abajo*i)-(pendiente_abajo*X_Original)+(Y_Original)
                        Y_altura = y
                        #Se utiliza un ciclo para poder rellenar todo el terreno debajo del punto seleccionado
                        while y < ancho[0]:
                            #si la y es menor al ancho[0] se pinta en el mapa/matriz
                            if (0 < y < ancho[0]) and (0 < i < largo[0]):
                                mapa[y][i] = 1
                            y += 1

                        contador_avance += 1
                        i += 1
                        #al terminar de hacer el crater se valida si i es mayor o igual a 800

                    
                    #al terminar de hacer un lado de la montana se valida que el contador de avance fue mayor o igual al avance
                    if contador_avance >= avance:
                        #se le suma la distancia que debe avanzar ahora el avance 
                        avance += punto_medio

                    #se tira un random para ver si se hará una montana o un crater
                    crater_monta = random.randint(1,2)
                    contador += 1
                    contador_monta += 1
                    #X_Original pasa a valer i que será la nueva x que se utilizará en la formula
                    X_Original = i
                else:
                    crater_monta = random.randint(1,2)
            

            #el contador valida si se hicieron 3 montanas y 2 crateres en total, de ser así se hace un return del mapa
            if contador==5:
                i=largo[0]
                return mapa


    #se crea la irregularidad del terreno
    def irregularidad(mapa):
        
        x = 0
        y = 0
        #Es el random que se genera parahacer los relieves del terreno
        irregu = random.randint(1,2)
        #Se recorre la parte Y de la matriz
        while y < ancho[0]-1:
            #Se recorre la matriz en la parte X
            while x < largo[0]-2:
                #Se corrobora que el punto que se está viendo es tierra y el que está a la derecha es cielo
                if (mapa[y][x] == 1 and mapa[y][x+1] == 0):
                    #Se crea una variable para que se vaya avanzando en la matriz
                    avance = 0
                    #Es el while que "embellece" el terreno, para que se vea bien con los relieves y las irregularidades
                    while True:
                        #se ve que la x más en contador de avance sea menor que el tamano de la pantana, para que no se salga de la matriz
                        if x+avance < largo[0]:
                            #Si el punto de arriba es 1 significando que es terreno
                            if mapa[y-1][x+avance] == 1:
                                #como se cumplio la condicion ahora se combierte el punto de abajo en terreno
                                mapa[y][x+avance] = 1
                                avance += 1
                            #si no se cumple se le suma solamente al avance
                            else:
                                avance += 1
                        #si al sumarle avance a x es mayor que la pantana se sale directamente del while
                        else:
                            break
                
                #Se corrobora que el punto que se está viendo es tierra y el que está a la izquierda es cielo
                if (mapa[y][x] == 1 and mapa[y][x-1] == 0):
                    #Aquí se realiza lo mismo que en el if de arriba, pero con la diferencia de los lados a los cuales se ven y agregan
                    avance = 0
                    #Es el while que "embellece" el terreno, para que se vea bien con los relieves y las irregularidades
                    while True:
                        if x+avance < largo[0]:
                            if mapa[y-1][x-avance] == 1:
                                mapa[y][x-avance] = 1
                                avance += 1
                            else:
                                avance += 1
                        else:
                            break
                
                #este if ve los puntos de la derecha de las montanas o crateres
                if (mapa[y][x] == 1 and mapa[y][x+1] == 0):
                    #si el random es 1 se quita terreno hacia la izquierda
                    if irregu == 1:
                        mapa[y][x] = 0
                        mapa[y][x-1] = 0
                    #si el random es 2 se agrega terreno a la derecha
                    elif irregu == 2:
                        mapa[y][x] = 1
                        mapa[y][x+1] = 1
                    irregu = random.randint(1,2)

                #en la primero parte se ven los puntos de la izquierda de las montanas o crateres y en la segunda parte del or se ven las zonas planas
                elif (mapa[y][x] == 1 and mapa[y][x-1] == 0) or (mapa[y][x] == 1 and mapa[y][x-1] == 1 and mapa[y][x+1] == 1 and mapa[y-1][x] == 0):
                    #si el random es 1 se quita terreno hacia la derecha
                    if irregu == 1:
                        mapa[y][x] = 0
                        mapa[y][x+1] = 0
                    #si el random es 2 se agrega terreno a la izquierda
                    elif irregu == 2:
                        mapa[y][x] = 1
                        mapa[y][x-1] = 1
                    irregu = random.randint(1,2)

                x += 1
            x = 0
            y += 1
        return(mapa)

    #Dibuja el mapa pintando con los colores
    def dibuja_mapa(Pant, base):
        x = 0
        y = 0
        while y < ancho[0]:
            while x < largo[0]:
                if base[y][x] == 0:
                    Terreno.dibuja_cielo(Pant,x,y)  
                elif base[y][x] == 1:
                    Terreno.dibuja_terreno(Pant,x,y)
                elif base[y][x] == jugador1.color:
                    Tanque.dibuja_tanques(Pant,jugador1.color,x,y)
                elif base[y][x] == jugador2.color:
                    Tanque.dibuja_tanques(Pant,jugador2.color,x,y)
                elif base[y][x] == jugador3.color:
                    Tanque.dibuja_tanques(Pant,jugador3.color,x,y)
                elif base[y][x] == jugador4.color:
                    Tanque.dibuja_tanques(Pant,jugador4.color,x,y)
                elif base[y][x] == jugador5.color:
                    Tanque.dibuja_tanques(Pant,jugador5.color,x,y)
                elif base[y][x] == jugador6.color:
                    Tanque.dibuja_tanques(Pant,jugador6.color,x,y)
                x += 1
            x = 0
            y += 1