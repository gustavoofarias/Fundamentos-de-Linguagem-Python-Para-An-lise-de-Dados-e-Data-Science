'''
Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros
'''


valor_pago = float(input("Digite o valor a ser pago:"))

escolha = int(input('''
[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3]  em até 2x no cartão: preço formal
[4] 3x ou mais no cartão: 20% de juros '''))

if escolha == 1:
    pagamento = valor_pago - (valor_pago * 0.1)
    print(f"Você vai ter que pagar {pagamento}R$ ")

elif escolha == 2:
    pagamento = valor_pago - (valor_pago * 0.05)
    print(f"Você vai ter que pagar {pagamento}R$ ")

elif escolha == 3:
    pagamento = valor_pago / 2
    print(f"Você vai ter que pagar 2x de {pagamento}R$ ")

elif escolha == 4:
    pagamento = valor_pago + ( valor_pago * 0.2)
    print(f"Você vai ter que pagar {pagamento}R$ ")



