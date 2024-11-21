import random

CORAZON   = chr(9829) # Character 9829 is '♥'.
DIAMANTE = chr(9830) # Character 9830 is '♦'.
PICA   = chr(9824) # Character 9824 is '♠'.
TREBOL    = chr(9827) # Character 9827 is '♣'.

NUM_BARAJAS = 6
PALOS = [CORAZON,DIAMANTE,PICA,TREBOL] * 13 * NUM_BARAJAS
VALORES = [2,3,4,5,6,7,8,9,10,'J','Q','K','A'] * 4 * NUM_BARAJAS

def crear_baraja() -> list:
    baraja = []
    for i in range(len(VALORES)):
        baraja.append((VALORES[i], PALOS[i]))
    random.shuffle(baraja)
    return baraja

def mostrar_cartas(cartas) -> None:
    for fila in range(4):
        for columna, carta in enumerate(cartas):
            valor, palo = carta
            if fila == 0:
                print(' ___ ', end=' ')
            elif fila == 1:
                print(f'|{valor}  |', end=' ')
            elif fila == 2:
                print(f'| {palo} |', end=' ')
            elif fila == 3:
                print(f'|__{valor}|', end=' ')
        print()


baraja = crear_baraja()
cartas_jugador = [baraja.pop(),baraja.pop()]
mostrar_cartas(cartas_jugador)