def algoritmo_genetico(populacao, parametros):
    for geracao in range(parametros.geracoes):
        candidatos = populacao.seleciona_cromossomos()
        filhos = candidatos.cruza_cromossomos()
        filhos.mutacao_cromossomos()
        populacao = populacao.selecao_natural(filhos)
        if populacao.cromossomos[0].fitness == 0:
            populacao.cromossomos[0].tempo_de_encontro = geracao
            return populacao.cromossomos[0]
    populacao.cromossomos[0].tempo_de_encontro = parametros.geracoes
    return populacao.seleciona_cromossomos[0]
