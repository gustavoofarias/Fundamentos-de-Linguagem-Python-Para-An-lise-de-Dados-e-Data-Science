'''
Exercício Python 098: 
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1   
b) de 10 até 0, de 2 em 2   
c) uma contagem personalizada 
'''

import time

def contador(i, f, p):
    print("-" * 30)
    print(f"Contagem de {i} até {f} de {p} em {p}")
    print("-" * 30)

    if i < f:
        cont = i

        while cont <= f:
            print(f"{cont}", end='\n')  # Adiciona uma quebra de linha após cada valor
            time.sleep(0.5)
            cont += p
        print("-" * 30)
        print("FIM")

    else:
        cont = i
        while cont >= f:
            print(f"{cont}", end='\n')  # Adiciona uma quebra de linha após cada valor
            time.sleep(0.5)
            cont -= p
        print("-" * 30)
        print("FIM")

contador(1, 10, 1)
