from math import *


class Parabolico:
    def calculofuturo(β, vi):
        om=((β*pi)/180) #Angulo de disparo multiplicado por pi y dividido en 180 que es el angulo de disparo
        #g=9.81 # m/s**2 #gravedad de la tierra
        a=tan(om) #tangente del angulo ingresado
        b=((9.81)/((2*vi**2)*cos(om)**2)) #formula que usa la gravedad, velocidad inicial ingresada y el angulo de inicio que ingresamos
        ymax=(vi**2)*(sin(om)*sin(om))/(2*9.81) # el movimiento que hace la bala, esto marca el punto maximo que alcanza el disparo
        xmax=(vi**2)*(sin(2*om))//(9.81) # La distancia maxima que hace la bala al usar la velocidad y el angulo inicial
        tmax=(vi*sin(om))/(9.81) # tiempo que tarda la bala en llegar al punto mas alto
        tv=2*(tmax)
        return xmax