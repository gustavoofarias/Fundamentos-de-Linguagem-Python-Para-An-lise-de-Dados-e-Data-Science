'''
Exercício Python 19:
 Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
 Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''
import random

lista = []

for i in range(1, 5):
    aluno = input("Qual o nome do aluno: ")
    lista.append(aluno)

sorteado = random.choice(lista)

print(f"O aluno sorteado foi {sorteado}!")
