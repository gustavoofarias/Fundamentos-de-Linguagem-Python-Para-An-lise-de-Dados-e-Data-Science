'''
Exercício Python 090: 
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.
'''

nome_media = {}

nome = input("Digite seu nome:")
media = float(input("Digite sua media:"))

nome_media[nome] = media

print(nome_media)