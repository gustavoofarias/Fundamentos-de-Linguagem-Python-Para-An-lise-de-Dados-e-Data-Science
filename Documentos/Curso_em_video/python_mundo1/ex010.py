'''
Exercício Python 10:
 Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e 
 mostre quantos dólares ela pode comprar.
'''


dinheiro = float(input("Digite quanto dinheiro você tem na carteira: "))
dolar = 5.50
conversao = dinheiro / dolar

print(f"Você tem {dinheiro}R$ na carteira e em dólares isso é {conversao:.2f}$")
