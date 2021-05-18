class Carril:
    def __init__(self, carro, metrosTotal, desplazamientoFinal, metrosRecorridos):
        self.carro = carro
        self.metrosTotal = metrosTotal
        self.metrosRecorridos = metrosRecorridos 
        self.desplazamientoFinal = desplazamientoFinal
        pass

    
    def avanzarDistancia(self, metros):
        self.metrosRecorridos += metros
        if(self.metrosRecorridos>=self.metrosTotal):
            self.desplazamientoFinal = True


