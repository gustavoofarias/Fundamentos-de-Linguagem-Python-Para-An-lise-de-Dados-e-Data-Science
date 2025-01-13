'''
Exercício Python 100: 
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los 
dentro da lista e a segunda função vai mostrar a soma entre todos os valores 
pares sorteados pela função anterior.

'''

import random


def sorteia():
   numeros = [random.randint(1,100) for i in range(5)]

   return numeros

def soma(lista):
    soma = sum(lista)

    return soma

# Programa principal

numeros_sorteado = sorteia()
print(f"Os números sorteados foram {numeros_sorteado}")

soma = sum(numeros_sorteado)

print(f"A soma dos números sorteados foi {soma}")

