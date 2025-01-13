'''
Exercício Python 9:
 Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

'''

num = int(input("Digite um número:"))
multiplicador = 1
for i in range(1,11):
    tabuada = num * multiplicador
    print(f"A multiplicação de {num} x {multiplicador} é {tabuada}")
    multiplicador += 1
    
