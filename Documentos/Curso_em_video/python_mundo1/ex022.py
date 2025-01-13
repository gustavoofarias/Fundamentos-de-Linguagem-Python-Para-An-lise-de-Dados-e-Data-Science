'''
Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.
'''

nome = str(input("Digite seu nome:"))

maiuscula = nome.upper()
minuscula = nome.lower()
letras = len(nome.replace(" ", ""))
letras_primeiro = len(nome.split()[0])

print(f"{maiuscula}")
print(f"{minuscula}")
print(f"{letras}")
print(f"{letras_primeiro}")
