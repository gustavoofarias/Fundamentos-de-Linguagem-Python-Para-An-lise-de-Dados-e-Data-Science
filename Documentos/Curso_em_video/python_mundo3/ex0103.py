'''
Exercício Python 103: 
Faça um programa que tenha uma função chamada ficha(),
 que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador,
 mesmo que algum dado não tenha sido informado corretamente.

'''


def ficha(nome='Nome', gols= 0):
   
    print('-' * 30)
    print(f"Jogador: {nome}")
    print('-' * 30)
    print(f"Gols: {gols}")
    print('-' * 30)

    
    

ficha("Gustavo", 35)