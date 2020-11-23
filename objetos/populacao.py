from objetos.cromossomo import Cromossomo
import numpy as np
import copy as cp


class Populacao:
    def __init__(self, numero_cromossomos, parametros):
        self.numero_cromossomos = numero_cromossomos
        self.parametros = parametros
        self.cromossomos = self.cria_cromossomos()

    def cria_cromossomos(self):
        cromossomos = np.array([])
        for cromossomo in range(0, self.numero_cromossomos):
            cromossomo = Cromossomo()
            cromossomos = np.append(cromossomos, cromossomo)
        return cromossomos

    def gera_posicoes_aleatorias(self):
        for cromossomo in range(0, self.numero_cromossomos):
            colunas_possiveis = np.arange(8)
            for linha_rainha in range(0, 8):
                coluna_rainha = np.random.choice(colunas_possiveis)
                bits = format(coluna_rainha, "#005b")
                self.cromossomos[cromossomo].bits.insert(bits, 3 * linha_rainha)
                colunas_possiveis = np.delete(colunas_possiveis, coluna_rainha)
                self.cromossomos[cromossomo].tabuleiro[linha_rainha, coluna_rainha] = 1
            self.cromossomos[cromossomo].calcular_fitness()

    def seleciona_cromossomos(self):

        nova_populacao = Populacao(self.numero_cromossomos, self.parametros)

        if nova_populacao.numero_cromossomos % 2 != 0:
            nova_populacao.numero_cromossomos += 1
            
        for i in range(nova_populacao.numero_cromossomos):
            chance_escolha = np.random.uniform(0, 1)
            cromossomo_1 = np.random.choice(self.cromossomos, replace=False)
            cromossomo_2 = np.random.choice(self.cromossomos, replace=False)
            
            if cromossomo_1.fitness <= cromossomo_2.fitness:
                cromossomo_melhor = cromossomo_1
                cromossomo_pior = cromossomo_2
            else:
                cromossomo_melhor = cromossomo_2
                cromossomo_pior = cromossomo_1

            if chance_escolha <= 0.80:
                nova_populacao.cromossomos[i] = cp.copy(cromossomo_melhor)
            else:
                nova_populacao.cromossomos[i] = cp.copy(cromossomo_pior)

        return nova_populacao
