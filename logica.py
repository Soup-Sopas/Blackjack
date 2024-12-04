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
    match tipo:
        case 1:
            print("Ordenador 1")
            while obtener_valor_cartas(cartas) <= 15:
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
