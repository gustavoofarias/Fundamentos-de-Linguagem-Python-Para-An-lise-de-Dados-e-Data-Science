'''
Exercício Python 20: 
O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
import random

import random

lista_alunos = []


for i in range(0, 4):
    aluno = input("Digite o nome do aluno: ")
    lista_alunos.append(aluno)


random.shuffle(lista_alunos)

print(f"{lista_alunos}")

