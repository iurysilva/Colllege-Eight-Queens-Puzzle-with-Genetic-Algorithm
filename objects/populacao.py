from objects.cromossomo import Cromossomo
import numpy as np
import bitstring


class Populacao:
    def __init__(self, numero_cromossomos, parametros):
        self.numero_cromossomos = numero_cromossomos
        self.parametros = parametros
        self.cromossomos = self.cria_cromossomos()

    def cria_cromossomos(self):
        cromossomos = np.array([])
        for cromossomo in range(0, self.numero_cromossomos):
            colunas_possiveis = np.array([0, 1, 2, 3, 4, 5, 6, 7])
            cromossomo = Cromossomo()
            cromossomo.bits = bitstring.BitArray(bin='')
            for linha_rainha in range(0, 8):
                coluna_rainha = colunas_possiveis[np.random.randint(0, len(colunas_possiveis))]
                bits = format(coluna_rainha, "#005b")
                cromossomo.bits.insert(bits, 3*linha_rainha)
                colunas_possiveis = np.delete(colunas_possiveis, np.where(colunas_possiveis == coluna_rainha))
                cromossomo.tabuleiro[linha_rainha, coluna_rainha] = 1
            cromossomo.calcular_fitness()
            cromossomos = np.append(cromossomos, cromossomo)
        return cromossomos
