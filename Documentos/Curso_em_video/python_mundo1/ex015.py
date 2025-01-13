'''
Exercício Python 15: 
Escreva um programa que pergunte a quantidade de Km percorridos
 por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
 Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

km_percorrido = float(input("Digite quantos km você pecorreu:"))
dias = int(input("Digite quantos dias que você quer alugar:"))

carro = 60
km = 0.15

calculo = (km_percorrido * km) + (carro * dias)

print(f"Para o aluguel do carro você terá que pagar {calculo}R$")