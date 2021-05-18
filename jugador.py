import random


class Player:

    def __init__(self, nombre):
        self.nombre = nombre
      
    def lanzarDados(self):
        metros = random.randint(1,6) * 100
        return metros
        
    
    




