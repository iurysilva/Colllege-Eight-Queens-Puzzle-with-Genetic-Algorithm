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
        numero_de_bits_por_rainha = (self.parametros.numero_rainhas - 1).bit_length()
        numero_de_bits_por_cromossomo = numero_de_bits_por_rainha * self.parametros.numero_rainhas
        for cromossomo in range(0, self.numero_cromossomos):
            cromossomo = Cromossomo()
            palavra_do_cromossomo = '0' * numero_de_bits_por_cromossomo
            cromossomo.palavra = bitstring.BitArray(bin=palavra_do_cromossomo)
            for i in range(0, numero_de_bits_por_cromossomo):
                if np.random.uniform(0, 1) < 0.5:
                    cromossomo.palavra.overwrite('0b1', i)
            cromossomos = np.append(cromossomos, cromossomo)
        return cromossomos

