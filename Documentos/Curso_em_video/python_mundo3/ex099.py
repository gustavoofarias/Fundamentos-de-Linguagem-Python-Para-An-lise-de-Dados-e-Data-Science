'''
Exercício Python 099: 
Faça um programa que tenha uma função chamada maior(), 
que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

'''


def maior(*numeros):
    maior = max(numeros)
    print("Foram informados esses valores:")
    cont = 0
    for numero in numeros:
        cont += 1
        print(numero, end=" ")
    
    # Quebra de linha
    print()
    
    print(f"Ao todo foram {cont} números")
    print(f"O maior número é: {maior}")

# Teste da função
maior(1, 2, 3, 4, 5)
