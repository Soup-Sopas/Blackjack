import time
import random
from baraja import *
from logica import *

def mostrar_cartas(cartas, mostrar = False) -> None:
    for fila in range(4):
        ace = 0
        for columna, carta in enumerate(cartas):
            valor, palo = carta
            if valor == 'a': ace += 1
            if mostrar and columna == 1: valor, palo = '*', '?'
            if fila == 0:
                print(' ___ ', end=' ')
            elif fila == 1:
                print(f'|{valor}'.ljust(4) + '|', end=' ')
            elif fila == 2:
                print(f'| {palo} |', end=' ')
            elif fila == 3:
                print('|' + f'{valor}|'.rjust(4, '_'), end=' ')
        print()
        if fila == 3 and not mostrar:
            print(f"{obtener_valor_cartas(cartas)}".rjust(len(cartas) * 5 + (len(cartas) - 1),'-'))
        if fila == 3 and obtener_valor_cartas(cartas) == 21 and len(cartas) == 2:
            print("Blackjack")
    print()

def obtener_valor_cartas(cartas) -> int:
    valor = 0
    for carta in cartas:
        if carta[0] in ['J','Q','K']:
            valor += 10
        elif carta[0] == 'A':
            if valor + 11 == 21 or valor < 11 :
                valor += 11
            elif valor + 11 > 21:
                valor += 1
        else:
            valor += carta[0]
    return valor

def pedir() -> bool:
    decision = ''
    while decision not in ['H','S']:
        decision = input("H | S\n").upper()
    return True if decision == 'H' else False




def turno_jugador(cartas) -> list:
    print("Jugador 1")
    if obtener_valor_cartas(cartas)== 21: return cartas
    while True:
        if pedir():
            cartas.append(baraja.pop())
            mostrar_cartas(cartas)
            if obtener_valor_cartas(cartas) >= 21:
                return cartas
        else:
                return cartas

def resultado(cartas) -> str:
    valor = obtener_valor_cartas(cartas)
    dealer = obtener_valor_cartas(cartas_dealer)
    if valor > 21 :
        return "Perdiste"
    elif dealer > 21 or valor > dealer:
        return "Ganaste"
    elif valor < dealer:
        return "Perdiste"
    else:
        return "Empate"

def menu():
    #print("Bienvenido a Blackjack")
    #eleccion=int(input("Si desea jugar pulse el 1\n"
     #                  "Sino desea jugar pulse el 2\n"))
    #if eleccion ==1:
        num_jugadores = int(input("¿Cuantos jugadores van a jugar? (Maximo 5):"))
        jugadores = []
        ordenadores = []
        for num in range(num_jugadores):
            jugadores.append([baraja.pop(),baraja.pop()])
        for num in range(abs(num_jugadores - 5)):
            ordenadores.append([baraja.pop(),baraja.pop()])

        print("Dealer")
        mostrar_cartas(cartas_dealer, True)

        for jugador in jugadores:
            print("Jugador")
            mostrar_cartas(jugador)

        for ordenador in ordenadores:
            print("Ordenador")
            mostrar_cartas(ordenador)

        for i in range(len(jugadores)):
            jugadores[i] = turno_jugador(jugadores[i])

        for i in range(len(ordenadores)):
            ordenadores[i] = ordenador_logica(ordenadores[i])

        crupier_logica()

        todos = jugadores + ordenadores
        i = 1
        for jugador in todos:
            print(i,resultado(jugador))
            i += 1
    #else:
     #   print("Gracias")

if 1+1==2:
    menu()


