'''
Exercício Python 5: 
Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

'''

entrada = int(input("Digite um número:"))

antecessor = entrada - 1
sucessor = entrada + 1

print(f"O antecessor do número {entrada} é {antecessor}.")
print(f"O sucessor do número {entrada} é {sucessor}.")