'''
Exercício Python 45: 
Crie um programa que faça o computador jogar Jokenpô com você.
'''

import random

print(''' Suas opções:
[1] PAPEL
[2] TESOURA
[3] PEDRA''')

escolha = input("Escolha uma opção: ")

computador = random.choice(['papel', 'tesoura', 'pedra'])

if escolha == '1':
    if computador == 'tesoura':
        print("Você venceu!")
    elif computador == 'pedra':
        print("Você perdeu.")
    else:
        print("Empate!")
elif escolha == '2':
    if computador == 'pedra':
        print("Você venceu!")
    elif computador == 'papel':
        print("Você perdeu.")
    else:
        print("Empate!")
elif escolha == '3':
    if computador == 'papel':
        print("Você venceu!")
    elif computador == 'tesoura':
        print("Você perdeu.")
    else:
        print("Empate!")
else:
    print("Escolha inválida.")
