from objetos import Parametros, Populacao
import numpy as np
import bitstring


geracoes = 10
numero_de_cromossomos = 2
taxa_de_mutacao = 0.80
taxa_de_crossover = 0.01
taxa_de_escolha_cromossomo = 0.80

parametros = Parametros(geracoes, taxa_de_mutacao, taxa_de_crossover, taxa_de_escolha_cromossomo)
populacao = Populacao(numero_de_cromossomos, parametros)
nova_populacao = populacao.seleciona_cromossomos()

for cromossomo in range(0, numero_de_cromossomos):
    print("Rainhas se atacando ", populacao.cromossomos[cromossomo].fitness)
    print("bits: ", populacao.cromossomos[cromossomo].bits.bin)
    print(populacao.cromossomos[cromossomo].tabuleiro)

'''
for cromossomo in range(0, numero_de_cromossomos):
    print("Rainhas se atacando ", nova_populacao.cromossomos[cromossomo].fitness)
    print("bits: ", nova_populacao.cromossomos[cromossomo].bits.bin)
    print(nova_populacao.cromossomos[cromossomo].tabuleiro)
'''