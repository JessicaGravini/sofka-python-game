from jugador import Player


class Podio:  # Pista

    def __init__(self):
        self.primerLugar = None
        self.segundoLugar = None
        self.tercerLugar = None
        pass

    def asignarPrimerLugar(self, player):
        self.primerLugar = player

    def asignarSegundoLugar(self, player):
        self.segundoLugar = player

    def asignarTercerLugar(self, player):
        self.tercerLugar = player

    def obtenerPrimerLugar(self):
        return self.primerLugar

    def obtenerSegundoLugar(self):
        return self.segundoLugar

    def obtenerTercerLugar(self):
        return self.tercerLugar

    def jugadorYaPertenecePodio(self, player):
        return self.obtenerPrimerLugar() == player or self.obtenerSegundoLugar() == player or self.obtenerTercerLugar() == player
