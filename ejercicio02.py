"""

Desarrolla el juego de piedra papel o tijera. El programa debe permitir al usuario jugar
contra la computadora, que seleccionará su jugada de manera aleatoria. El programa
debe anunciar al ganador de cada ronda. (5pts)

"""

import random

def eleccion_computadora(opciones):
    turno_computadora = random.choice(opciones)
    return turno_computadora

def Jugar(turno_jugador,turno_computadora):
    ganador = ""
    if turno_computadora == turno_jugador:
        ganador = "Empate"
    elif (turno_jugador == "Papel" and turno_computadora == "Piedra") or (turno_jugador == "Piedra" and turno_computadora == "Tijera") or (turno_jugador == "Tijera" and turno_computadora == "Papel"):
        ganador = "Jugador"
    else:
        ganador = "Computadora"
    return ganador
    
def eleccion_ganador(ganador):
    if ganador == "Empate":
        print(f"-- Es un Empate ! --")
    elif ganador == "Jugador":
        print(f"-- Felicidades Ganaste la ronda ! --")
    else:
        print(f"-- Esta partida la gana la Computadora --")
        

condicion = True
while condicion:
    
    print("\n--Bienvenido a mi Juego de Piedra, papel o tijera--")
    print("1. Jugar\n2. Salir")
    seleccion = int(input("Ingresa tu eleccion: "))
    opciones = ("Piedra","Papel","Tijera")
    
    if seleccion == 1:
        print("\n----- JUGANDO -----")
        print("1. Piedra\n2. Papel\n3. Tijera")
        eleccion_jugador = int(input("Ingresa tu eleccion: "))
        
        if eleccion_jugador not in range(1,4):
            print("Ingresa una eleccion valida.")
            continue
        
        turno_jugador = opciones[eleccion_jugador-1]
        turno_computadora = eleccion_computadora(opciones)
        
        ganador = Jugar(turno_jugador,turno_computadora)
        
        print(f"\n*** Computadora: {turno_computadora} vs Jugador: {turno_jugador} *** ")
        
        eleccion_ganador(ganador)
        
    elif seleccion == 2:
        print("Saliendo del Programa...")
        condicion = False
    else:
        print("Opcion invalida, Intenta de nuevo.")
        
        
        
        