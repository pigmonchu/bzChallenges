import random

_PALOS = ['o', 'c', 'e', 'b']
_FIGURAS = ['A', '2', '3', '4', '5','6', '7', 'S', 'C', 'R' ]
def create_deck():
    b = []
    for p in _PALOS:
        for f in _FIGURAS:
            b.append(f+p)
    
    return b

def eligeCarta(maxn, excepted):
    ix = random.randrange(0, maxn)
    while ix == excepted:
        ix = random.randrange(0, maxn)
    return ix

def shuffle_deck(baraja):
    for idx, naipe in enumerate(baraja):
        alazar = eligeCarta(len(baraja), idx)
        baraja[idx] = baraja[alazar]
        baraja[alazar] = naipe

class Baraja():
    __PALOS = ['o', 'c', 'e', 'b']
    __FIGURAS = ['A', '2', '3', '4', '5','6', '7', 'S', 'C', 'R' ]
    
    def __init__(self):
        self.naipes = []
        for p in self.__PALOS:
            for f in self.__FIGURAS:
                self.naipes.append(f+p)

    def __eligeCarta(self, maxn, excepted):
        '''
        Función de apoyo.
        Elige un entero al azar entre 0 y maxn (excluido) evitando el valor de excepted
        '''
        ix = random.randrange(0, maxn)
        while ix == excepted:
            ix = random.randrange(0, maxn)
        return ix
    
    def shuffle(self):
        for idx, naipe in enumerate(self.naipes):
            alazar = self.__eligeCarta(len(self.naipes), idx)
            self.naipes[idx] = self.naipes[alazar]
            self.naipes[alazar] = naipe

    def distribute(self, mano, jugadores):
        manos = []
        for j in range(jugadores):
            reparto = []
            for m in range(mano):
                reparto.append(self.naipes.pop(0))
            manos.append(reparto)
        return manos

