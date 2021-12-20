from random import randint as r
class Tanque:
    def __init__(self, balas):
        self.vida = 100
        self.cantBalas = balas

    #Cambia la vida  
    def set_Vida (self, vidaNew):
        self.vida = self.vida-vidaNew
    
    def get_Vida (self):
        return self.vida
    def get_Balas (self):
        return self.cantBalas
      
tanque1 = Tanque(100)
print("Getter: ",tanque1.get_Vida())
tanque1.set_Vida(50)
print("Getter: ",tanque1.get_Vida())
print("Getter: ",tanque1.get_Balas())

tanque1 = Tanque(50)
print("Getter: ",tanque1.get_Balas())
print("Getter: ",tanque1.get_Vida())