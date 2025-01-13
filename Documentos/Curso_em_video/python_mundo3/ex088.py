'''
Exercício Python 088: 
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''
import random

lista = []

jogos = int(input("Quantos jogos serão gerados?"))

print(f"Sorteando {jogos} jogos. ")
print('*' * 40)

for i in range(0,jogos):
    lista_temp = []
    for z in range(0, 6):
        lista_temp.append(random.randint(1, 60))
        
    lista.append(lista_temp[:])
    lista_temp.clear()
    print(f"O jogo {i + 1} é: {lista[i]}")
    print('=' * 40)

print("Boa Sorte!")