'''
Exercício Python 68: 
Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
import random

contador = 0
while True:
    numero = int(input("Digite um número:"))
    par_impar = input("Você quer ser par ou impar?").upper()
    computador = random.randint(1,10)

    if par_impar == "PAR":
        if (numero + computador) % 2 == 0:
            contador += 1
            print(f"Você escolheu {numero} o computador {computador} o que da {numero + computador}")
            print("Você venceu") 
        else:
            print(f"Você escolheu {numero} o computador {computador} o que da {numero + computador}")
            print(f"Você perdeu!")
            print(f"Você ganhou {contador} seguidas")
            break

    elif par_impar == "IMPAR":
        if (numero + computador) % 2 == 1:
            contador += 1
            print(f"Você escolheu {numero} o computador {computador} o que da {numero + computador}")
            print("Você venceu") 
        else:
            print(f"Você escolheu {numero} o computador {computador} o que da {numero + computador}")
            print(f"Você perdeu!")
            print(f"Você ganhou {contador} seguidas")
            break
            

            

    

