from objects import Parametros, Populacao


geracoes = 10
numero_de_rainhas = 4
numero_de_cromossomos = 2
taxa_de_mutacao = 0.80
taxa_de_crossover = 0.01

parametros = Parametros(geracoes, numero_de_rainhas, taxa_de_mutacao, taxa_de_crossover)
populacao = Populacao(numero_de_cromossomos, parametros)

