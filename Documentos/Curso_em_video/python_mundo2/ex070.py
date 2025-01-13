'''
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
'''

# Inicialize as variáveis contadoras e listas
contador_acima_1000 = 0
lista_produtos = []
total_gasto = 0

while True:
    # Solicite o nome e o preço do produto
    nome = input("Qual o nome do produto: ")
    preco = float(input("Qual o preço do produto: "))

    # Adicione o produto à lista de produtos
    lista_produtos.append((nome, preco))

    # Adicione o preço do produto ao total gasto
    total_gasto += preco

    # Verifique se o preço do produto é maior que R$1000
    if preco > 1000:
        contador_acima_1000 += 1

    # Verifique se o usuário deseja continuar
    continuar = input("Você deseja continuar (SIM ou NÃO)? ").upper()
    if continuar != "SIM":
        break  # Sai do loop se a resposta não for SIM

# Verifique se foram inseridos produtos
if lista_produtos:
    # Calcule o produto mais barato
    produto_mais_barato = min(lista_produtos, key=lambda x: x[1])

    # Exiba os resultados
    print(f"Total gasto na compra: R${total_gasto:.2f}")
    print(f"Quantidade de produtos acima de R$1000: {contador_acima_1000}")
    print(f"Nome do produto mais barato: {produto_mais_barato[0]}")
else:
    print("Nenhum produto inserido.")



