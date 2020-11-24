from objetos import Parametros, Populacao


geracoes = 10
numero_de_cromossomos = 5
taxa_de_mutacao = 0.80
taxa_de_crossover = 0.01
taxa_de_escolha_cromossomo = 0.80

parametros = Parametros(geracoes, taxa_de_mutacao, taxa_de_crossover, taxa_de_escolha_cromossomo)
populacao = Populacao(numero_de_cromossomos, parametros)
populacao.gera_posicoes_aleatorias()
candidatos = populacao.seleciona_cromossomos()
filhos = candidatos.cruza_cromossomos()
filhos.mutacao_cromossomos()
populacao = populacao.selecao_natural(filhos)
