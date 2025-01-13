'''
Exercício Python 37:
 Escreva um programa em Python que leia um número inteiro qualquer
   e peça para o usuário escolher qual será a base de conversão: 1 para binário,
     2 para octal e 3 para hexadecimal.
'''

numero = int(input("Digite um número:"))

base = int(input('''Qual base de conversão você quer?

[1] para binário
[2] para octal
[3] para hexadecimal
'''))

if base == 1:
    binario = bin(numero)
    print(f"O número {numero} em binário é: {binario}")

elif base == 2:
    octal = oct(numero)
    print(f"O número {numero} em octal é: {octal}")

elif base == 3:
    hexadecimal = hex(numero)
    print(f"O número {numero} em hexadecimal é: {hexadecimal}")
