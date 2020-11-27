from objetos import Parametros, Populacao, Algoritmo_Genetico
import numpy as np

geracoes = 1000
numero_de_execucoes = 2
numero_de_cromossomos = 20
taxa_de_mutacao = 0.80
taxa_de_crossover = 0.01
taxa_de_escolha_cromossomo = 0.80

parametros = Parametros(geracoes, taxa_de_mutacao, taxa_de_crossover, taxa_de_escolha_cromossomo)
populacao = Populacao(numero_de_cromossomos, parametros)
algoritmo_genetico = Algoritmo_Genetico(populacao, numero_de_execucoes)

algoritmo_genetico.executar()


for execucao in range(numero_de_execucoes):
    print("iterações necessárias: ", algoritmo_genetico.iteracoes_executadas[execucao])
    print("bits", algoritmo_genetico.resultados[execucao])
    print("fitness: ", algoritmo_genetico.fitness_encontrados[execucao])
    print("Tempo de execução: ", algoritmo_genetico.time_elapsed[execucao])
    print("tabuleiro encontrado")
    print(algoritmo_genetico.resultados[execucao].tabuleiro)
    print("---------------------------------------------")


print()
print("Média dos fitness: ", np.mean(algoritmo_genetico.fitness_encontrados))
print("Desvio padrão dos fitness: ", np.std(algoritmo_genetico.fitness_encontrados))
print()
print("Média dos tempos de execução: ", np.mean(algoritmo_genetico.time_elapsed))
print("Desvio padrão dos tempos de execução: ", np.std(algoritmo_genetico.time_elapsed))
print()
print("Média de Gerações: ", np.mean(algoritmo_genetico.iteracoes_executadas))
print("Desvio padrão de Gerações: ", np.std(algoritmo_genetico.iteracoes_executadas))