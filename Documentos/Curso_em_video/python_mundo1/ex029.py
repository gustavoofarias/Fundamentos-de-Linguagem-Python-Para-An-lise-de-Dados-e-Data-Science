'''
Exercício Python 29: 
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''


velocidade_carro = int(input("Digite a velocidade do carro:"))
limite = 80
multa = 7.00

if velocidade_carro > 80:
    print(f"Você foi multado!")
    multa_preco = (velocidade_carro - limite) * multa
    print(f"Você vai ter que pagar {multa_preco}R$ de multa.")

else:
    print("Você não foi multado.")
