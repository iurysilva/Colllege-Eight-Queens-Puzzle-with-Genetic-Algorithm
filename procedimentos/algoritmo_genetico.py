def algoritmo_genetico(populacao, parametros):
    for geracoes in range(parametros.geracoes):
        candidatos = populacao.seleciona_cromossomos()
        filhos = candidatos.cruza_cromossomos()
        filhos.mutacao_cromossomos()
        populacao = populacao.selecao_natural(filhos)
        if populacao.cromossomos[0].fitness == 0:
            print(geracoes)
            break
    return populacao.cromossomos[0]
