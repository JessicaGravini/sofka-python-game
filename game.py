from carril import Carril
import random
from track import Track


class Game:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.cars = []
        self.pista = {}
        self.carriles = []
        pass

    def addCarToGame(self, car):
        self.cars.append(car)

    def crearPista(self):
        kilometrosRandom = random.randint(1, 100)
        pista = Track(kilometrosRandom, len(self.cars))
        self.pista = pista
        return pista

    def obtenerPista(self):
        return self.pista

    def asignarCarrosACarriles(self):
        for car in self.cars:
            kilometrosAMetros = self.pista.kilometros * 1000
            carril = Carril(car, kilometrosAMetros, False, 0)
            self.carriles.append(carril)

    def obtenerCarros(self):
        return self.cars

    def obtenerCarriles(self):
        return self.carriles
