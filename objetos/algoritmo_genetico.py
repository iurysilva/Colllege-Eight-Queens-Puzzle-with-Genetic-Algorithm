class Algoritmo_Genetico:
    def __init__(self, populacao, parametros):
        self.populacao = populacao
        self.parametros = parametros
        self.iteracoes_executadas = 0

    def executar(self):
        for geracao in range(self.parametros.geracoes):
            candidatos = self.populacao.seleciona_cromossomos()
            filhos = candidatos.cruza_cromossomos()
            filhos.mutacao_cromossomos()
            populacao = self.populacao.selecao_natural(filhos)
            if populacao.cromossomos[0].fitness == 0:
                self.iteracoes_executadas = geracao
                return populacao.cromossomos[0]
        self.iteracoes_executadas = self.parametros.geracoes
        return self.populacao.seleciona_cromossomos[0]
