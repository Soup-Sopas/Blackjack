import time, random
from baraja import *
from logica import *
from jugador import *

def resultado(cartas) -> str:
    valor = obtener_valor_cartas(cartas)
    dealer = obtener_valor_cartas(cartas_dealer)
    if valor > 21 :
        return f"Perdiste\n {valor}-{dealer}"
    elif dealer > 21 or valor > dealer:
        return f"Ganaste\n {valor}-{dealer}"
    elif valor < dealer:
        return f"Perdiste\n {valor}-{dealer}"
    else:
        return f"Empate\n {valor}-{dealer}"

def menu():
    # print("Bienvenido a Blackjack")
    # eleccion=int(input("Si desea jugar pulse el 1\n"
    #                  "Sino desea jugar pulse el 2\n"))
    # if eleccion ==1:
    num_jugadores = int(input("¿Cuantos jugadores van a jugar? (Maximo 5):"))
    nombres = []
    for i in range(num_jugadores):
        nombres.append(input("¿Cual es tu nombre?: "))
    jugadores = []
    ordenadores = []
    for num in range(num_jugadores):
        jugadores.append([[baraja.pop(), baraja.pop()], nombres[num]])
    for num in range(abs(num_jugadores - 5)):
        ordenadores.append([baraja.pop(), baraja.pop()])

    print("Dealer")
    mostrar_cartas(cartas_dealer, True)
    time.sleep(0.5)

    participantes = jugadores + ordenadores
    random.shuffle(participantes)

    for participante in participantes:
        if participante in jugadores:
            print(participante[1])
            mostrar_cartas(participante[0])
            time.sleep(0.5)
        else:
            print('Ordenador')
            mostrar_cartas(participante)
            time.sleep(0.5)

    for i in range(len(participantes)):
        if participantes[i] in jugadores:
            participantes[i] = turno_jugador(participantes[i])
        else:
            participantes[i] = ordenador_logica(participantes[i])
            time.sleep(0.5)

    crupier_logica()

    for participante in participantes:
        if participante in jugadores:
            print(participante[1], resultado(participante[0]))
        else:
            print("Ordenador", resultado(participante))
    #else:
     #   print("Gracias")

if 1+1==2:
    menu()


