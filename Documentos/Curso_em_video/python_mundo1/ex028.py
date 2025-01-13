'''
Exercício Python 28:
 Escreva um programa que faça o computador “pensar”
 em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir 
 qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
import random

numero_usuario = int(input("Digite um número de 0 a 5: "))

if 0 <= numero_usuario <= 5:
    numero_sorteado = random.randint(0, 5)
    
    print(f"O número sorteado foi: {numero_sorteado}")

    if numero_sorteado == numero_usuario:
        print("Parabéns! Você venceu!")
    else:
        print("Você perdeu. Tente novamente.")
else:
    print("Número fora do intervalo permitido (0 a 5).")
