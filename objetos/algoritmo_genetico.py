class Algoritmo_Genetico:
    def __init__(self, populacao, parametros, numero_execucoes):
        self.populacao = populacao
        self.parametros = parametros
        self.numero_execucoes = numero_execucoes
        self.iteracoes_executadas = [i for i in range(self.numero_execucoes)]
        self.resultados = [i for i in range(self.numero_execucoes)]

    def executar(self):
        for execucao in range(self.numero_execucoes):
            self.populacao.gera_posicoes_aleatorias()
            encontrou = False
            for geracao in range(self.parametros.geracoes):
                candidatos = self.populacao.seleciona_cromossomos()
                filhos = candidatos.cruza_cromossomos()
                filhos.mutacao_cromossomos()
                self.populacao = self.populacao.selecao_natural(filhos)
                if self.populacao.cromossomos[0].fitness == 0:
                    self.iteracoes_executadas[execucao] = geracao
                    self.resultados[execucao] = self.populacao.cromossomos[0]
                    encontrou = True
                    break
            if not encontrou:
                self.iteracoes_executadas[execucao] = self.parametros.geracoes
                self.resultados[execucao] = self.populacao.cromossomos[0]
