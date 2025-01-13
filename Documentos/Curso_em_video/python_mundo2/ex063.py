'''
Exercício Python 63: 
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
'''
contador = 0
num = 0
num1 = 1

numero = int(input("Digite um número: "))

while contador < numero:
    print(num)
    fibonacci = num + num1
    num = num1
    num1 = fibonacci
    contador += 1
