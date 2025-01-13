'''
Exercício Python 038: 
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais
'''

numero = int(input("Digite um número:"))
numero2 = int(input("Digite um número:"))

if numero > numero2:
    print("O primeiro valor é maior.")

elif numero2 > numero:
    print("O segundo valor é maior.")

else:
    print("Os dois valores são iguais.")


