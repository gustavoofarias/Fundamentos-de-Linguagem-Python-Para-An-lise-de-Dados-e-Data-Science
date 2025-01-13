'''
Exercício Python 53: 
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
'''

frase = input("Digite um frase:").upper().strip()

if frase == frase[::-1]:
    print("É um palíndromo")

else:
    print("Não é um palíndromo.")