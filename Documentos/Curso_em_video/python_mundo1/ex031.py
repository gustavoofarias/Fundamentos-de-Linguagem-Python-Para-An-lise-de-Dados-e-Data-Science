'''
Exercício Python 31: 
Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''

distancia = float(input("Digite quantos km quer percorrer:"))

viagem_curta = 0.50
viagem_longa = 0.45

if distancia <= 200:
    preco_passagem = distancia * viagem_curta
    print(f"O preço da passagem é {preco_passagem}R$")

elif distancia > 200:
    preco_passagem = distancia * viagem_longa
    print(f"O preço da passagem é {preco_passagem}R$")


