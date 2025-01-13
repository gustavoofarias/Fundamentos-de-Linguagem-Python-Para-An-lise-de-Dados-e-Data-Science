'''
Exercício Python 58: 
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''

import random 

numero_sorteado = random.randint(0,10)

tentativas = 0

while True:
    numero_usuario = int(input("Digite um número de 0 10:"))
    tentativas += 1

    if numero_usuario == numero_sorteado:
        print(f"Você venceu em {tentativas} tentativas.")
        break

    else:
        print("Você perdeu.")
