from baraja import *
from logica import *

def pedir() -> bool:
    decision = ''
    while decision not in ['H','S']:
        decision = input("H | S\n").upper()
    return True if decision == 'H' else False

def turno_jugador(jugador) -> list:
    cartas, nombre = jugador
    print(nombre)
    mostrar_cartas(cartas)
    if obtener_valor_cartas(cartas) == 21: return jugador
    while True:
        if pedir():
            cartas.append(baraja.pop())
            mostrar_cartas(cartas)
            if obtener_valor_cartas(cartas) >= 21:
                print("Te pasate. Perdiste")
                return [cartas, nombre]
        else:
            return [cartas, nombre]