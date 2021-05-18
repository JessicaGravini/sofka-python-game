from podio import Podio
from jugador import Player
from car import Car
from game import Game

nroJugadores = 0
lstJugadores = list()
lstJuegos = list()

def solicitarNroJugadores():
    while True:
        try:
            nroJugadores = int(input(f"Bienvenido, para empezar ¿Cuantos jugadores desea (minimo 3)? "))
            if(nroJugadores >= 3):
                return nroJugadores
            else:
                print("El minimo de jugadores debe ser 3")
                continue
        except ValueError:
            print("El numero de jugadores debe ser un valor entero")
            continue

def solicitarNombreJugadores():
    for contador in range(0, nroJugadores):
        jugadorActualNombre = input("Ingrese el nombre del jugador numero " + str(contador + 1) + "\n")
        player = Player(jugadorActualNombre)
        lstJugadores.append(player)

def iniciarJuego():
    deseaIniciarJuego = input("Desea iniciar un juego nuevo? (y/n) ")
    if(deseaIniciarJuego == 'y'):
        print("La lista de juegos disponibles es la siguiente (ingrese el número asociado para continuar): ")
        for contador in range(0, len(lstJuegos)):
            print(f"{contador}. {lstJuegos[contador].nombre}")
        juegoSeleccionado = int(input("Deseo seleccionar el juego número: "))
        juego = lstJuegos[juegoSeleccionado]
        pista = juego.obtenerPista()
        calcularPodios(juego, pista)

def calcularPodios(game, pista):
    print("*************************************************")
    print("Bienvenidos, se dará inicio a la carrera!")
    print(f"Se ha preparado la pista que tendrá una distancia de {pista.kilometros} kilometros y {pista.nroCarriles} carriles")

    carrilesEnJuego = game.obtenerCarriles()
    podio = Podio()

    while podio.obtenerPrimerLugar() == None or podio.obtenerSegundoLugar() == None or podio.obtenerTercerLugar() == None:
        for carril in carrilesEnJuego:
            if(podio.jugadorYaPertenecePodio(carril.carro.player) == False):
                metrosObtenidos = carril.carro.player.lanzarDados()
                carril.avanzarDistancia(metrosObtenidos)
                if(carril.desplazamientoFinal):
                    if(podio.obtenerPrimerLugar() == None):
                        podio.asignarPrimerLugar(carril.carro.player)
                    elif(podio.obtenerSegundoLugar() == None):
                        podio.asignarSegundoLugar(carril.carro.player)
                    elif(podio.obtenerTercerLugar() == None):
                        podio.asignarTercerLugar(carril.carro.player)
            else:
                pass

    primerLugar = podio.obtenerPrimerLugar()
    segundoLugar = podio.obtenerSegundoLugar()
    tercerLugar = podio.obtenerTercerLugar()

    print("******** Podio **********")
    print(f"El ganador del primer lugar es {primerLugar.nombre}")
    print(f"El ganador del segundo lugar es {segundoLugar.nombre}")
    print(f"El ganador del tercer lugar es {tercerLugar.nombre}")
    iniciarJuego()

def crearJuego():
    global nroJugadores
    global lstJugadores
    if(nroJugadores == 0):
        nroJugadores = solicitarNroJugadores()
        solicitarNombreJugadores()
    
    game = Game(input("Para continuar, ingrese el nombre de su juego: "))
    for jugador in lstJugadores:
        car = Car(jugador)
        game.addCarToGame(car)
    game.crearPista()
    game.asignarCarrosACarriles()
    lstJuegos.append(game)

    while True:
        respuestaCrearNuevoJuego = input("Desea crear un juego nuevo? (y/n) ")
        if respuestaCrearNuevoJuego != 'y' and respuestaCrearNuevoJuego != 'n':
            print("Debe ingresar 'y' o 'n' para continuar")
            continue
        elif respuestaCrearNuevoJuego == 'y':
            crearJuego()
            break
        elif respuestaCrearNuevoJuego == 'n':
            iniciarJuego()
            break

crearJuego()