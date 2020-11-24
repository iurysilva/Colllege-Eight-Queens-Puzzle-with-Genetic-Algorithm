from objetos import Parametros, Populacao
from procedimentos import algoritmo_genetico


geracoes = 1000
numero_de_cromossomos = 20
taxa_de_mutacao = 0.80
taxa_de_crossover = 0.01
taxa_de_escolha_cromossomo = 0.80

parametros = Parametros(geracoes, taxa_de_mutacao, taxa_de_crossover, taxa_de_escolha_cromossomo)
populacao = Populacao(numero_de_cromossomos, parametros)
populacao.gera_posicoes_aleatorias()
resultado = algoritmo_genetico(populacao, parametros)
print("iterações necessárias: ", resultado.tempo_de_encontro)
print("bits do melhor cromossomos", resultado)
print("fitness: ", resultado.fitness)
print("tabuleiro encontrado")
print(resultado.tabuleiro)
