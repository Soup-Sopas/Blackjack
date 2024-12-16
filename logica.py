import random
from baraja import *

baraja = crear_baraja()
cartas_dealer = [baraja.pop(), baraja.pop()]

def crupier_logica():
    print("Dealer")
    while obtener_valor_cartas(cartas_dealer) < 17:
        mostrar_cartas(cartas_dealer)
        cartas_dealer.append(baraja.pop())
    mostrar_cartas(cartas_dealer)

def ordenador_logica(cartas)-> list:
    tipo = random.randint(1,3)
    valor_dealer = obtener_valor_cartas([cartas_dealer[0], (0, '*')])
    match tipo:
        case 1:
            print("Ordenador 1")
            while obtener_valor_cartas(cartas) <= 11 or (obtener_valor_cartas(cartas) == 12 and 4 <= valor_dealer >= 6) or (13 <= obtener_valor_cartas(cartas) >= 16 and valor_dealer >= 7):
                print(obtener_valor_cartas(cartas))
                if obtener_valor_cartas(cartas) >= 17:
                    print("Hola")
                    break

                mostrar_cartas(cartas)
                cartas.append(baraja.pop())
            mostrar_cartas(cartas)
            return cartas
        case 2:
            print("Ordenador 2")
            while obtener_valor_cartas(cartas) <= 16:
                mostrar_cartas(cartas)
                cartas.append(baraja.pop())
            mostrar_cartas(cartas)
            return cartas
        case 3:
            print("Ordenador 3")
            while obtener_valor_cartas(cartas) <= 14:
                mostrar_cartas(cartas)
                cartas.append(baraja.pop())
            mostrar_cartas(cartas)
            return cartas

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
