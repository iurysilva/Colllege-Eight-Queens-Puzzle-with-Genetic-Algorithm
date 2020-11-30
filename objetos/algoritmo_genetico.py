import numpy as np
import time
from objetos import Populacao


class Algoritmo_Genetico:
    def __init__(self, populacao, numero_execucoes):
        self.populacao = populacao
        self.numero_execucoes = numero_execucoes
        self.iteracoes_executadas = [i for i in range(self.numero_execucoes)]
        self.resultados = [i for i in range(self.numero_execucoes)]
        self.fitness_encontrados = [i for i in range(self.numero_execucoes)]
        self.time_elapsed = np.array([])

    def realizar_execucao(self, execucao):
        for geracao in range(self.populacao.parametros.geracoes):
            if self.populacao.cromossomos[0].fitness == 0:
                self.iteracoes_executadas[execucao] = geracao
                self.resultados[execucao] = self.populacao.cromossomos[0]
                self.fitness_encontrados[execucao] = self.populacao.cromossomos[0].fitness
                return 0
            candidatos = self.populacao.seleciona_cromossomos()
            candidatos.cruza_cromossomos()
            candidatos.mutacao_cromossomos()
            self.populacao = self.populacao.selecao_natural(candidatos)
        self.iteracoes_executadas[execucao] = self.populacao.parametros.geracoes
        self.resultados[execucao] = self.populacao.cromossomos[0]
        self.fitness_encontrados[execucao] = self.populacao.cromossomos[0].fitness

    def executar(self):
        for execucao in range(self.numero_execucoes):
            time_start = time.perf_counter()
            self.populacao = Populacao(self.populacao.numero_cromossomos, self.populacao.parametros)
            self.populacao.gera_posicoes_aleatorias()
            self.populacao.ordena_populacao()
            self.realizar_execucao(execucao)
            self.time_elapsed = np.append(self.time_elapsed, time.perf_counter() - time_start)
