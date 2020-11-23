from objetos.cromossomo import Cromossomo
import numpy as np
import copy as cp


class Populacao:
    def __init__(self, numero_cromossomos, parametros=False):
        self.numero_cromossomos = numero_cromossomos
        self.parametros = parametros
        self.cromossomos = self.cria_cromossomos()

    def cria_cromossomos(self):
        return [Cromossomo() for _ in range(self.numero_cromossomos)]

    def gera_posicoes_aleatorias(self):
        for cromossomo in range(0, self.numero_cromossomos):
            colunas = np.arange(0, 8)
            np.random.shuffle(colunas)
            for linha_rainha in range(0, 8):
                coluna_rainha = colunas[linha_rainha]
                bits = format(coluna_rainha, "#005b")
                self.cromossomos[cromossomo].bits.insert(bits, 3 * linha_rainha)
                self.cromossomos[cromossomo].tabuleiro[linha_rainha, coluna_rainha] = 1
            self.cromossomos[cromossomo].calcular_fitness()

    def seleciona_cromossomos(self):
        numero_cromossomos = self.numero_cromossomos
        if numero_cromossomos % 2 != 0:
            numero_cromossomos += numero_cromossomos + 1
        nova_populacao = Populacao(numero_cromossomos, self.parametros)
        for i in range(nova_populacao.numero_cromossomos):
            chance_escolha = np.random.uniform(0, 1)
            cromossomo_1 = np.random.choice(self.cromossomos)
            cromossomo_2 = np.random.choice(self.cromossomos)
            while cromossomo_2.bits == cromossomo_1.bits:
                cromossomo_2 = np.random.choice(self.cromossomos)
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

    def gera_filho(self, cromossomo_1, cromossomo_2, ponto):
        colunas_utilizadas = np.ones(8, dtype='int') * -1
        cont = 0
        filho = Cromossomo()
        bits = cromossomo_2.bits[:3*ponto]
        bits.insert(cromossomo_2.bits[3*ponto:], 0)
        bits.insert(cromossomo_1.bits[:3*ponto], 0)
        for bit in range(0, 24+ponto*3, 3):
            if int(bits[bit:bit+3].bin, 2) not in colunas_utilizadas:
                colunas_utilizadas[cont] = int(bits[bit:bit+3].bin, 2)
                cont += 1
                filho.bits.insert(bits[bit:bit+3], filho.bits.len)
        return filho

    def cruza_cromossomos(self, nova_populacao):
        populacao_pos_cruzamento = Populacao(nova_populacao.numero_cromossomos, self.parametros)
        for cromossomo in range(nova_populacao.numero_cromossomos//2):
            ponto = np.random.randint(1, 8)
            pai = nova_populacao.cromossomos[cromossomo]
            mae = nova_populacao.cromossomos[cromossomo+1]
            filho_1 = self.gera_filho(pai, mae, ponto)
            filho_2 = self.gera_filho(mae, pai, ponto)
            populacao_pos_cruzamento.cromossomos[cromossomo] = filho_1
            populacao_pos_cruzamento.cromossomos[cromossomo+1] = filho_2
        return populacao_pos_cruzamento


