import numpy as np
from objetos import Cromossomo


def gera_filho(cromossomo_1, cromossomo_2, ponto):
    colunas_utilizadas = np.ones(8, dtype='int') * -1
    cont = 0
    filho = Cromossomo()
    bits = cromossomo_2.bits[:3 * ponto]
    bits.insert(cromossomo_2.bits[3 * ponto:], 0)
    bits.insert(cromossomo_1.bits[:3 * ponto], 0)
    for bit in range(0, 24 + ponto * 3, 3):
        if int(bits[bit:bit + 3].bin, 2) not in colunas_utilizadas:
            coluna = int(bits[bit:bit + 3].bin, 2)
            colunas_utilizadas[cont] = coluna
            cont += 1
            filho.bits.insert(bits[bit:bit + 3], filho.bits.len)
            filho.tabuleiro[cont-1][coluna] = 1
    filho.calcular_fitness()
    return filho
