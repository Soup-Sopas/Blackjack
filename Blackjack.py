import random

CORAZON   = chr(9829) # Character 9829 is '♥'.
DIAMANTE = chr(9830) # Character 9830 is '♦'.
PICA   = chr(9824) # Character 9824 is '♠'.
TREBOL    = chr(9827) # Character 9827 is '♣'.

NUM_BARAJAS = 6
PALOS = [CORAZON,DIAMANTE,PICA,TREBOL] * NUM_BARAJAS * 13
BARAJAS = [1,2,3,4,5,6,7,8,9,10,'J','Q','K'] * NUM_BARAJAS

random.shuffle(BARAJAS)
def crear_mazo() -> list:
    deck = []
    deck.append(BARAJAS)
    deck.append(PALOS)
    random.shuffle(deck)
    return deck

mazo = crear_mazo()
cartas_jugador = [mazo[0].pop(),mazo[1].pop()]
cartas_dealer = [mazo[0].pop()]
print(cartas_jugador)


#baraja = {CORAZON: [(1,'A'),2,3,4,5,6,7,8,9,10,(10,'J'),(10,'Q'),(10,'K')],
         # DIAMANTE: [1,2,3,4,5,6,7,8,9,10,(10,'J'),(10,'Q'),(10,'K')],
          #PICA: [1,2,3,4,5,6,7,8,9,10,(10,'J'),(10,'Q'),(10,'K')],
          #TREBOL: [1,2,3,4,5,6,7,8,9,10,(10,'J'),(10,'Q'),(10,'K')],}