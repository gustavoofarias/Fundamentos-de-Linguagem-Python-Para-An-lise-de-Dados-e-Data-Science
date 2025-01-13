'''
Exercício Python 46: 
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''
from time import sleep

contador = 10
for i in range(1,12):
    print(f"Contagem regressiva para os fogos: {contador}")
    sleep(1)
    contador -= 1
    if contador == 0:
        print("Feliz ano novo!")