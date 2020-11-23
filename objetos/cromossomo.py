import bitstring
import numpy as np


class Cromossomo:
    def __init__(self):
        self.bits = bitstring.BitArray(bin='')
        self.fitness = 0
        self.tabuleiro = np.zeros((8, 8))

    def __repr__(self):
        return str(self.bits.bin)

    def get_fitness(self):
        return self.fitness

    def calcular_fitness(self):
        fitness = 0
        eachH = {queen + 1: 0 for queen in range(8)}
        for index_da_rainha in range(0, 8):
            linha, coluna = index_da_rainha, int(self.bits.bin[3*index_da_rainha:(index_da_rainha+1)*3], 2)
            # verificar a diagonal superior esquerda
            for i, j in zip(range(linha, -1, -1), range(coluna, -1, -1)):
                # print("Diag acima ",queen," - ", i,j)
                if self.tabuleiro[i][j] and linha != i and coluna != j:
                    fitness += 1  # soma no custo total
                    # soma nos custos individuais
                    eachH[coluna + 1] += 1
                    eachH[j + 1] += 1
            # verificar a diagonal inferior esquerda
            for i, j in zip(range(linha, 8, 1), range(coluna, -1, -1)):
                if self.tabuleiro[i][j] and linha != i and coluna != j:
                    fitness += 1  # soma no custo total
                    # soma nos custos individuais
                    eachH[coluna + 1] += 1
                    eachH[j + 1] += 1
            self.fitness = fitness
