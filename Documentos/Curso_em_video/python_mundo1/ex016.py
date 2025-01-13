from math import trunc
'''
Exercício Python 16:
 Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''

numero = float(input("Digite um número:"))

converter = trunc(numero)

print(f"O número real é {numero} e sua porcão inteira é {converter}")


